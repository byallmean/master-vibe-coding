# Design First D5: Visual Quality Assurance

Responsible Agents: UX Engineer, QA Engineer, Design Director

Note: File này thuộc chuỗi Design First của version 2.0. Nó chạy sau UI Implementation và trước khi kết luận Phase 08 Quality Assurance hiện có. Tên file D5 không có nghĩa là Phase 09 Security Audit.

## Objective

Nghiệm thu giao diện bằng cách chạy thật và nhìn thật, không nghiệm thu chỉ bằng cách đọc code. Không được coi giao diện không bị lỗi là đồng nghĩa với giao diện đẹp.

## Input

- Giao diện đã triển khai theo module
- Thiết kế và prototype đã duyệt
- Design System
- Dữ liệu thật hoặc dữ liệu test có cấu trúc thực tế

## Execution Steps

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

## Deliverables

- UI-UX-AUDIT.md cho đợt kiểm tra, kèm danh sách lỗi phân loại Critical, High, Medium, Low
- Bộ ảnh chụp thực tế ở viewport mục tiêu, kèm ngày và phạm vi kiểm tra
- Báo cáo Visual QA Score theo Design Acceptance Gate
- Danh sách lỗi còn lại và kế hoạch sửa có thời hạn

## Quality Gate

Chỉ nghiệm thu giao diện khi vượt qua quality-gates/visual-qa-gate.md và quality-gates/design-acceptance-gate.md với tổng điểm từ 85 trên 100, không tiêu chí nào dưới 70, không lỗi nghiêm trọng trong luồng chính, không JSON thô ở giao diện người dùng thường, không thành phần vỡ ở viewport mục tiêu, chức năng quan trọng đã được kiểm tra bằng tương tác thật và có screenshot evidence. Không dùng điểm tổng để bù cho lỗi nghiêm trọng. Design Director có quyền từ chối nghiệm thu nếu chất lượng thị giác không đạt dù chức năng chạy đúng.

Viewport tối thiểu: Desktop 1440 x 900, Laptop 1280 x 800, Tablet 768 x 1024, Mobile 390 x 844. Được phép điều chỉnh theo thiết bị mục tiêu thực tế. Phải kiểm tra responsive tại kích thước phù hợp, không chỉ co nhỏ giao diện desktop.

Sử dụng công cụ browser automation hoặc screenshot testing nếu môi trường hỗ trợ. Nếu không có công cụ trực quan thì ghi rõ giới hạn. Không giả vờ đã kiểm tra giao diện thực tế.

## Failure Handling

Nếu Visual QA FAIL thì trả lại cho UX Engineer và Frontend Engineer kèm ảnh chụp và bước tái hiện, không trả lại bằng mô tả chung chung. Nếu sửa giao diện gây lỗi chức năng thì chạy lại regression test trước khi chấm lại điểm thị giác. Nếu không có công cụ chụp ảnh thì ghi rõ giới hạn và không đánh dấu PASS cho phần thị giác.

## Next Workflow

08-testing.md
