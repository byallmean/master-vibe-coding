# Handover Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Mọi gate trước đã vượt qua hoặc có lý do hoãn lại ghi rõ.
- AI Handover Package bản nháp đủ 20 mục đã có.
- Trạng thái code, database, API và deploy hiện tại đã xác minh bằng bằng chứng thật.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.
- Kiểm chứng bằng cách để một agent mới đọc handover và nêu được trạng thái hiện tại và bước tiếp theo mà không cần khám phá lại toàn bộ dự án.

## Bảng tiêu chí

- Đủ 20 mục. Handover package đủ hai mươi mục theo templates/HANDOVER-TEMPLATE.md, không thiếu mục nào mà không ghi lý do.
- Phân biệt xác minh, giả định và chưa biết. Mỗi thông tin đánh dấu rõ là đã xác minh, giả định hay chưa biết. Không lẫn lộn giả định với sự thật.
- Trạng thái thực tế. Trạng thái code, database, API, deploy, gate và lỗi còn lại phản ánh đúng thực tế hiện tại, đối chiếu được với commit, log và bằng chứng thật.
- Bước tiếp theo rõ ràng. Người nhận biết được việc tiếp theo là gì, ai làm, khi nào làm và cần gì để làm.
- Không chứa secret. Handover không chứa mật khẩu, token, private key hay chuỗi kết nối có secret. Kết quả quét secret đính kèm.
- Tài liệu đồng bộ. PRD, kiến trúc, API Specification và tài liệu vận hành cập nhật theo code hiện tại, không để tài liệu cũ nằm lại. Thay đổi nào chưa gộp vào spec sống thì ghi rõ.
- Kiểm chứng đọc hiểu. Một agent mới đã đọc handover và nêu được trạng thái hiện tại và bước tiếp theo, kèm ngày kiểm chứng và tên agent.

## Deliverables

- AI Handover Package đầy đủ 20 mục

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Kết quả kiểm chứng đọc hiểu phải đính kèm.

## Approval Requirements

- Product Owner phê duyệt handover.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện bàn giao.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi handover chứa secret, khi thiếu trạng thái thực tế, hoặc khi lẫn lộn xác minh với giả định.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu handover thiếu trạng thái thực tế hoặc lẫn lộn xác minh với giả định thì FAIL. Bổ sung bằng chứng thật rồi mới đánh dấu lại.
