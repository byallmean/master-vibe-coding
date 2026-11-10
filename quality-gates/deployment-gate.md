# Deployment Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Testing Gate và Security Gate đã vượt qua.
- Deployment Checklist đã điền đầy đủ.
- Kế hoạch rollback đã viết và đã có người chịu trách nhiệm rollback.
- Baseline trước khi deploy đã ghi: commit, image digest, trạng thái health, kết quả test và backup hiện có.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Staging đạt trước khi deploy production. Bản build sẽ deploy đã chạy trên staging và vượt qua smoke test ở staging. Không deploy production bản chưa chạy ở staging.
- Migration an toàn. Migration đã chạy thử ở staging, có rollback, và không xóa dữ liệu. Migration phá vỡ phải có kế hoạch cụ thể và phê duyệt riêng.
- Secret đúng môi trường. Secret production không dùng cho preview hay dev, file env đã kiểm tra, không có secret trong log deploy.
- Kiểm tra bảo mật trước khi ship. Debug tắt, source map tắt, thư mục git không truy cập được, security header đầy đủ, CORS chỉ whitelist domain của mình. Kết quả kiểm tra bằng lệnh thật đính kèm.
- Health check đạt. Endpoint health trả kết quả tốt trên môi trường đích, kèm log health check có ngày giờ.
- Domain, SSL và log đạt. Domain trỏ đúng, chứng chỉ SSL còn hạn, log chạy và không chứa secret.
- Smoke test đạt. Các luồng chính chạy được trên môi trường đích sau khi deploy, kèm log smoke test.
- Rollback sẵn sàng. Các bước rollback đã viết, đã biết cách quay về image và commit trước, và đã có người chịu trách nhiệm rollback.

## Deliverables

- Deployment Checklist, bằng chứng health check và smoke test, kế hoạch rollback

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Log health check và smoke test phải là log chạy thật trên môi trường đích, không dùng log staging để chứng minh production.

## Approval Requirements

- Product Owner phê duyệt deploy production.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện coi là deploy xong.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi health check thất bại, smoke test thất bại, migration chưa có rollback, hoặc kiểm tra bảo mật trước khi ship chưa đạt.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu health check hoặc smoke test thất bại thì FAIL và rollback theo kế hoạch, không sửa trực tiếp trên production. Sau khi rollback thì so sánh với baseline đã ghi trước khi deploy để xác nhận hệ thống về trạng thái cũ.
