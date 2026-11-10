# Production Acceptance Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Deployment Gate đã vượt qua.
- Operations Runbook, Monitoring Dashboard Specification, Backup và Recovery Plan bản nháp đã có.
- Ứng dụng đã chạy production ít nhất một chu kỳ kiểm tra, không phải vừa deploy xong.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Monitoring đủ. Mỗi dịch vụ chính có metric sức khỏe, lỗi và tài nguyên. Dashboard hiển thị được trạng thái hiện tại, không phải dashboard trống.
- Alerting đủ. Cảnh báo có ngưỡng rõ ràng, có người nhận và có cách xử lý. Cảnh báo phải được test thử, không chỉ cấu hình xong rồi để đó.
- Backup chạy thật. Backup chạy theo lịch, lưu trữ đủ bản, và đã khôi phục thử thành công ít nhất một lần. Backup chưa từng khôi phục thử thì FAIL cho mục backup.
- Recovery Plan viết đầy đủ. Các bước khôi phục sau sự cố đã viết, có người chịu trách nhiệm, có thời gian khôi phục mục tiêu, và đã diễn tập hoặc đã mô phỏng ít nhất một lần.
- Runbook xử lý sự cố. Runbook có các sự cố thường gặp, cách chẩn đoán, cách khắc phục và cách leo thang. Runbook không chứa secret.
- Log đủ dùng. Log có request id, mức độ, thời gian, không chứa secret hay dữ liệu nhạy cảm, và lưu trữ đủ lâu để truy vết sự cố.

## Deliverables

- Operations Runbook, Monitoring Dashboard Specification, Backup và Recovery Plan

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Bằng chứng khôi phục thử phải là log khôi phục thật, ghi rõ dữ liệu nào, khôi phục lúc nào và kết quả ra sao.

## Approval Requirements

- Product Owner phê duyệt production readiness.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện gọi là sẵn sàng production.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi backup chưa từng khôi phục thử, khi chưa có alerting, hoặc khi chưa có runbook xử lý sự cố.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu backup chưa từng khôi phục thử thì FAIL cho mục backup, không được gọi là sẵn sàng production. Chạy khôi phục thử rồi mới đánh dấu lại.
