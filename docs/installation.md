# Cai dat master-vibe-coding

## Cai tu GitHub

Repo cong khai: https://github.com/byallmean/master-vibe-coding

Clone repo ve roi chay script cai dat, script tu sao chep skill vao dung vi tri cua tung cong cu va tu chay validator de kiem tra.

- Muse:

git clone https://github.com/byallmean/master-vibe-coding.git ~/workspace/custom-skills/master_vibe_coding

- Claude Code:

git clone https://github.com/byallmean/master-vibe-coding.git ~/.claude/skills/master_vibe_coding

Khi co ban moi thi vao thu muc skill va chay git pull de cap nhat.

## Cai bang mot lenh

Tu trong thu muc skill, chay script cai dat voi target can cai. Script tu sao chep toan bo thu muc skill vao dung vi tri cua tung cong cu, roi tu chay validator de kiem tra.

- Muse, mac dinh:

bash scripts/install.sh muse

- Claude Code:

bash scripts/install.sh claude-code

- Cursor:

bash scripts/install.sh cursor

- Codex:

bash scripts/install.sh codex

Neu khong truyen target thi script cai cho Muse. Sau khi cai xong thi mo lai phien lam viec va goi skill bang ten master-vibe-coding khi bat dau du an.

## Vi tri cai dat

- Muse: ~/workspace/custom-skills/master_vibe_coding
- Claude Code: ~/.claude/skills/master_vibe_coding
- Cursor: ~/.cursor/skills/master_vibe_coding
- Codex: ~/.codex/skills/master_vibe_coding

## Cai bang tay

Neu khong dung script thi sao chep toan bo thu muc skill vao vi tri tren sao cho file SKILL.md va skill.yaml nam ngay trong thu muc do.

- Neu phien ban Claude Code cua ban yeu cau frontmatter trong SKILL.md thi them frontmatter name va description o dau file, giu nguyen toan bo noi dung ben duoi.
- Kiem tra lai rang cac duong dan tuong doi trong skill van dung sau khi sao chep.
- Neu cong cu khong ho tro subagent thi chay cac chuyen gia tuan tu theo thu tu phu thuoc va ghi ro lua chon nay trong PROJECT_STATUS.md.

## Luu y chung

- Khong sao chep secret vao bat ky file skill nao.
- Sau khi cai dat, chay validator truoc khi dung skill cho du an that.
