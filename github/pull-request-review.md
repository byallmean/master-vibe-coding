# GitHub: Review pull request

Review hai tang theo workflows/07c-code-review.md, tang 1 truoc roi moi den tang 2, khong tron hai tang vao nhau.

Tang 1 Spec Compliance:

- Kiem tra PR co mo ta ro rang, lien ket issue va test da chay
- Kiem tra tung acceptance criteria co duoc dap ung hay khong
- Kiem tra code co dung kien truc, xu ly loi va quyen hay khong
- Kiem tra migration co rollback va tai lieu co cap nhat hay khong

Tang 2 Code Quality:

- Kiem tra code co de doc khong, co trung lap khong, co code chet khong, co dung quy uoc cua du an khong
- Kiem tra secret trong code hoac log, quyen so huu resource, validation dau vao va field ngoai allowlist

Quy tac chung:

- Khong merge PR co rui ro cao khi chua co phe duyet phu hop
- Ghi nhan xet cu the theo dong code, khong chi viet chung chung
- Reviewer khong duoc la agent vua viet code do trong cung mot phien neu co the tach agent. Neu bat buoc cung agent thi chi duoc Comment, khong duoc tu Approve

Quy tac an toan:

- Khong xoa repository, xoa branch, force push, ghi de du lieu, xoa migration, thay doi production database hoac secret khi chua co phe duyet.
- Cac thao tac co nguy co mat du lieu hoac anh huong production phai duoc nguoi dung phe duyet truoc.
