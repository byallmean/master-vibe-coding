# Performance Gate

Gate mới của version 3.0, tách ra từ Security Gate. Gate này chấm hiệu năng bằng số liệu thật, theo mẫu của Design Acceptance Gate. Không đánh dấu PASS chỉ bằng nhận xét chạy mượt.

## Entry Criteria

- Testing Gate đã vượt qua.
- Ngân sách hiệu năng của dự án đã được định trước và ghi trong Performance Report.
- Dữ liệu test có kích thước gần thực tế và cấu hình test đã ghi rõ.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm số đo thật cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí và ngân sách mặc định

Ngân sách dưới đây là mặc định khi Product Owner chưa đặt số khác. Product Owner có thể điều chỉnh từng số nhưng phải ghi rõ số mới và lý do vào Performance Report.

- LCP tối đa 2.5 giây trên luồng chính, đo ở viewport mục tiêu.
- Trang chính hiển thị nội dung đầu tiên trong tối đa 1.5 giây.
- API p95 tối đa 500 mili giây cho endpoint thường, đo với dữ liệu gần thực tế.
- Bundle JavaScript tối đa 300 KB sau khi nén cho trang chính.
- Query database chậm nhất trong luồng chính tối đa 200 mili giây, có chỉ mục phù hợp.
- Không có nút thắt nào làm luồng chính chậm gấp đôi ngân sách.

## Deliverables

- Performance Report kèm số đo thật cho từng tầng
- Danh sách nút thắt có mức độ ưu tiên

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt, hoặc đã có số điều chỉnh đã phê duyệt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Số đo phải là kết quả chạy thật trong cùng điều kiện trước và sau khi tối ưu, kèm kích thước dữ liệu và cấu hình test.

## Approval Requirements

- Product Owner phê duyệt ngân sách hiệu năng và kết quả đo.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát, kèm thời hạn cải thiện và người chịu trách nhiệm. CONDITIONAL PASS không được áp dụng khi LCP vượt ngân sách trên luồng chính hoặc khi API p95 vượt ngân sách gấp đôi.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu không đạt ngân sách thì trả lại cho Backend Engineer và Frontend Engineer kèm số đo thật. Nếu tối ưu không cải thiện thì chạy workflows/08b-systematic-debugging.md.
