# Kiem soat truy cap database

File reference nay thuoc version 2.2. Chi load khi code cham toi database, truy van, migration hoac luu tru file. Ap dung cho Postgres truc tiep, SQLite va Supabase RLS lam vi du.

## Nguyen tac chung

Kiem tra dang nhap la chua du. Moi truy van phai kiem tra quyen so huu resource: user chi duoc doc va sua dong cua minh. Khong co bang nao mo cho moi user doc het.

## Postgres truc tiep va SQLite

Khi app tu quan ly ket noi database thi lop truy cap du lieu phai loc theo chu so huu trong moi query, khong chi loc o lop giao dien.

BAD: lay toan bo bang roi loc o frontend, hoac query theo id do client gui ma khong kiem tra id do thuoc ve user dang goi.

GOOD: moi query deu co dieu kien chu so huu, vi du chi lay dong co owner bang user hien tai, va chi cap nhat dong thoa ca id va owner.

## Supabase Row Level Security, lam vi du

Bat RLS cho moi bang. Bang tao bang SQL Editor hoac migration mac dinh tat RLS, ai co anon key cung doc va ghi duoc.

Khong bao gio dung chinh sach cho phep tat ca nhu USING true hoac chi kiem tra da dang nhap. Chinh sach phai gioi han theo chu so huu, vi du chi cho doc dong co user id bang user dang goi.

Insert va Update phai co WITH CHECK, neu khong user co the doi chu so huu cua dong sang user khac.

## Field nhay cam tren bang user sua duoc

Neu bang profiles cho user tu sua dong cua minh thi user co the tu dat is admin thanh true, credits thanh so lon hoac subscription tier thanh goi cao nhat. Cach sua: tach field nhay cam sang bang rieng khong mo qua API, hoac chi cap quyen update cho tung cot duoc phep nhu display name va avatar.

## Bang phu va bucket file

Bang trung gian, bang audit log va bang metadata thuong bi quen, du bang chinh da co chinh sach. Moi bang mo qua API deu can chinh sach rieng. Bucket luu tru file cung can chinh sach rieng, gioi han upload vao thu muc cua chinh user do.

## Ham SECURITY DEFINER

Ham SECURITY DEFINER bo qua RLS. Chi dat ham do trong schema rieng, dat search path rong, va validate moi dau vao trong ham.
