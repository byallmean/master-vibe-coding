# Phase 09: Security Audit

Responsible Agents: Security Engineer

Note: File này được viết lại ở version 2.1 theo 9 bước audit của vibe-security, đã điều chỉnh cho stack tự host. Từ version 3.0, performance được tách riêng sang workflows/09b-performance-audit.md và quality-gates/performance-gate.md. Security không chỉ chạy ở Phase 09. Bất cứ khi nào code chạm tới auth, payment, database, API key, secret hoặc dữ liệu người dùng thì Security Engineer phải được gọi ngay từ Phase 04, Phase 07 và Phase 08.

## Objective

Tìm rủi ro bảo mật bằng bằng chứng cụ thể, phân loại theo mức độ nghiêm trọng, kèm code trước và sau khi sửa cho từng phát hiện.

## Input

- Code đã test
- Danh sách dependency
- Danh sách endpoint, tích hợp bên ngoài và luồng thanh toán nếu có
- CONSTITUTION.md của dự án

## Execution Steps

Luật cơ bản: không bao giờ tin dữ liệu do client gửi. Giá, user ID, vai trò, subscription, feature flag và rate limit counter đều phải được kiểm tra hoặc thực thi ở server. Chỉ kiểm tra bước nào liên quan tới stack thật của dự án, bỏ qua bước không liên quan và ghi rõ lý do bỏ. Chi tiết từng bước nằm trong security/references, chỉ load file liên quan: secrets-and-env, database-security, authentication, rate-limiting, payments, mobile, ai-integration, deployment, data-access, file-upload-and-ssrf.

1. Secrets và biến môi trường. Quét secret cứng trong code, log, cấu hình và lịch sử git bằng gitleaks. Kiểm tra không có secret nào bị đưa vào bundle client qua tiền tố như NEXT_PUBLIC, VITE hay EXPO_PUBLIC. Kiểm tra file env đã có trong gitignore. Nếu secret từng bị commit thì coi như đã lộ và phải rotate ngay.
2. Kiểm soát truy cập database. Kiểm tra mọi bảng đều có chính sách truy cập theo chủ sở hữu, không có chính sách nào cho phép tất cả user đọc mọi dòng. Kiểm tra không có field nhạy cảm nào mà user tự sửa được qua update. Kiểm tra bảng phụ, bảng audit và bucket file đều có chính sách riêng.
3. Xác thực và phân quyền. Kiểm tra JWT bằng verify chữ ký, từ chối thuật toán none, kiểm tra issuer, audience và hạn dùng. Kiểm tra mọi endpoint đều xác thực và kiểm tra quyền sở hữu resource ở handler và ở tầng truy cập dữ liệu, không chỉ ở middleware hay forward-auth. Kiểm tra token lưu trong cookie HttpOnly kèm Secure và SameSite, không lưu trong localStorage.
4. Rate limiting và chống lạm dụng. Kiểm tra mọi endpoint auth, AI call, gửi email hay SMS, xử lý file và webhook đều có rate limit kết hợp theo IP và theo user.
5. Thanh toán nếu có. Kiểm tra giá tra cứu ở server, không lấy giá từ request của client. Kiểm tra webhook xác minh chữ ký bằng raw body. Kiểm tra trạng thái subscription ở server mỗi request được bảo vệ.
6. Mobile nếu có. Kiểm tra token lưu trong secure storage, API key không nằm trong bundle, deep link có xác thực.
7. AI và LLM nếu có. Kiểm tra API key của AI chỉ ở server, có spending cap cứng và usage cap theo từng user. Kiểm tra user input không nối thẳng vào system prompt. Kiểm tra output của LLM được coi là dữ liệu không tin cậy và được sanitize trước khi render.
8. Cấu hình deploy. Kiểm tra tắt debug và source map ở production, thư mục git không truy cập được từ bên ngoài, security header đầy đủ, CORS chỉ whitelist domain của mình, key production không dùng cho môi trường preview hay dev.
9. Truy cập dữ liệu và validation. Kiểm tra mọi query đều dùng parameter, không nối chuỗi user input vào SQL. Kiểm tra ORM không nhận trực tiếp object từ request body làm điều kiện lọc. Kiểm tra mọi dữ liệu ngoài đều được validate bằng schema runtime. Kiểm tra không spread request body thẳng vào database, chỉ ghi các field trong allowlist.
10. File upload và SSRF. Kiểm tra file upload chỉ chấp nhận loại file và dung lượng đã khai báo, quét nội dung trước khi lưu, không cho upload file thực thi, không cho truy cập file của user khác qua đường dẫn. Kiểm tra server không gọi URL do user nhập khi chưa kiểm tra allowlist. Chi tiết nằm trong security/references/file-upload-and-ssrf.md, chỉ load khi dự án có tính năng upload file hoặc gọi URL do user nhập.
11. Phân loại phát hiện Critical, High, Medium, Low kèm file, dòng, tên lỗi, attacker làm được gì cụ thể và code trước và sau khi sửa. Lỗi Critical phải báo ngay ở đầu báo cáo.
12. Kiểm tra lại sau khi sửa bằng lệnh chạy mới, không dùng kết quả cũ.

## Deliverables

- Security Report theo templates/SECURITY-REPORT.md
- Danh sách sửa chữa có ưu tiên

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/security-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ. CONDITIONAL PASS không được áp dụng cho phát hiện Critical, secret lộ, hay auth bypass.

## Failure Handling

Nếu có phát hiện Critical hoặc High thì dừng deploy, sửa trước hoặc ghi rõ phương án kiểm soát tạm thời có phê duyệt, có thời hạn và người chịu trách nhiệm. Nếu nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md, không sửa đoán mò. Nếu sửa gây lỗi mới thì rollback về baseline trước khi thử hướng khác.

## Next Workflow

09b-performance-audit.md
