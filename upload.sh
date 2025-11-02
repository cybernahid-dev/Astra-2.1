#!/bin/bash
# =========================================================
# 🔄 Universal Auto Upload Script for GitHub
# Author: cybernahid-dev
# Year: 2025
# Description: Automatically detects changes and pushes
#              updates to your GitHub repository via SSH.
# =========================================================

# --- 🛠 CONFIGURATION ---
REPO_URL=$(git config --get remote.origin.url)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
WATCH_DIR=$(pwd)

# --- ⚡ CHECKS ---
if [ -z "$REPO_URL" ]; then
  echo "❌ No GitHub repository linked. Use:"
  echo "   git remote add origin <repo-url>"
  exit 1
fi

if ! command -v inotifywait &>/dev/null; then
  echo "⚙️ Installing dependency: inotify-tools..."
  pkg install inotify-tools -y >/dev/null 2>&1 || sudo apt install inotify-tools -y
fi

# --- 🚀 AUTO SYNC LOOP ---
echo "🚀 Auto Upload Activated for: $WATCH_DIR"
echo "📡 Watching branch: $BRANCH"
echo "🔐 Repo: $REPO_URL"
echo "-------------------------------------------"

while true; do
  # Wait for any file changes in the current directory
  inotifywait -r -e modify,create,delete,move "$WATCH_DIR" >/dev/null 2>&1
  echo "🔄 Change detected! Uploading to GitHub..."
  git add .
  git commit -m "Auto-update: $(date +"%Y-%m-%d %H:%M:%S")" >/dev/null 2>&1
  git push -u origin "$BRANCH" >/dev/null 2>&1
  echo "✅ Sync complete at $(date +"%H:%M:%S")"
  echo "-------------------------------------------"
done
