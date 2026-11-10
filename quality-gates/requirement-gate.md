# Requirement Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Discovery Gate đã vượt qua.
- BRD và PRD bản nháp đã có.
- Ma trận truy vết yêu cầu đã bắt đầu, mỗi yêu cầu có ID riêng.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Mỗi yêu cầu có nguồn gốc. Mỗi yêu cầu ghi rõ ai yêu cầu, vì vấn đề nào, và link tới BRD hoặc PRD. Yêu cầu không có nguồn gốc phải bị loại hoặc ghi rõ là giả định.
- Mỗi yêu cầu có tiêu chí nghiệm thu. Tiêu chí phải đo được, viết dưới dạng có thể kiểm tra, không viết chung chung như chạy tốt hay đẹp.
- Mỗi yêu cầu có test tương ứng trong ma trận truy vết. Yêu cầu nào chưa có test thì ghi rõ hạn bổ sung test trước khi code module đó.
- Không trùng lặp và không mâu thuẫn. Hai yêu cầu trùng nhau phải gộp, hai yêu cầu mâu thuẫn phải giải quyết trước khi qua gate.
- Ưu tiên rõ ràng. Mỗi yêu cầu có mức ưu tiên và lý do, phân biệt must have với nice to have. MVP chỉ gồm must have.
- Phạm vi đóng. Ghi rõ yêu cầu nào ngoài phạm vi và lý do, không để yêu cầu ngoài phạm vi lén lọt vào backlog mà không đánh dấu.

## Deliverables

- BRD, PRD, Use Case Specification, User Story Backlog, Acceptance Criteria

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt, trừ trường hợp CONDITIONAL PASS đã ghi rõ hạn bổ sung. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Ma trận truy vết phải đính kèm, mỗi dòng có ID yêu cầu, tiêu chí nghiệm thu và test tương ứng.

## Approval Requirements

- Product Owner phê duyệt PRD, backlog và mức ưu tiên.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS chỉ được áp dụng khi yêu cầu thiếu test nhưng đã ghi rõ hạn bổ sung trước khi bắt đầu code module đó.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu có yêu cầu không có tiêu chí nghiệm thu thì CONDITIONAL PASS chỉ khi ghi rõ hạn bổ sung trước khi bắt đầu code module đó, nếu không thì FAIL. Nếu có yêu cầu mâu thuẫn chưa giải quyết thì FAIL.
