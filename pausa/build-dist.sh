#!/usr/bin/env bash
# Wraps the artifact-format pages (no doctype/head) into standalone HTML files for GoHighLevel custom-code pages or any host.
set -euo pipefail; cd "$(dirname "$0")"; mkdir -p dist/funnel dist/assets
wrap(){ src=$1; out=$2; { printf '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'; sed -n '1,/<\/style>/p' "$src"; printf '</head>\n<body>\n'; sed '1,/<\/style>/d' "$src"; printf '\n</body>\n</html>\n'; } > "$out"; }
wrap index.html dist/index.html
for p in sales checkout gracias; do wrap funnel/$p.html dist/funnel/$p.html; done
cp -r assets/images dist/assets/ 2>/dev/null || true; mkdir -p dist/assets/audio dist/assets/video; cp assets/audio/*.mp3 dist/assets/audio/; [ -f assets/video/landing-explainer.mp4 ] && cp assets/video/landing-explainer.mp4 dist/assets/video/ || true
rm -f dist/assets/images/*.webp dist/assets/images/*.png
echo "dist ready: $(find dist -type f | wc -l) files"
