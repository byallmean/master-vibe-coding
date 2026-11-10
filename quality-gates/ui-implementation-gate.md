# UI Implementation Gate

Gate cho phần triển khai frontend theo Design System, áp dụng cho từng module ngay sau khi code xong module đó, trước khi chuyển sang Visual QA đầy đủ.

## Entry Criteria

- Design System, Design Tokens và Screen Specification đã được duyệt.
- Code frontend của module đã được viết và chạy được.
- API tích hợp của module đã có xử lý lỗi.

## Required Activities

- Kiểm tra token: mỗi component dùng token chung, không có giá trị màu hay spacing riêng lẻ không có lý do.
- Kiểm tra component: component ánh xạ 1-1 với Design System, không có component trùng lặp vô nghĩa.
- Kiểm tra trạng thái: hover, focus, active, disabled, loading, success, error và confirmation cho các tương tác chính.
- Kiểm tra JSON Policy: không có JSON thô cho người dùng thường. Object thành field có tên rõ ràng. Array thành bảng hoặc danh sách. Boolean thành trạng thái trực quan. Ngày định dạng theo ngôn ngữ người dùng. Tiền tệ kèm đơn vị. Trạng thái có nhãn dễ hiểu. ID kỹ thuật bị ẩn nếu không có giá trị sử dụng.
- Kiểm tra dashboard, bảng và form theo UI Implementation Standard: dashboard có chỉ số quan trọng và hành động cần làm, bảng có search filter sort phân trang khi cần, form có nhóm trường label validation và thông báo lỗi dễ hiểu.
- Kiểm tra responsive và accessibility ở mức code và chạy thật: bàn phím, màn hình đọc, tương phản, kích thước chữ.

## Deliverables

- Code frontend theo module
- Báo cáo Design Consistency Audit của UX Engineer cho module
- Ảnh chụp thực tế ban đầu của module

## Exit Criteria

- Mỗi component chính dùng token chung.
- Không có JSON thô ở giao diện người dùng thường.
- Các trạng thái tương tác và dữ liệu chính đã được triển khai.
- Lỗi API hiển thị rõ ràng, không trang trắng.
- Không có secret trong code frontend.

## Evidence

- Link tới file, commit, pull request, ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.

## Approval Requirements

- UX Engineer xác nhận module khớp thiết kế ở mức code và chạy thật.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển sang Visual QA.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát, không áp dụng cho JSON thô hoặc thiếu trạng thái lỗi của luồng chính.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu giao diện lệch thiết kế thì sửa giao diện, không tự sửa thiết kế trong lúc code. Nếu thiết kế không thể code đúng thì đưa về Visual UI Designer và Design Director trước khi code tiếp.
