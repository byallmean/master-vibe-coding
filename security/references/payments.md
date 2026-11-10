# Bao mat thanh toan

File reference nay thuoc version 2.2. Chi load khi code cham toi thanh toan, gia, subscription hoac webhook cua cong thanh toan nhu Stripe.

## Khong bao gio tin gia do client gui

Day la lo thanh toan so 1 trong app vibe-coded: gia lay tu request body cua client. Attacker sua request la mua duoc voi gia bat ky, ke ca gia rat nho.

BAD: tao checkout session voi gia lay thang tu request body.

GOOD: chi lay product ID tu request, tra cuu gia o server tu database hoac tu Stripe Price ID, roi moi tao checkout session voi gia do. Gia phai duoc dinh nghia o Stripe hoac o server, khong bao gio lay tu client.

## Xac minh chu ky webhook

Webhook cua Stripe phai duoc xac minh chu ky. Buoc nay can raw body, parse body thanh JSON truoc se pha vo chu ky.

Voi Express thi route webhook phai dung raw body truoc khi dung JSON parser. Voi Next.js App Router thi dung request text, khong dung request json. Sau khi xac minh chu ky moi xu ly event.

## Kiem tra trang thai subscription o server

Kiem tra trang thai subscription o server moi request duoc bao ve, dung database cua minh dong bo qua webhook lam nguon that. Khong tin gia tri cache tu luc dang nhap, flag o client, hay claim trong JWT tao tu luc cap token va khong refresh. Subscription co the bi huy, het han hoac doi goi bat ky luc nao.

## Metadata cua checkout session

Kiem tra metadata cua checkout session nhu user ID va goi dich vu duoc dat o server luc tao session, khong lay tu client. Neu metadata lay tu client thi attacker co the nhan la user khac hoac chon goi khac.
