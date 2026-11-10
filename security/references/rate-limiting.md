# Rate limiting va chong lam dung

File reference nay thuoc version 2.2. Chi load khi code cham toi endpoint auth, AI call, gui email hay SMS, xu ly file, webhook hoac bat ky endpoint nao nhan input tu ben ngoai o quy mo lon.

## Endpoint nao can rate limit

AI assistant hau nhu khong bao gio tu them rate limit, nen phai kiem tra rieng tung endpoint:

- Auth: dang nhap, dang ky, reset mat khau, xac minh OTP, magic link. Khong co limit thi attacker do mat khau hoac liet ke tai khoan.
- AI call: moi endpoint goi AI. Mot user co the dot het ngan sach thang trong vai phut.
- Gui email hay SMS: khong co limit thi attacker dung app lam spam relay.
- Xu ly file: upload, resize, convert. Tac vu nang CPU ma khong co limit thi bi tan cong tu choi dich vu.
- Webhook va endpoint nhan input ben ngoai o quy mo lon.

## Ket hop limit theo IP va theo user

Chi limit theo IP thi attacker doi IP de vuot qua. Chi limit theo user thi attacker tao tai khoan moi de vuot qua. Dung ca hai cung luc.

## Khong luu counter o noi user tu reset duoc

Neu counter rate limit nam o bang public ma user doc ghi duoc qua API thi user tu reset counter cua minh. Dung Redis, bang o schema rieng khong mo qua API, limit o edge hoac API gateway, hoac bo nho trong bo cho app chay mot server.

Voi stack tu host: dung Traefik rate limit middleware hoac Redis. Traefik co the gioi han theo IP ngay o cong vao, Redis dung cho limit theo user va cho app chay nhieu server.

## Bao ve chi phi

Dat canh bao chi phi o moi cloud provider. Dat spending cap cung o moi AI provider. Dung quota theo user co gioi han cung, khong chi canh bao mem. Theo doi mau su dung bat thuong nhu tang dot ngot hoac request vao gio la.
