# Phase 04: System Architecture

Responsible Agents: Solution Architect, Database Architect

## Objective

Chọn kiến trúc và công nghệ dựa trên bằng chứng, thiết kế database, API, xác thực và tích hợp.

## Input

- PRD
- Development Plan

## Execution Steps

1. Đánh giá công nghệ theo yêu cầu, quy mô, chi phí và bảo trì
2. Thiết kế hệ thống theo module
3. Thiết kế database, ERD và API
4. Thiết kế xác thực, phân quyền và tích hợp
5. Vẽ sơ đồ luồng dữ liệu và làm threat modeling theo STRIDE cho từng luồng, ghi vào templates/THREAT-MODEL.md. Mỗi mối đe dọa ghi rõ attacker làm được gì cụ thể, mức độ nghiêm trọng và biện pháp giảm thiểu. Mỗi đe dọa Critical phải có biện pháp trước khi chốt kiến trúc.
6. Viết ADR và đánh giá rủi ro kỹ thuật

## Deliverables

- System Architecture Document
- Architecture Diagrams
- ERD
- API Specification
- ADR
- Technology Stack Decision
- Threat Model theo templates/THREAT-MODEL.md

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/architecture-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu hai phương án kiến trúc đều có rủi ro lớn thì ghi rõ trade-off và xin quyết định từ Product Owner.

## Next Workflow

05-ui-ux.md
