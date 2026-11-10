# Xac thuc va phan quyen

File reference nay thuoc version 2.2. Chi load khi code cham toi dang nhap, session, JWT, SSO, OIDC hoac phan quyen. Ap dung cho Authentik OIDC, Traefik forward-auth va JWT tu quan ly.

## JWT

Dung verify chu ky, khong bao gio dung decode mot minh. Decode chi doc payload ma khong kiem tra chu ky, attacker tu tao payload nao cung duoc.

Tu choi thuat toan none. Mot so thu vien chap nhan token khong ky neu thuat toan la none. Qua trinh verify phai tu choi truong hop nay.

Kiem tra issuer, audience va han dung, khong chi kiem tra chu ky.

## Middleware va forward-auth khong du lam lop auth duy nhat

Middleware chay o edge tien cho viec kiem tra auth, nhung khong phai lop bao mat dang tin duy nhat. Traefik forward-auth cung vay: no la cong bao ve, khong thay cho viec verify o handler.

Luon verify lai auth o route handler, o server action va o tang truy cap du lieu. Middleware chi la lop tien ich, khong phai buc tuong duy nhat giua attacker va du lieu.

## Server Action va API route la endpoint cong khai

Server Action bien dich thanh endpoint POST cong khai, ai cung goi duoc bang curl. Moi Server Action can ba thu o dau: validate dau vao bang schema runtime, xac thuc user da dang nhap, phan quyen bang cach kiem tra user so huu resource do. Tuong tu, moi API route handler deu la endpoint cong khai va can xac thuc o dau moi handler.

## Khong lo du lieu nhay cam ve client

Khong bao gio tra toan bo object database ve component client. Object co the chua mat khau da hash, internal ID hoac co admin. Chi select field client can, vi du ten va avatar.

## Session va token storage

Luu token trong cookie HttpOnly kem Secure va SameSite Lax, khong luu trong localStorage. LocalStorage bat ky JavaScript nao tren trang cung doc duoc, mot lo XSS la lo het token. Cookie HttpOnly thi JavaScript khong doc duoc va trinh duyet tu gui kem request.

## Authentik OIDC va SSO

Khi dung Authentik lam IdP thi app khong tu luu mat khau user. App nhan token tu Authentik, verify chu ky va issuer, roi moi tao session cua minh. Khong tin claim role trong token neu claim do khong duoc refresh, kiem tra quyen o server moi request quan trong.

## MFA

Bat MFA cho tai khoan admin va tai khoan co quyen sua du lieu nhay cam. MFA dung TOTP hoac khoa bao mat, khong dung SMS lam lop duy nhat vi SMS de bi danh cap so. Khi dung Authentik thi bat MFA o Authentik, khong tu viet lai logic MFA trong app. Luu ma khoi phuc o noi an toan va co quy trinh cap lai khi user mat thiet bi.

## Quan ly session

Session phai co han dung va tu het han khi khong hoat dong. Cho user xem danh sach session dang mo va thu hoi session tu xa khi doi mat khau hoac khi nghi ngo bi xam nhap. Khi user doi mat khau thi thu hoi tat ca session cu. Khi cap lai token thi xoay refresh token, token cu khong dung duoc nua. Khong de session ton tai mai mai va khong luu session trong localStorage.
