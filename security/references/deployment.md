# Bao mat deploy

File reference nay thuoc version 2.2. Chi load khi deploy, cau hinh reverse proxy, Traefik, Docker hoac moi truong production.

## Tat debug va source map o production

Debug mode o production thuong lo stack trace, bien moi truong va duong dan noi bo. Tat debug va tat che do log chi tiet o production.

Source map o production lo toan bo source code cho ai mo DevTools. Tat source map o production.

## Thu muc git khong duoc truy cap tu ben ngoai

Kiem tra duong dan git cua site khong tra ve noi dung. Neu ai cung doc duoc lich su commit thi toan bo source code va moi secret tung commit deu lo. Chan truy cap thu muc git o reverse proxy.

## Tach moi truong

Production, preview va dev dung key, database va khoa thanh toan khac nhau. Preview deployment khong bao gio dung key production vi preview thuong ai co link cung mo duoc.

## Security header

Dat cac header sau cho moi response: Content Security Policy bat dau chat che roi moi no long khi can, Strict Transport Security, X Frame Options DENY, X Content Type Options nosniff, Referrer Policy strict origin when cross origin, Permissions Policy tat camera, microphone va geolocation khi khong can.

Voi Traefik thi dat header o middleware va gan vao router, khong phu thuoc vao tung app tu dat.

## CORS

Khong bao gio dung Access Control Allow Origin sao cho endpoint da xac thuc. Chi whitelist domain cua minh. Khi bat Access Control Allow Credentials thi phai kem origin cu the, khong dung wildcard.

## Kiem tra truoc khi ship

Chay gitleaks de quet secret trong lich su git, xac minh file env da co trong gitignore, xac nhan debug da tat, trang loi khong lo stack trace, CORS chi cho domain cua minh.
