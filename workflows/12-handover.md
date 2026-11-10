# Phase 12: Documentation và Handover

Responsible Agents: Technical Project Manager, Chief AI Orchestrator

## Objective

Bàn giao đầy đủ để AI khác hoặc lập trình viên mới có thể tiếp tục mà không phải khám phá lại từ đầu.

## Input

- Toàn bộ tài liệu dự án
- Trạng thái code, database, API và deploy

## Execution Steps

1. Tổng hợp product, technical, architecture, database, API và deployment docs
2. Viết user manual, troubleshooting và runbook
3. Liệt kê known issues, technical debt và next steps
4. Đóng gói AI Handover Package có 22 mục
5. Kiểm tra lại rằng handover không chứa secret
6. Ghi handover sống vào file HANDOVER định dạng markdown trong thư mục .handoff ở gốc repo dự án, theo templates/HANDOVER-TEMPLATE.md, viết lại toàn bộ ở mỗi lần bàn giao
7. Trước khi viết handover sống thì đóng băng việc đang làm, commit hoặc stash code, dừng tiến trình đang chạy, kiểm chứng trạng thái thật bằng git status và nhánh hiện tại
8. Commit và push file handover sống cùng với code của lần làm việc đó
9. Bên nhận việc pull mới nhất, đọc file HANDOVER trong .handoff, PROJECT_STATUS và git log gần nhất, nêu trạng thái hiện tại và bước tiếp theo trước khi chạm vào code

## Deliverables

- AI Handover Package
- Handover sống trong repo dự án, đã commit và push
- Product Documentation
- Technical Documentation
- User Manual
- Troubleshooting Guide

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/handover-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu handover thiếu trạng thái thực tế hoặc chưa phân biệt xác minh, giả định và chưa biết thì trả lại để bổ sung. Nếu handover sống chưa commit và push hoặc không khớp với git status thì trả lại để viết lại.

## Next Workflow

01-discovery.md cho dự án tiếp theo hoặc bảo trì
