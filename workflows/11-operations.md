# Phase 11: Operations

Responsible Agents: DevOps/SRE Engineer, Technical Project Manager

## Objective

Vận hành, giám sát, backup, xử lý sự cố và cập nhật an toàn sau khi deploy.

## Input

- Ứng dụng đang chạy production
- Operations Runbook

## Execution Steps

1. Thiết lập monitoring, logging và alerting
2. Kiểm tra backup bằng cách khôi phục thử
3. Theo dõi hiệu năng và cập nhật dependency có kiểm soát
4. Xử lý sự cố theo quy trình, ghi lại bài học và viết postmortem theo templates/POSTMORTEM.md trong vòng 3 ngày sau khi sự cố kết thúc. Postmortem ghi timeline, nguyên nhân gốc, ảnh hưởng, biện pháp khắc phục và biện pháp phòng ngừa có người chịu trách nhiệm và thời hạn. Không đổ lỗi cá nhân trong postmortem.
5. Tập luyện incident drill định kỳ: giả lập sự cố, chạy quy trình xử lý và ghi lại điểm yếu của quy trình để sửa trước khi sự cố thật xảy ra
6. Quản lý phiên bản và rollback khi cần

## Deliverables

- Operations Runbook
- Monitoring Dashboard Specification
- Backup và Recovery Plan
- Incident Response Procedure
- Postmortem theo templates/POSTMORTEM.md cho mỗi sự cố production

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/production-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu backup chưa từng được khôi phục thử thì ghi rõ là chưa xác minh, không gọi là an toàn.

## Next Workflow

12-handover.md
