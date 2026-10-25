#!/usr/bin/env bash
# Downloads every generated still and clip listed in manifest.json into assets/images and assets/video,
# then builds the five ad videos and the landing explainer with ffmpeg (see build-videos.sh).
# Run this on your own machine (the cloud sandbox cannot reach the Higgsfield CDN).
set -euo pipefail
cd "$(dirname "$0")"
command -v jq >/dev/null || { echo "install jq first (brew install jq)"; exit 1; }
mkdir -p images video
jq -r '.images|to_entries[]|"\(.key) \(.value)"' manifest.json | while read -r name url; do
  [ -s "images/$name.png" ] || curl -sSL -o "images/$name.png" "$url" && echo "image  $name"
done
jq -r '.video_clips|to_entries[]|"\(.key) \(.value)"' manifest.json | while read -r name url; do
  [ -s "video/$name.mp4" ] || curl -sSL -o "video/$name.mp4" "$url" && echo "clip   $name"
done
echo "done. now run: bash build-videos.sh"
mkdir -p video/ugc
jq -r '.ugc_videos_lipsync_9x16|to_entries[]|select(.value|startswith("http"))|"\(.key|split(" ")[0]) \(.value)"' manifest.json | while read -r name url; do
  [ -s "video/ugc/$name.mp4" ] || curl -sSL -o "video/ugc/$name.mp4" "$url" && echo "ugc    $name"
done
