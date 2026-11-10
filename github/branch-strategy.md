# GitHub: Chien luoc branch va bao ve branch

- Branch chinh: main la production, develop la tich hop neu du an dung
- Branch tinh nang: feature/ten-tinh-nang, sua loi: fix/ten-loi, khan cap: hotfix/ten-loi
- Khong commit truc tiep len main khi da co bao ve branch
- Yeu cau pull request, review va CI chay dat truoc khi merge
- Khong force push len branch dung chung, khong xoa branch khi chua xac nhan

## Git worktree

- Moi thay doi lon lam tren worktree rieng, khong lam chung worktree voi thay doi khac. Tao worktree moi tu main hoac develop, lam xong thi tao pull request tu worktree do, merge xong thi xoa worktree.
- Truoc khi viet code trong worktree thi chay setup va xac minh baseline sach: build dat, test chinh do, health check tot. Ghi baseline vao PROJECT_STATUS.md.
- Khong dung chung mot worktree cho hai thay doi khac nhau. Khong commit thay doi cua story nay vao worktree cua story khac.

Quy tac an toan:

- Khong xoa repository, xoa branch, force push, ghi de du lieu, xoa migration, thay doi production database hoac secret khi chua co phe duyet.
- Cac thao tac co nguy co mat du lieu hoac anh huong production phai duoc nguoi dung phe duyet truoc.
