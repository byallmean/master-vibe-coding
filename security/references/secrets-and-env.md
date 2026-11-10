# Secrets va bien moi truong

File reference nay thuoc version 2.2. Chi load khi code cham toi secret, API key, bien moi truong hoac cau hinh deploy. Ap dung cho stack tu host: bien moi truong, secret manager, Docker secret, khong chi cho Next.js hay Vercel.

## Khong bao gio hardcode secret

Khong ghi API key, mat khau, chuoi ket noi database, private key hay chung chi vao code. Secret chi nam trong bien moi truong, secret manager hoac Docker secret.

BAD: chuoi ket noi co mat khau ghi thang trong code, hoac API key ghi thang trong file cau hinh commit len git.

GOOD: doc secret tu bien moi truong luc chay, file cau hinh chi chua ten bien, khong chua gia tri.

## Secret tung bi commit thi coi nhu da lo

Xoa file khoi commit hien tai la khong du, vi lich su git van giu secret. Khi phat hien secret trong lich su git thi rotate secret do ngay, roi moi xoa khoi lich su. Quet bang lenh gitleaks detect truoc moi lan deploy.

## Bien moi truong client-side

Cac tien to sau day dua bien moi truong vao bundle client luc build, ai cung doc duoc:

- Next.js: NEXT_PUBLIC
- Vite: VITE
- Expo va React Native: EXPO_PUBLIC
- Create React App: REACT_APP

Chi duoc dua ra client: Stripe publishable key, Supabase anon key, Firebase client config, public analytics ID.

Khong bao gio dua ra client: service role key, Stripe secret key, chuoi ket noi database, API key cua ben thu ba, JWT signing secret, OAuth client secret.

## File env va gitignore

File env, env local va moi file chua secret phai co trong gitignore truoc commit dau tien. File env example chi chua gia tri placeholder, khong chua key that. Kiem tra bang cach liet ke file da track trong git va tim file env.

## Tach secret theo moi truong

Production, staging va dev dung secret khac nhau. Key production khong dung cho moi truong preview hay dev. Preview deployment thuong ai co link cung mo duoc, nen khong duoc dung key production o do.
