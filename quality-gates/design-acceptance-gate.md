# Design Acceptance Gate

Gate riêng cho chất lượng thiết kế và trải nghiệm, áp dụng sau Visual QA và trước khi kết luận một module giao diện là xong. Gate này không thay thế design-gate bản 1.0. Design-gate kiểm tra thiết kế có đủ deliverable hay không. Gate này chấm điểm chất lượng thiết kế thật bằng bằng chứng chạy thật.

## Entry Criteria

- Giai đoạn thiết kế đã có Design Brief, Visual Direction, Design System, Screen Specification và quyết định Design Review.
- Giao diện đã được triển khai theo module và đã qua Visual QA.
- Có ảnh chụp thực tế ở viewport mục tiêu và danh sách lỗi phân loại Critical, High, Medium, Low.

## Required Activities

- Kiểm tra từng tiêu chí theo bảng điểm dưới đây, kèm ảnh chụp làm bằng chứng cho từng tiêu chí.
- Kiểm tra các luồng chính bằng tương tác thật, không chỉ đọc code hoặc mô tả.
- Đối chiếu ảnh chụp thực tế với thiết kế đã duyệt.

## Scoring, thang 100

- Visual Quality: 20 điểm. Giao diện đẹp, chuyên nghiệp, nhất quán, có bản sắc, không trông như trang debug.
- User Experience: 20 điểm. Dễ hiểu, dễ dùng, ít thao tác, luồng hợp lý, không bắt người dùng nhớ ID hoặc nhập tay dữ liệu đã có sẵn.
- Information Architecture: 15 điểm. Sitemap, navigation, phân cấp màn hình và gom nhóm thông tin theo cách người dùng hiểu.
- Design Consistency: 15 điểm. Mỗi module dùng chung Design System và token, không có phong cách riêng theo màn hình.
- Responsive Design: 10 điểm. Giao diện dùng được ở viewport mục tiêu, không chỉ co nhỏ giao diện desktop.
- Interaction Quality: 10 điểm. Các trạng thái hover, focus, active, disabled, loading, success, error và confirmation đầy đủ và có mục đích.
- Accessibility: 5 điểm. Chấm theo checklist WCAG 2.1 mức AA cho luồng chính: điều hướng bằng bàn phím cho mỗi chức năng, độ tương phản chữ tối thiểu 4.5 cho chữ thường và 3 cho chữ lớn, trạng thái focus nhìn thấy được, ảnh có alt text mô tả đúng, form có label gắn đúng trường, thông báo lỗi đọc được bằng trình đọc màn hình, tôn trọng tùy chọn giảm chuyển động của user. Kiểm tra bằng tương tác thật, không chỉ đọc code.
- Frontend Performance: 5 điểm. Hiển thị khởi đầu, cuộn và tương tác không giật, không chờ vô lý.

## Exit Criteria, điều kiện PASS

Tất cả các điều kiện sau phải đồng thời đạt, không được bù trừ:

- Tổng điểm tối thiểu 85 trên 100.
- Không tiêu chí nào dưới 70 trên 100 theo thang riêng của tiêu chí đó.
- Không có lỗi nghiêm trọng trong các user flow chính.
- Không có JSON thô trong giao diện người dùng thường. JSON chỉ ở khu vực Advanced hoặc Developer Settings có hướng dẫn rõ ràng.
- Không có thành phần giao diện bị vỡ trên viewport mục tiêu.
- Các chức năng quan trọng đã được kiểm tra bằng tương tác thực tế.
- Có screenshot evidence kèm ngày và phạm vi kiểm tra.

## Evidence

- Link tới file, commit, pull request, ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Nếu môi trường không có công cụ chụp ảnh thì ghi rõ giới hạn và không đánh dấu PASS cho phần thị giác.

## Approval Requirements

- Design Director có quyền từ chối nghiệm thu nếu chất lượng thị giác không đạt dù chức năng hoạt động đúng.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng cho lỗi nghiêm trọng, JSON thô ở giao diện thường, hoặc thành phần vỡ ở viewport mục tiêu.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu điểm tổng dưới 85 hoặc một tiêu chí dưới 70 thì trả lại cho UX Engineer và Frontend Engineer kèm ảnh chụp và bước tái hiện. Nếu lỗi gốc nằm ở Design System hoặc Information Architecture thì quay lại giai đoạn thiết kế, không sửa từng nút riêng lẻ để đủ điểm.
