# Bao mat mobile

File reference nay thuoc version 2.2. Chi load khi du an co app mobile React Native, Expo hoac tuong duong.

## Luu token dung cho

Luu token trong secure storage cua he dieu hanh, khong luu trong AsyncStorage. AsyncStorage khong ma hoa va bat ky code nao cung doc duoc.

## API key khong nam trong bundle

API key trong bundle JavaScript cua app mobile thi ai cung trich xuat duoc. Moi call toi AI hay dich vu tra phi phai di qua backend cua minh. Client chi gui noi dung toi server, server goi AI API bang key o server.

Bien moi truong co tien to EXPO_PUBLIC se bi dua thang vao bundle luc build. Khong bao gio dat secret vao bien co tien to do.

## Deep link

Xac thuc deep link truoc khi xu ly. Deep link khong xac thuc co the bi dung de mo man hinh nhay cam hoac truyen tham so doc hai vao app. Chi chap nhan deep link tu domain cua minh va validate moi tham so.

## Sinh trac hoc

Sinh trac hoc yeu chi mo khoa thiet bi, khong thay cho xac thuc server. Sau khi mo khoa bang sinh trac hoc van phai co session hop le o server moi duoc truy cap du lieu.
