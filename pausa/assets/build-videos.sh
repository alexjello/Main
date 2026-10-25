#!/usr/bin/env bash
# Assembles the five ad videos + landing explainer from the Higgsfield clips and Ana's voiceovers.
# Needs ffmpeg. Run fetch-assets.sh first. Output goes to assets/final/.
# Text overlays use the copy in ads/copy-and-captions.md; edit the TXT_* variables to change them.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p final tmp
FONT="${FONT:-/System/Library/Fonts/Supplemental/Arial Bold.ttf}"; [ -f "$FONT" ] || FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf

# normalize a clip to 1080x1920 (9:16) with blurred fill, 30 fps, no audio
norm(){ ffmpeg -y -loglevel error -i "video/$1.mp4" -vf "split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30[bg];[b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,fps=30,format=yuv420p" -an "tmp/$1.v.mp4"; }
for c in clip1-hero-pushin-6s clip2-hijo-toque-9x16-6s clip3-cena-6s clip4-mano-toque-5s clip5-familia-sofa-5s clip6-sobre-unboxing-5s clip7-antes-despues-5s clip8-tarea-5s; do norm "$c"; done
# still → 4 s clip
stillclip(){ ffmpeg -y -loglevel error -loop 1 -t 4 -i "images/$1.png" -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z='min(zoom+0.0008,1.08)':d=120:s=1080x1920,fps=30,format=yuv420p" -an "tmp/$1.v.mp4"; }
stillclip 07-sobre; stillclip 01-hero-disco

# concat helper: $1 = out name, $2 = audio file, rest = ordered clip names
assemble(){ out=$1; vo=$2; shift 2; : > tmp/list.txt; for c in "$@"; do echo "file '$PWD/tmp/$c.v.mp4'" >> tmp/list.txt; done
  ffmpeg -y -loglevel error -f concat -safe 0 -i tmp/list.txt -i "audio/$vo" -filter_complex "[1:a]aformat=sample_rates=48000,apad[a]" -map 0:v -map "[a]" -shortest -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k "final/$out.mp4"; }

# V1 La cena (VO 24.7 s): cena, toque, mano, familia, sobre
assemble V1-la-cena-9x16 vo1-cena.mp3 clip3-cena-6s clip2-hijo-toque-9x16-6s clip4-mano-toque-5s clip5-familia-sofa-5s 07-sobre
# V2 La tarea (22.2 s): tarea, toque, hijo, sobre
assemble V2-la-tarea-9x16 vo2-tarea.mp3 clip8-tarea-5s clip2-hijo-toque-9x16-6s clip4-mano-toque-5s clip6-sobre-unboxing-5s 07-sobre
# V3 Somos familia (29.2 s): familia, antes/despues, hero, cena, abuela(still), sobre
assemble V3-somos-familia-9x16 vo3-familia.mp3 clip5-familia-sofa-5s clip7-antes-despues-5s clip1-hero-pushin-6s clip3-cena-6s clip6-sobre-unboxing-5s 01-hero-disco
# V4 Retargeting (11.6 s): hero, sobre
assemble V4-sigue-aqui-9x16 vo5-retargeting.mp3 clip1-hero-pushin-6s clip6-sobre-unboxing-5s 07-sobre
# V5 Landing explainer (52.4 s): all eight clips + two stills (≈51 s)
assemble landing-explainer-9x16 vo4-landing.mp3 clip7-antes-despues-5s clip1-hero-pushin-6s clip6-sobre-unboxing-5s clip8-tarea-5s clip4-mano-toque-5s clip2-hijo-toque-9x16-6s clip3-cena-6s clip5-familia-sofa-5s 01-hero-disco 07-sobre
# 16:9 version of the explainer for the landing page (letterbox the 9:16 master onto a sage background)
ffmpeg -y -loglevel error -i final/landing-explainer-9x16.mp4 -vf "scale=-2:1080,pad=1920:1080:(ow-iw)/2:0:color=0x2F4536" -c:a copy final/landing-explainer.mp4
cp final/landing-explainer.mp4 video/landing-explainer.mp4
echo "built: $(ls final)"
echo "Text overlays: add in CapCut/Premiere from the tables in ads/copy-and-captions.md (section 5), or uncomment the drawtext block below."
# Example burned-in caption (Spanish, white, bottom third):
# ffmpeg -i final/V1-la-cena-9x16.mp4 -vf "drawtext=fontfile='$FONT':text='¿Cuándo fue la última cena sin teléfonos?':fontsize=58:fontcolor=white:borderw=3:bordercolor=black@0.6:x=(w-text_w)/2:y=h*0.72:enable='between(t,0,3)'" -c:a copy final/V1-captioned.mp4
