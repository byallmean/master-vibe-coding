# Development Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Architecture Gate và Design Gate đã vượt qua.
- STORY.md của module đã có, kèm file sẽ đọc, file sẽ sửa, lệnh kiểm chứng và output mong đợi.
- Baseline trước khi sửa đã ghi: commit hiện tại, trạng thái health, kết quả test trước khi sửa.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Code chạy được sau mỗi milestone. Build đạt, app khởi động được, luồng chính chạy được. Không chấp nhận code chỉ đọc đúng mà chưa chạy.
- Test-first có bằng chứng. Test thất bại đã viết trước khi viết code production cho cùng tính năng, log test thất bại và log test đậu sau khi sửa đều đính kèm.
- Coverage đạt ngưỡng. Coverage code mới và code thay đổi tối thiểu 80 phần trăm, hoặc có số mới và lý do điều chỉnh đã phê duyệt.
- Code review hai tầng đã xong. CODE-REVIEW.md có cả tầng 1 spec compliance và tầng 2 code quality, kèm quyết định Approve. Reviewer không phải là agent vừa viết code đó trong cùng một phiên.
- Không phá API hay database. API cũ vẫn trả đúng, migration có rollback, không có thay đổi phá vỡ nào chưa ghi trong CHANGE-PROPOSAL hoặc ADR.
- Không có secret trong code, log hay ảnh container. Kết quả quét secret bằng gitleaks đính kèm.
- Tài liệu cập nhật. API Specification, README và ADR cập nhật theo code, không để tài liệu cũ nằm lại.
- Frontend dùng Design System. Module frontend đã vượt qua ui-implementation-gate nếu có thay đổi giao diện.

## Deliverables

- Code theo module, test của module, Pull Request có review

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- CODE-REVIEW.md và log test phải đính kèm, không chỉ ghi đã review và đã test.

## Approval Requirements

- Technical Project Manager phê duyệt kết quả module.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi code không chạy được, khi chưa có review hai tầng, khi coverage dưới ngưỡng mà không có lý do đã phê duyệt, hoặc khi có secret trong code.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu code không chạy được hoặc chưa có review thì FAIL, không được chuyển sang test tổng thể. Nếu test thất bại mà nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md.
