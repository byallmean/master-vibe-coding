# Discovery Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- TRIAGE.md đã có mức phân loại S, M hoặc L và đường chạy đã chọn.
- CONSTITUTION.md của dự án đã có hoặc đã ghi rõ lý do chưa có đối với mức S.
- Ý tưởng ban đầu của Product Owner đã có bằng văn bản.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Vấn đề rõ ràng. Vấn đề được viết thành một câu, nói rõ ai gặp vấn đề gì và hậu quả nếu không sửa. Không chấp nhận mô tả chỉ có tính năng muốn làm mà không nói vấn đề.
- Người dùng xác định. Nhóm người dùng chính có tên, đặc điểm và cách họ làm việc hiện tại. Không chấp nhận người dùng chung chung là mọi người.
- Phạm vi ban đầu. Ghi rõ phạm vi làm và phạm vi không làm trong giai đoạn này, kèm lý do.
- Khả thi có bằng chứng. Đánh giá khả thi dựa trên công nghệ đã có, dữ liệu đã có hoặc thí nghiệm nhỏ, không dựa trên cảm tính. Ghi rõ giả định nào chưa xác minh.
- Giá trị có thể đo. Ghi rõ làm xong thì đo bằng chỉ số nào, ai đo và khi nào đo.

## Deliverables

- Product Vision, Problem Statement, Initial Scope, Feasibility Assessment

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Giả định chưa xác minh phải được liệt kê riêng, kèm hạn xác minh và người chịu trách nhiệm.

## Approval Requirements

- Product Owner phê duyệt vấn đề, người dùng và phạm vi.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi vấn đề chưa rõ hoặc người dùng chưa xác định.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu vấn đề chưa rõ thì FAIL, quay lại Idea Discovery, không chuyển sang phân tích yêu cầu chi tiết.
