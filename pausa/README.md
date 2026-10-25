# Pausa · launch kit (discos únicamente)

Everything needed to sell the **Disco Pausa** ($34) and **Pack Familiar** ($79) by mail. Spanish-first, family-owned positioning, Ana (ElevenLabs) voice. Nothing here touches GoHighLevel or any ad account; you import it.

## Live artifacts
| What | Link |
|---|---|
| Media buying plan (TOF / MOF / BOF / retargeting / retention, budgets, KPIs, kill rules, launch calendar) | https://claude.ai/artifact/QSK38pJQYWkMPPhadxZQnm |
| Landing page + sales page + checkout + thank-you (one artifact, four pages) | https://claude.ai/artifact/KBfLw97L8TLZS9FqMEawsZ |
| Ad creative review board (12 stills with copy, 5 voiceovers, clip links, storyboards, 20 hooks, captions) | https://claude.ai/artifact/ACn6LU81e25QcaXK2or5nb |
| Guía Familiar (parent program, web version + PDF) | https://claude.ai/artifact/LamAC9sX36ZhEeiE7Mnfzp |

## Folder map
```
pausa/
  index.html              landing page (artifact format: no <html>/<head>; see dist/ for standalone)
  funnel/sales.html       long-form sales page with order box (Disco / Pack + $19 bump)
  funnel/checkout.html    checkout form; replace the dashed block with the GHL/Stripe payment element
  funnel/gracias.html     thank-you + one-click Pack Comunidad upsell ($39)
  dist/                   standalone copies of the four pages + assets, ready to paste into GHL custom-code pages
  media-plan/             the media plan page
  ads/copy-and-captions.md   all copy: angles, 20 hooks, 6 statics, carousel, 8 captions, 4 video scripts, email/SMS
  ads/pausa-ad-creative.html review board page
  pdf/programa-pausa.html    print source (Letter, 11 pages) · pdf/programa-pausa.pdf · pdf/guia-familiar-web.html
  brand/brand.md          offer, voice, palette, voice IDs
  assets/images/          12 stills (jpg + webp) from Higgsfield
  assets/audio/           5 Ana voiceovers (mp3)
  assets/manifest.json    permanent URLs of the 12 stills and 8 motion clips
  assets/fetch-assets.sh  downloads clips (run on your Mac; the cloud sandbox cannot reach the Higgsfield CDN)
  assets/build-videos.sh  ffmpeg: stitches clips + voiceovers into V1–V4 (9:16) and the landing explainer
  build-dist.sh           regenerates dist/
```

## To go live (order of operations)
1. `bash assets/fetch-assets.sh && bash assets/build-videos.sh` on a machine with open internet. This produces `assets/final/*.mp4` and drops `landing-explainer.mp4` where the landing page expects it. Until then the landing plays Ana's voiceover over the stills with the same timing, so the page already works.
2. Add captions to the four ad videos (tables in `ads/copy-and-captions.md`, section 5) in CapCut or Premiere, or use the drawtext example at the bottom of `build-videos.sh`.
3. `bash build-dist.sh`, then paste each `dist/*.html` into a GHL funnel step as custom code. Upload `dist/assets/` to GHL media and replace the relative paths, or host the folder anywhere and keep the paths.
4. In `checkout.html`, swap the dashed placeholder for the GHL payment element; connect the thank-you button to the one-click upsell product.
5. Install Meta Pixel + CAPI and TikTok pixel in GHL. The pages already fire `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`, `VideoPlay` and `VideoWatched75`.
6. Build the campaigns exactly as laid out in the media plan (account structure section). Start at $50/day, TOF only.

## Placeholders to replace before launch
- Brand name **Pausa**, email `hola@pausa.family`, and the family story wording in `index.html`, `funnel/*.html`, `pdf/programa-pausa.html` (search "familia detrás de Pausa").
- Prices and COGS in `brand/brand.md` and the media plan's unit-economics tiles.
- App store names in the PDF (page 3) once the real app is listed.

## Generation record
- Stills: Higgsfield `gpt_image_2_5`, 12 jobs (ids in `assets/manifest.json`).
- Clips: Higgsfield `seedance_2_5`, 8 jobs, 5–6 s, 720p, no model audio.
- Voice: ElevenLabs voice "Ana" (`tr6YFWVGFIcVUGrOMYMV`), model `eleven_v4`, flow https://elevenlabs.io/app/flows/ONdyhhCogJtcztV5RdCY (also holds the 12 stills as reference nodes).
