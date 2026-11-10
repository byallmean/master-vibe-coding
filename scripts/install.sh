#!/bin/bash
# Cai dat master-vibe-coding bang mot lenh.
# Cach dung: ./scripts/install.sh [muse|claude-code|cursor|codex]
# Mac dinh la muse. Script chi sao chep file, khong doi noi dung skill.
set -e

TARGET="${1:-muse}"
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="master_vibe_coding"

case "$TARGET" in
  muse)
    DEST="$HOME/workspace/custom-skills/$SKILL_NAME"
    ;;
  claude-code)
    DEST="$HOME/.claude/skills/$SKILL_NAME"
    ;;
  cursor)
    DEST="$HOME/.cursor/skills/$SKILL_NAME"
    ;;
  codex)
    DEST="$HOME/.codex/skills/$SKILL_NAME"
    ;;
  *)
    echo "Target khong hop le: $TARGET"
    echo "Dung mot trong: muse, claude-code, cursor, codex"
    exit 2
    ;;
esac

if [ "$DEST" = "$SCRIPT_DIR" ]; then
  echo "Thu muc dich trung thu muc nguon, bo qua buoc sao chep."
else
  mkdir -p "$(dirname "$DEST")"
  rm -rf "$DEST"
  cp -r "$SCRIPT_DIR" "$DEST"
fi

echo "Da cai skill vao: $DEST"
echo "Kiem tra bang validator..."
cd "$DEST" && python3 scripts/validate-skill.py
echo "Cai dat xong. Mo lai phien lam viec va goi skill bang ten master-vibe-coding."
