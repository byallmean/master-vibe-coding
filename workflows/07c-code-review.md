# Workflow 07c: Code Review hai tầng

Responsible Agents: Code Reviewer, QA Engineer, Security Engineer khi có vấn đề bảo mật

Note: File này thuộc version 2.2. Chạy sau 07-development và trước 08-testing cho mỗi pull request. Review tách thành hai tầng riêng biệt, tầng 1 kiểm tra đúng spec, tầng 2 kiểm tra chất lượng code. Không trộn hai tầng vào nhau.

## Objective

Đảm bảo code trước khi vào test tổng thể đã đúng spec, có test, không phá API hay database, không lộ secret và không vi phạm Design System.

## Input

- Pull Request hoặc diff cần review
- PRD, API Specification, Design System và acceptance criteria liên quan
- STORY.md hoặc CHANGE-PROPOSAL.md của thay đổi
- Test Plan và kết quả test

## Execution Steps

1. Chọn reviewer. Reviewer không được là agent vừa viết code đó trong cùng một phiên nếu có thể tách agent. Nếu bắt buộc cùng agent thì ghi rõ là tự review và chỉ được Comment, không được tự Approve. Ghi tên reviewer vào báo cáo
2. Tầng 1 Spec Compliance. Reviewer đọc STORY.md hoặc CHANGE-PROPOSAL.md và acceptance criteria trước khi đọc code. Kiểm tra từng acceptance criteria có được đáp ứng hay không, API có đúng spec không, database có đúng ERD không, migration có rollback không, giao diện có đúng Design System không, test có đủ cho acceptance criteria không. Ghi kết quả tầng 1 trước khi sang tầng 2
3. Tầng 2 Code Quality. Chỉ bắt đầu khi tầng 1 đã xong. Kiểm tra code dễ đọc, không trùng lặp, xử lý lỗi đầy đủ, log đúng cách, không có code chết, đúng quy ước của dự án
4. Kiểm tra bảo mật ở mức code. Kiểm tra secret trong code hoặc log, quyền truy cập và quyền sở hữu resource, validation đầu vào, field ngoài allowlist, giá lấy từ client, token lưu sai chỗ. Phát hiện Critical báo ngay cho Orchestrator, không đợi hết review
5. Kiểm tra test. Test thất bại đã viết trước khi viết code hay không, coverage code mới và code thay đổi có đạt ngưỡng 80 phần trăm hay không, có sửa test để test đậu hay không, security test phủ định có chạy hay không
6. Ghi báo cáo review theo templates/CODE-REVIEW.md, tách riêng tầng 1 và tầng 2, mỗi vấn đề có file, dòng, mức độ và đề xuất sửa cụ thể
7. Kết luận bằng quyết định rõ ràng: Approve khi cả hai tầng đều đạt, Request Changes khi có vấn đề Critical hoặc High, Comment khi chỉ có gợi ý nhỏ. Chỉ chuyển sang 08-testing khi có Approve hoặc khi vấn đề đã sửa xong và review lại đạt

## Deliverables

- CODE-REVIEW.md có hai tầng riêng biệt và quyết định cuối cùng
- Danh sách vấn đề phân loại Critical, High, Medium, Low
- Quyết định Approve, Request Changes hoặc Comment

## Quality Gate

Chỉ chuyển sang 08-testing khi có Approve, hoặc khi vấn đề Critical và High đã sửa xong và review lại đạt. Gate áp dụng là quality-gates/development-gate.md. Không được tự Approve code do chính mình viết trong cùng một phiên.

## Failure Handling

Nếu tầng 1 FAIL thì trả lại cho dev kèm acceptance criteria chưa đạt, không sửa bằng tầng 2. Nếu phát hiện bảo mật Critical thì dừng review, báo ngay cho Orchestrator và Security Engineer. Nếu review lại lần hai vẫn có vấn đề Critical hoặc High thì đưa cho Orchestrator quyết định có cắt phạm vi hay không, không kéo dài review vô hạn.

## Next Workflow

08-testing.md
