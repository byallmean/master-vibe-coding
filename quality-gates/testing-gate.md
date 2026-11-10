# Testing Gate

Gate này được viết lại ở version 2.1 với ngưỡng số cụ thể, theo mẫu của Design Acceptance Gate. Không đánh dấu PASS chỉ bằng lời khẳng định test đã chạy.

## Entry Criteria

- Giai đoạn trước đã có đầu ra đầy đủ hoặc có lý do hoàn lại ghi rõ.
- Tài liệu cần thiết đã có trong repository hoặc thư mục dự án.
- Test Plan đã có, kèm ngưỡng coverage và danh sách acceptance criteria cần test.

## Required Activities

- Kiểm tra từng deliverable theo checklist của gate.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.
- Kiểm tra test thất bại đã được viết trước khi viết code production cho cùng tính năng, không chỉ kiểm tra test đậu sau khi code xong.

## Deliverables

- Test Plan, Test Coverage Report, danh sách lỗi

## Tiêu chí và ngưỡng, điều kiện PASS

Tất cả các điều kiện sau phải đồng thời đạt, không được bù trừ:

- Coverage tối thiểu 80 phần trăm dòng code cho code mới và code thay đổi. Product Owner có thể điều chỉnh ngưỡng cho từng dự án nhưng phải ghi rõ số mới và lý do vào TEST-PLAN.md.
- Mỗi acceptance criteria đều có ít nhất một test, và test đó đã chạy thật.
- Test đã chạy ở các tầng phù hợp với thay đổi: unit cho logic nghiệp vụ, integration cho API và database, end-to-end cho luồng chính.
- Security test phủ định đã chạy: gọi API không có token, gọi bằng token của user khác để lấy resource của user khác, gửi field lạ trong body, gửi giá sai nếu có thanh toán.
- Regression test đã chạy sau mỗi lần sửa và không có lỗi mới xuất hiện.
- Không có lỗi nghiêm trọng nào chưa sửa hoặc chưa có phương án kiểm soát có thời hạn và người chịu trách nhiệm.
- Không sửa test để test đậu và không bỏ test mà không ghi lý do.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Log test phải là log chạy mới, không dùng log cũ để chứng minh test mới chạy.
- Coverage report phải ghi rõ phạm vi tính coverage là code mới và code thay đổi hay toàn bộ code.

## Approval Requirements

- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi coverage dưới ngưỡng mà không có lý do đã phê duyệt, khi có acceptance criteria chưa có test, hoặc khi có lỗi nghiêm trọng chưa sửa.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu có lỗi nghiêm trọng chưa sửa và chưa có phương án kiểm soát thì FAIL. Nếu test thất bại mà nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md, không sửa test để test đậu.
