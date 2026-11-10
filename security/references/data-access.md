# Truy cap du lieu va validation

File reference nay thuoc version 2.2. Chi load khi code cham toi query database, ORM, API route, webhook hoac form nhan input tu ben ngoai.

## SQL injection

Luon dung query co parameter hoac method cua ORM. Khong bao gio noi chuoi user input vao cau SQL.

BAD: query noi thang user ID vao chuoi SQL.

GOOD: query co parameter, gia tri user ID truyen rieng, khong nam trong chuoi SQL.

## ORM van co the bi injection

Ngay ca khi dung ORM, injection van xay ra neu dua object chua validate thang vao dieu kien loc. Attacker co the gui object co operator nhu contains de khop moi ban ghi.

BAD: dua thang request body lam dieu kien where cho ORM.

GOOD: validate bang schema runtime truoc, chi lay field da validate roi moi dua vao where.

Khong bao gio dung raw query khong an toan voi input cua user. Raw query co parameter thi duoc, raw query noi chuoi thi khong.

## Validate moi input o ranh gioi he thong

Validate moi input tu ben ngoai o ranh gioi he thong bang schema runtime nhu Zod, Yup hoac Joi: API route handler, Server Action, webhook handler, form submit, URL parameter va query string.

Khong dua vao TypeScript type mot minh. Type chi ton tai luc bien dich, khong ton tai luc chay. Attacker gui request sai dinh dang se vuot qua moi kiem tra cua TypeScript.

## Mass assignment

Khong spread request body thang vao thao tac database. Attacker co the them field bat ngo nhu is admin hay credits.

BAD: update user voi toan bo request body lam du lieu.

GOOD: chi lay cac field da validate va nam trong allowlist nhu ten va email roi moi update.
