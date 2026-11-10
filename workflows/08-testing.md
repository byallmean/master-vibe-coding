# Phase 08: Quality Assurance

Responsible Agents: QA Engineer

## Objective

Chứng minh tính năng hoạt động đúng bằng test thật ở nhiều tầng, không chỉ đọc code.

## Input

- Code theo module
- Acceptance Criteria

## Execution Steps

1. Viết test plan theo acceptance criteria, kèm ngưỡng coverage mặc định tối thiểu 80 phần trăm cho code mới và code thay đổi
2. Chạy unit, integration, API, UI và end-to-end test. Phần UI phải chạy thêm D5-visual-quality-assurance.md và vượt qua visual-qa-gate và design-acceptance-gate trước khi kết luận giai đoạn này
3. Chạy security test phủ định: gọi API không có token, gọi bằng token của user khác để lấy resource của user khác, gửi field lạ trong body, gửi giá sai nếu có thanh toán. Ghi kết quả vào Security Report
4. Chạy regression test sau mỗi lần sửa
5. Ghi lỗi có bước tái hiện và mức độ
6. Tổng hợp coverage report và danh sách lỗi còn lại

## Deliverables

- Test Plan
- Test Coverage Report
- Danh sách lỗi và trạng thái sửa

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/testing-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu test thất bại thì ghi lỗi và trả lại cho dev, không tự sửa test để test đậu. Nếu nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md, không sửa code khi chưa biết nguyên nhân gốc.

## Next Workflow

09-security-audit.md
