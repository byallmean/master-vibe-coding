# Phase 00: Triage và Phân loại quy mô

Responsible Agents: Chief AI Orchestrator, Product Manager

Note: File này thuộc version 2.1. Mọi yêu cầu phải chạy qua triage trước khi vào workflow 01-discovery hoặc 07-development. Triage quyết định mức độ nặng của quy trình, không phải mức độ quan trọng của yêu cầu. Yêu cầu nhỏ vẫn có thể quan trọng, nhưng không cần chạy đủ 12 giai đoạn để làm đúng.

## Objective

Phân loại yêu cầu theo quy mô thay đổi thật, chọn đường chạy phù hợp, ghi rõ gate nào được bỏ và gate nào không được bỏ, rồi mới bắt đầu làm.

## Input

- Yêu cầu của Product Owner
- Code, repository, branch và trạng thái hiện tại nếu có
- CONSTITUTION.md của dự án nếu đã có

## Execution Steps

1. Đọc yêu cầu và đếm phạm vi thay đổi thật: số file dự kiến sửa, có đổi API hay không, có đổi database hay không, có đổi giao diện chính hay không, có chạm tới auth, payment, secret hay dữ liệu người dùng hay không.
2. Phân loại theo bảng dưới đây và ghi quyết định vào templates/TRIAGE.md. Nếu nằm giữa hai mức thì chọn mức nặng hơn, không chọn mức nhẹ để chạy nhanh.
3. Kiểm tra CONSTITUTION.md của dự án. Nếu dự án chưa có constitution thì tạo theo templates/CONSTITUTION.md trước khi làm mức M hoặc L. Mức S được làm ngay nhưng phải tuân thủ các nguyên tắc bất khả xâm phạm đã ghi trong SKILL.md.
4. Chọn đường chạy theo mức và ghi rõ gate bắt buộc. Không được tự ý bỏ gate bắt buộc vì lý do tốc độ.

## Phân loại S, M, L

- Mức S, sửa nhỏ. Điều kiện: 1 đến 3 file, không đổi API, không đổi database, không đổi giao diện chính, không chạm tới auth, payment, secret hay dữ liệu người dùng. Đường chạy: mô tả thay đổi, viết test thất bại trước, sửa code, chạy test và regression, review, commit. Gate bắt buộc: Testing Gate ở mức test đã chạy, Security Gate chỉ khi chạm tới dữ liệu nhạy cảm, Deployment Gate khi deploy. Không cần discovery, PRD, kiến trúc hay design system mới.
- Mức M, tính năng nhỏ. Điều kiện: 4 đến 10 file, có thể đổi API hoặc database nhỏ, có thể thêm một màn hình, có thể chạm tới auth hoặc dữ liệu người dùng. Đường chạy rút gọn: specify, plan, tasks, implement. Chạy 01-discovery rút gọn, 02-business-analysis, 04-architecture ở mức rút gọn, D1 đến D3 chỉ khi đổi giao diện chính, 07-development, 08-testing, 09-security-audit, 10-deployment. Nếu thay đổi trên app đang có thì viết CHANGE-PROPOSAL trước theo workflows/00b-change-proposal.md. Gate bắt buộc: Requirement Gate, Architecture Gate, Testing Gate, Security Gate, Deployment Gate, Design Acceptance Gate chỉ khi đổi giao diện chính.
- Mức L, dự án mới hoặc làm lại lớn. Điều kiện: hơn 10 file, đổi kiến trúc, đổi database lớn, thêm module mới, làm lại giao diện, hoặc chạm tới nhiều hệ thống. Đường chạy: đủ 12 giai đoạn từ 01-discovery đến 12-handover, kèm chuỗi Design First D1 đến D5 và đầy đủ gate. Không được rút gọn mức L thành mức M.

## Deliverables

- TRIAGE.md đã điền, có mức S, M hoặc L, lý do phân loại và đường chạy đã chọn
- Danh sách gate bắt buộc và gate được bỏ, kèm lý do
- CONSTITUTION.md của dự án nếu là mức M hoặc L và dự án chưa có

## Quality Gate

Chỉ bắt đầu làm khi TRIAGE.md đã ghi rõ mức, đường chạy và gate bắt buộc, và Product Owner hoặc Orchestrator đã xác nhận mức phân loại. Nếu trong lúc làm phát hiện phạm vi vượt mức đã chọn thì dừng lại, triage lại và nâng mức, không cố làm tiếp ở mức cũ.

## Failure Handling

Nếu không phân loại được vì thiếu thông tin thì ghi rõ thông tin thiếu, hỏi Product Owner một câu cụ thể, và tạm chọn mức M cho đến khi có đủ thông tin. Không được tự đoán mức S khi chưa đọc code thật. Nếu một thay đổi mức S phá vỡ chức năng cũ thì nâng lên mức M và chạy regression đầy đủ.

## Next Workflow

01-discovery.md cho mức L, 07-development.md cho mức S và M sau khi có TRIAGE.md
