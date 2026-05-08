#!/usr/bin/env bash
# ZTF PMO Hub — refresh data and deploy to GitHub Pages
# Usage: bash ~/ztf-pmo-hub/deploy.sh
set -e

SHEET_ID="1GXWo3up9CokeCHNQPmvLbmzXY1eCmSwW979ZB_EMrbs"
ACCOUNT="mosheera.salah@zalando.de"
DIR="$(cd "$(dirname "$0")" && pwd)"
UPDATED=$(date "+%b %d, %Y %H:%M")

echo "🔄 Fetching data from Google Sheets..."
TOKEN=$(gcloud auth print-access-token --account=$ACCOUNT)
curl -s "https://sheets.googleapis.com/v4/spreadsheets/$SHEET_ID/values/A2:Z200?majorDimension=ROWS" \
  -H "Authorization: Bearer $TOKEN" > /tmp/sheet_raw.json

echo "⚙️  Generating dashboard..."
python3 "$DIR/generate.py" "$UPDATED"

echo "📦 Committing and pushing..."
cd "$DIR"
git add index.html
git commit -m "chore: refresh data — $UPDATED"
git push origin main

echo ""
echo "✅ Live at: https://mosheera29-crypto.github.io/ztf-pmo-hub/"
