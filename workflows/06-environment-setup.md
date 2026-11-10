# Phase 06: Development Environment

Responsible Agents: DevOps/SRE Engineer, Solution Architect

## Objective

Thiết lập repository, môi trường, Docker, CI/CD và secret sao cho mọi người đều chạy được cùng một cách.

## Input

- Repository hiện tại nếu có
- Kiến trúc và công nghệ đã chọn

## Execution Steps

1. Kiểm tra repository, branch, README và cấu trúc hiện tại
2. Thiết lập branch strategy và commit convention
3. Thiết lập môi trường phát triển và database
4. Thiết lập Docker nếu phù hợp và CI/CD cơ bản
5. Chuẩn hóa biến môi trường và secret, không ghi secret vào code. Kiểm tra file env đã có trong gitignore trước commit đầu tiên và quét secret trong lịch sử git bằng gitleaks

## Deliverables

- Development Environment
- Repository Documentation
- CI/CD Foundation
- Development Setup Guide

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/development-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu repository hiện tại lớn hơn mô tả thì dừng lại, kiểm tra lại toàn bộ cấu trúc trước khi thêm code mới.

## Next Workflow

07-development.md
