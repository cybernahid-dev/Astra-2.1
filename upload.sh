#!/bin/bash
# ============================================================
#  Astra 2.1 Auto Upload Script
#  Created by cybernahid-dev
# ============================================================

echo "🚀 Starting Astra 2.1 Upload Process..."

# Check internet connection
if ! ping -c 1 github.com &>/dev/null; then
  echo "❌ No internet connection! Please connect and try again."
  exit 1
fi

# Go to project directory
cd "$(dirname "$0")" || exit

# Check if .git exists
if [ ! -d ".git" ]; then
  echo "🧩 Git not initialized. Initializing now..."
  git init
  git branch -M main
fi

# Check user identity
if ! git config user.name >/dev/null; then
  git config --global user.name "cybernahid-dev"
  git config --global user.email "githubnahid@gmail.com"
  echo "✅ Git user configured."
fi

# Add all files
git add .

# Commit with timestamp
commit_msg="Auto update - $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_msg"

# Check remote URL
if ! git remote | grep -q origin; then
  echo "⚙️ Adding remote origin..."
  git remote add origin https://github.com/cybernahid-dev/Astra-2.1.git
fi

# Push to GitHub
echo "⬆️ Uploading files to GitHub..."
git push -u origin main

echo "✅ Upload completed successfully!"
