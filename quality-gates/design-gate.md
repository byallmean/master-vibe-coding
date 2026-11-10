# Design Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate. Gate này kiểm tra thiết kế có đủ deliverable và có đúng nội dung hay không. Chất lượng thị giác thật được chấm ở Design Acceptance Gate sau Visual QA.

## Entry Criteria

- Architecture Gate đã vượt qua.
- Chuỗi Design First D1, D2, D3 đã chạy xong và có quyết định Design Review.
- User Journey và API Specification đã có.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Mỗi màn hình chính đều có thiết kế. Danh sách màn hình chính đối chiếu với user journey, không thiếu màn hình nào của luồng chính.
- Mỗi màn hình có đủ trạng thái. Trạng thái rỗng, trạng thái lỗi, trạng thái thành công và trạng thái đang tải đều có thiết kế, không chỉ có trạng thái bình thường.
- Thiết kế khớp user journey. Mỗi bước trong luồng chính đều có màn hình tương ứng, không có bước thừa và không có bước thiếu.
- Design Tokens đầy đủ. Token dùng chung cho màu, typography, spacing và radius, không để màn hình tự định nghĩa giá trị riêng.
- Component Library ánh xạ 1-1 với Design System. Không có component trùng lặp vô nghĩa, không có component dùng một lần rồi bỏ.
- Thiết kế khớp API. Mỗi dữ liệu màn hình hiển thị đều có trong API Specification, không có field thiết kế mà API không trả được. Nếu không khớp thì quay lại Phase 04, không tự sửa API trong lúc vẽ giao diện.
- Quyết định Design Review đã có. Design Director, Product Designer và Product Manager đã duyệt bằng văn bản.

## Deliverables

- Design Specification, Design Tokens, Component Library, Screen Specifications

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt, trừ trường hợp CONDITIONAL PASS đã ghi rõ hạn bổ sung.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Quyết định Design Review phải đính kèm.

## Approval Requirements

- Design Director phê duyệt thiết kế.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS chỉ được áp dụng khi màn hình thiếu trạng thái lỗi nhưng đã ghi rõ hạn bổ sung trước khi code màn hình đó.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu màn hình thiếu trạng thái lỗi thì CONDITIONAL PASS chỉ khi ghi rõ việc bổ sung trước khi code màn hình đó. Nếu thiết kế không khớp API thì FAIL và quay lại Phase 04.
