# Visual QA Gate

Gate cho quy trình kiểm tra giao diện bằng cách chạy thật và nhìn thật, áp dụng sau UI Implementation và trước khi kết luận Phase 08 Quality Assurance.

## Entry Criteria

- Giao diện đã vượt qua ui-implementation-gate cho module liên quan.
- Ứng dụng chạy được và có dữ liệu thật hoặc dữ liệu test có cấu trúc thực tế.
- Thiết kế và prototype đã duyệt sẵn có để đối chiếu.

## Required Activities

Thực hiện đủ 17 bước sau, theo đúng thứ tự, và ghi bằng chứng cho từng bước:

1. Khởi chạy ứng dụng.
2. Mở bằng trình duyệt.
3. Truy cập các màn hình chính.
4. Chụp screenshot.
5. Kiểm tra visual hierarchy.
6. Kiểm tra typography.
7. Kiểm tra spacing.
8. Kiểm tra alignment.
9. Kiểm tra màu sắc.
10. Kiểm tra component consistency.
11. Kiểm tra responsive.
12. Kiểm tra các trạng thái tương tác.
13. Kiểm tra dữ liệu thật hoặc dữ liệu test có cấu trúc thực tế.
14. So sánh với thiết kế đã duyệt.
15. Ghi nhận lỗi.
16. Sửa lỗi.
17. Chụp lại screenshot và kiểm tra lại.

Viewport tối thiểu: Desktop 1440 x 900, Laptop 1280 x 800, Tablet 768 x 1024, Mobile 390 x 844. Được phép điều chỉnh theo thiết bị mục tiêu thực tế. Phải kiểm tra responsive tại kích thước phù hợp, không chỉ co nhỏ giao diện desktop.

Sử dụng công cụ browser automation hoặc screenshot testing nếu môi trường hỗ trợ. Nếu không có công cụ trực quan thì ghi rõ giới hạn. Không giả vờ đã kiểm tra giao diện thực tế.

## Deliverables

- UI-UX-AUDIT.md cho đợt kiểm tra
- Bộ ảnh chụp thực tế ở viewport mục tiêu
- Báo cáo Visual QA Score theo design-acceptance-gate
- Danh sách lỗi còn lại và kế hoạch sửa có thời hạn

## Exit Criteria

- Tất cả màn hình chính đã có ảnh chụp thực tế ở viewport mục tiêu.
- Không có thành phần vỡ ở viewport mục tiêu.
- Không có JSON thô ở giao diện người dùng thường.
- Các luồng chính đã được kiểm tra bằng tương tác thật.
- Lỗi Critical và High đã được sửa hoặc có kế hoạch sửa có thời hạn được Design Director chấp nhận.

## Evidence

- Link tới file, commit, pull request, ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Ảnh chụp phải ghi rõ màn hình, viewport, ngày và bản build được kiểm tra.

## Approval Requirements

- Design Director duyệt kết quả Visual QA.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện kết luận phần giao diện của module.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát, không áp dụng cho thành phần vỡ ở viewport mục tiêu hoặc JSON thô.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Trả lại cho UX Engineer và Frontend Engineer kèm ảnh chụp và bước tái hiện. Sau khi sửa thì chạy lại regression test rồi chụp lại và chấm lại, không chấp nhận sửa bằng mô tả.
