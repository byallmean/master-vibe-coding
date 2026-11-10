# Phase 10: Deployment

Responsible Agents: DevOps/SRE Engineer

## Objective

Đưa sản phẩm lên môi trường thật có health check, smoke test và rollback, không tuyên bố thành công khi chưa có bằng chứng.

## Input

- Code đã vượt Testing Gate và Security Gate
- Môi trường đích

## Execution Steps

1. Kiểm tra production readiness và staging. Kiểm tra trước khi ship: tắt debug và source map ở production, thư mục git không truy cập được từ bên ngoài, security header đầy đủ, CORS chỉ whitelist domain của mình, key production không dùng cho môi trường preview hay dev
2. Chạy migration và kiểm tra secret
3. Build production và deploy theo quy trình đã chọn
4. Kiểm tra health check, domain, SSL và log
5. Chạy smoke test và chuẩn bị rollback
6. So sánh kết quả sau deploy với baseline đã ghi trước khi deploy: health, test và chức năng cũ có còn chạy không. Nếu có lỗi mới thì rollback về baseline

## Deliverables

- Deployment Checklist đã đánh dấu
- Bằng chứng health check và smoke test
- Kế hoạch rollback

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/deployment-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ.

## Failure Handling

Nếu health check hoặc smoke test thất bại thì rollback theo runbook, không sửa trực tiếp trên production để chữa cháy.

## Next Workflow

11-operations.md
