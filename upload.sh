#!/bin/bash
# =========================================
# 🚀 Astra 2.1 Secure Upload Script (SSH)
# Author: cybernahid-dev
# License: MIT
# Year: 2025
# =========================================

echo "🌌 Starting Astra 2.1 Secure Upload via SSH..."

# === Basic Git Config ===
git config --global user.name "cybernahid-dev"
git config --global user.email "youremail@example.com"   # তোমার GitHub ইমেইল দাও

# === Initialize Git if needed ===
if [ ! -d ".git" ]; then
    echo "🌀 Initializing new Git repository..."
    git init
fi

# === Set main branch ===
git branch -M main

# === Ensure SSH remote is set ===
if git remote | grep -q "origin"; then
    echo "🔄 Updating remote origin..."
    git remote set-url origin git@github.com:cybernahid-dev/Astra-2.1.git
else
    echo "🌐 Adding remote origin..."
    git remote add origin git@github.com:cybernahid-dev/Astra-2.1.git
fi

# === Add & Commit Changes ===
echo "📦 Adding and committing all changes..."
git add .
git commit -m "Auto upload — $(date '+%Y-%m-%d %H:%M:%S')" || echo "✅ No new changes to commit."

# === Push to GitHub ===
echo "🚀 Pushing to GitHub (SSH method)..."
git push -u origin main

echo "✅ Upload complete! Astra 2.1 is now synced to GitHub."
