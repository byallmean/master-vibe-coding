# Workflow 00b: Change Proposal cho ứng dụng đang có

Responsible Agents: Chief AI Orchestrator, Product Manager, Solution Architect

Note: File này thuộc version 2.2. Dùng cho thay đổi trên codebase đã có, theo vòng propose, apply, archive học từ OpenSpec. Thay đổi nhỏ trên app đang có không cần chạy đủ 12 giai đoạn, nhưng phải có proposal ghi rõ delta trước khi sửa. Không sửa app đang có mà không có proposal.

## Objective

Mô tả thay đổi trên app đang có bằng delta spec rõ ràng, được duyệt trước khi sửa, áp dụng đúng delta, rồi gộp delta vào spec sống và lưu trữ proposal.

## Input

- Code, repository, branch và trạng thái hiện tại của app đang có
- TRIAGE.md của yêu cầu
- PRD, kiến trúc và spec sống hiện có của app

## Execution Steps

1. Pha Propose. Viết templates/CHANGE-PROPOSAL.md: mô tả thay đổi, lý do, delta spec ghi rõ ADDED, MODIFIED, REMOVED cho từng mục, danh sách task, rủi ro, cách rollback và gate bắt buộc. Ghi baseline trước khi sửa: commit hiện tại, image digest nếu có, trạng thái health, kết quả test trước khi sửa và backup hiện có
2. Duyệt proposal. Product Owner duyệt proposal trước khi sửa. Proposal đổi API, đổi database hoặc đổi giao diện chính phải có thêm duyệt của Solution Architect hoặc Design Director. Không sửa trước khi proposal được duyệt
3. Pha Apply. Làm theo đúng delta spec và danh sách task trong proposal. Mỗi task là một STORY.md tự chứa đủ context. Chạy test-first, code review hai tầng theo workflows/07c-code-review.md, test tổng thể và security audit theo mức triage. Nếu trong lúc làm phát hiện phạm vi vượt delta thì dừng lại, cập nhật proposal và xin duyệt lại, không tự mở rộng delta
4. Kiểm chứng sau khi apply. So sánh kết quả với baseline: health, test, chức năng cũ có còn chạy không. Chạy Verification Before Completion bằng lệnh chạy mới. Nếu sửa gây lỗi mới thì rollback về baseline trước khi thử hướng khác
5. Pha Archive. Khi thay đổi đã xong và gate đã vượt, gộp delta vào spec sống: cập nhật PRD, kiến trúc, API Specification, ERD và tài liệu liên quan, không để spec cũ nằm lại. Lưu trữ proposal đã hoàn thành kèm quyết định gate và bằng chứng. Ghi quyết định vào DECISIONS.md

## Deliverables

- CHANGE-PROPOSAL.md đã duyệt, kèm delta spec ADDED, MODIFIED, REMOVED
- Code và test theo đúng delta
- CODE-REVIEW.md nếu có review
- Spec sống đã cập nhật và proposal đã archive

## Quality Gate

Chỉ archive khi thay đổi đã vượt gate bắt buộc mà triage đã ghi, spec sống đã cập nhật và không còn mục nào trong delta chưa làm. Gate áp dụng tùy theo mức triage, tối thiểu là Testing Gate và Security Gate khi chạm tới dữ liệu nhạy cảm, cộng Design Acceptance Gate khi đổi giao diện chính.

## Failure Handling

Nếu proposal bị từ chối thì ghi rõ lý do và sửa proposal, không sửa code trước. Nếu trong lúc apply phát hiện delta sai thì dừng lại và cập nhật proposal. Nếu sau khi apply mà chức năng cũ hỏng thì rollback về baseline và mở lại proposal, không sửa tiếp trên bản hỏng.

## Next Workflow

07-development.md để bắt đầu apply, hoặc 07c-code-review.md sau khi code xong, tùy bước hiện tại
