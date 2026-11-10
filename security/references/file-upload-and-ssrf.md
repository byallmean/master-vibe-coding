# File upload va SSRF

Chi load file nay khi du an co tinh nang upload file hoac khi server goi URL do user nhap. Neu du an khong co hai tinh nang do thi bo qua file nay va ghi ro ly do bo.

## File upload

BAD: chi kiem tra phan mo rong cua ten file, luu file vao thu muc web co the truy cap truc tiep, khong gioi han dung luong, khong quet noi dung.

GOOD: kiem tra loai file bang noi dung that cua file, khong tin phan mo rong. Gioi han dung luong toi da va tu choi file vuot gioi han. Quet noi dung truoc khi luu. Luu file ngoai thu muc web, khong cho chay file da upload nhu code. Dat ten file moi o server, khong dung ten file do user gui. Kiem tra quyen so huu moi khi user truy cap file, khong cho doan duong dan de doc file cua user khac.

## SSRF

BAD: server goi thang URL do user nhap ma khong kiem tra, ke ca URL tro vao dich vu noi bo nhu metadata cua cloud, localhost hay mang LAN.

GOOD: chi goi URL nam trong allowlist domain va giao thuc da khai bao. Chan dia chi IP noi bo, localhost va dai IP dac biet truoc khi goi. Gioi han thoi gian cho va kich thuoc phan hoi. Khong tra lai noi dung phan hoi noi bo cho user khi khong can thiet.

## Kiem tra

- Upload file co phan mo rong gia mao thi bi tu choi.
- Upload file vuot dung luong toi da thi bi tu choi.
- User khong doc duoc file cua user khac bang cach sua duong dan.
- Server tu choi URL tro vao localhost, dai IP noi bo va metadata cua cloud.
