# Phase 07: Implementation

Responsible Agents: Frontend Engineer, Backend Engineer, Integration Engineer

## Objective

Phát triển theo module và milestone, giữ phần mềm chạy được sau mỗi milestone.

## Input

- Architecture Document
- API Specification
- Design Specification

## Execution Steps

1. Ghi baseline trước khi sửa: commit hiện tại, image digest nếu có, trạng thái health, kết quả test trước khi sửa và backup hiện có. Làm việc trên branch hoặc git worktree riêng cho thay đổi này, không sửa trực tiếp trên branch chính
2. Kiểm tra yêu cầu, kiến trúc, CONSTITUTION.md và phụ thuộc của module
3. Thiết kế hoặc cập nhật database nếu cần
4. Phát triển backend, frontend và tích hợp API. Phần frontend phải chạy theo D4-ui-implementation.md và vượt qua ui-implementation-gate, không chỉ chạy đúng chức năng
5. Viết test thất bại trước khi viết code production cho cùng tính năng, chạy test và thấy test thất bại đúng lý do, rồi mới viết code cho test đó qua. Viết test cho logic nghiệp vụ, trường hợp biên và security test phủ định. Không viết code production khi chưa có test thất bại trước
6. Kiểm tra bảo mật ngay trong lúc viết code khi code chạm tới auth, payment, database, API key, secret hoặc dữ liệu người dùng. Kiểm tra quyền sở hữu từng resource, chỉ ghi field trong allowlist, validate dữ liệu ngoài bằng schema runtime, đặt rate limit cho endpoint nhạy cảm. Gọi Security Engineer ngay khi phát hiện vấn đề, không đợi đến Phase 09
7. Code review hai tầng theo workflows/07c-code-review.md và github/pull-request-review.md. Chỉ chuyển sang test tổng thể khi có Approve hoặc khi vấn đề đã sửa xong và review lại đạt
8. Cập nhật tài liệu, commit và tạo pull request

## Deliverables

- Code theo module
- Test của module
- Pull Request có review
- Tài liệu cập nhật

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/development-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu một module phá vỡ milestone trước thì dừng lại, sửa hoặc rollback module đó, không đẩy tiếp tính năng mới lên trên lỗi. Nếu test thất bại hoặc app lỗi mà nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md, không sửa code khi chưa biết nguyên nhân gốc.

## Next Workflow

08-testing.md
