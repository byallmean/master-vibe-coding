# Simulation: Ung dung dat lich hen dich vu

Muc dich cua file nay la chung minh skill co the dieu phoi tu y tuong den handover, khong phai tuyen bo ung dung mo phong la san pham that.

Phan mo phong va phan bang chung that duoc tach ro trong file nay.

## Y tuong ban dau

Khach hang dat lich hen dich vu, nhan vien xep lich, quan tri vien theo doi lich.

## Phase 01 den Phase 05: Mo phong

- Product Manager chot MVP la dang nhap, dat lich, chong trung lich va thong bao. Thanh toan that bi loai khoi MVP.
- Business Analyst viet user story cho dat lich va quy tac chong trung lich.
- Solution Architect chon kien truc module Auth, Booking, Notification va viet ADR cho viec tach module.
- UI/UX Designer ve luong dat lich va cac trang thai rong, dang tai, loi va thanh cong.

Day la phan mo phong thiet ke, chua co code that cho Auth va Notification.

## Phase 06 den Phase 07: Mo phong va bang chung that mot phan

- Module Booking co code that nho trong examples/simulation-app/booking.py, voi ham can_book kiem tra trung lich va khoang thoi gian khong hop le.
- Module Auth va Notification chi o muc thiet ke mo phong, chua co code that.

## Phase 08: Bang chung test that

Test that chay bang unittest cho module Booking, ket qua that thu duoc ngay 2026-11-03:

- test_empty_calendar: ok
- test_invalid_range: ok
- test_no_overlap: ok
- test_overlap: ok
- test_partial_overlap: ok
- Ran 5 tests, ket qua OK

Day la bang chung that duy nhat trong mo phong nay. No khong chung minh toan bo ung dung hoat dong.

## Phase 09 den Phase 11: Mo phong

- Security Engineer mo phong kiem tra xac thuc va phan quyen, chua co audit that.
- Performance Engineer mo phong do API va database, chua co so lieu that.
- DevOps/SRE Engineer mo phong quy trinh deploy co health check, smoke test va rollback, chua co deploy that.

## Phase 12: Handover mo phong

- Handover mo phong nam trong examples/simulation-project, gom PROJECT_CONTEXT, PROJECT_STATUS, CURRENT_TASK, DECISIONS, TECHNICAL_DEBT, BLOCKERS, NEXT_STEPS va CHANGELOG.
- Handover ghi ro Auth va Notification chua co code that, va chi Booking co test that.
- Handover khong chua secret.

## Ket luan mo phong

Skill da dieu phoi duoc chuoi 12 giai doan o muc vi du, voi mot bang chung test that cho mot module nho.

De bien mo phong thanh du an that, can bat dau lai tu Phase 04 cho Auth va Notification, viet code that, test that, audit that va deploy that theo dung quality gate.
