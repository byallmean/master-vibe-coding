# Security Gate

Gate này được viết lại ở version 2.1 với bảng tiêu chí cụ thể và danh sách hard-fail, theo mẫu của Design Acceptance Gate. Không đánh dấu PASS chỉ bằng lời khẳng định đã kiểm tra bảo mật.

## Entry Criteria

- Giai đoạn trước đã có đầu ra đầy đủ hoặc có lý do hoàn lại ghi rõ.
- Tài liệu cần thiết đã có trong repository hoặc thư mục dự án.
- Security Report theo templates/SECURITY-REPORT.md đã có, kèm danh sách phát hiện phân loại Critical, High, Medium, Low.
- CONSTITUTION.md của dự án đã được kiểm tra và không có vi phạm nào chưa ghi lại.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng chạy thật cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

Mỗi tiêu chí đều phải đạt. Tiêu chí nào không liên quan tới dự án thì ghi rõ lý do bỏ, không để trống.

- Secrets và biến môi trường. Không có secret trong code, log, lịch sử git hoặc ảnh container. Không có secret trong bundle client. File env đã có trong gitignore. Bằng chứng là output quét secret bằng gitleaks.
- Kiểm soát truy cập database. Mỗi bảng có chính sách truy cập theo chủ sở hữu. Không có field nhạy cảm nào mà user tự sửa được qua update. Bảng phụ và bucket file có chính sách riêng.
- Xác thực và phân quyền. Mỗi endpoint đều xác thực và kiểm tra quyền sở hữu resource ở handler và ở tầng truy cập dữ liệu. JWT verify chữ ký, từ chối thuật toán none, kiểm tra issuer, audience và hạn dùng. Token lưu trong cookie HttpOnly kèm Secure và SameSite, không lưu trong localStorage.
- Rate limiting. Endpoint auth, AI call, gửi email hay SMS, xử lý file và webhook đều có rate limit kết hợp theo IP và theo user.
- Thanh toán nếu có. Giá tra cứu ở server, không lấy giá từ request của client. Webhook xác minh chữ ký bằng raw body. Trạng thái subscription kiểm tra ở server mỗi request được bảo vệ.
- AI và LLM nếu có. API key của AI chỉ ở server, có spending cap cứng và usage cap theo từng user. Output của LLM được sanitize trước khi render.
- Cấu hình deploy. Tắt debug và source map ở production. Thư mục git không truy cập được từ bên ngoài. Security header đầy đủ. CORS chỉ whitelist domain của mình.
- Truy cập dữ liệu và validation. Mỗi query đều dùng parameter. Mỗi dữ liệu ngoài đều được validate bằng schema runtime. Chỉ ghi các field trong allowlist vào database.
- Dependency. Danh sách dependency đã quét và ghi rõ phiên bản có lỗ hổng. Lỗ hổng Critical hoặc High đã có phương án sửa hoặc nâng cấp.

## Deliverables

- Security Report, Performance Report

## Exit Criteria, điều kiện PASS

Tất cả các điều kiện sau phải đồng thời đạt, không được bù trừ:

- Không còn phát hiện Critical hoặc High chưa có phương án xử lý.
- Không có secret lộ trong code, log, lịch sử git hoặc ảnh container.
- Phân quyền đã được kiểm tra cả trường hợp hợp lệ và không hợp lệ, kèm kiểm tra quyền sở hữu từng resource.
- Security test phủ định đã chạy và đã đậu.
- Mỗi rủi ro được chấp nhận có chủ đích đã ghi rõ lý do, phạm vi ảnh hưởng và ngày xem lại trong Security Report.

## Hard-fail, không được CONDITIONAL PASS

- Bất kỳ phát hiện Critical nào chưa sửa.
- Secret lộ trong code, log, lịch sử git hoặc ảnh container.
- Auth bypass, nghĩa là truy cập được resource mà không cần xác thực hoặc dùng token của user khác.
- Giá hoặc subscription lấy từ request của client mà không kiểm tra lại ở server.
- Secret từng bị commit vào lịch sử git mà chưa rotate.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- Output của công cụ quét secret và quét dependency phải đính kèm, không chỉ ghi đã quét.
- Kết quả kiểm tra header, CORS, debug, source map và thư mục git phải là kết quả lệnh chạy thật trên môi trường đích.

## Approval Requirements

- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.
- Security Engineer có quyền từ chối nghiệm thu nếu có phát hiện Critical, dù chức năng hoạt động đúng.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát, kèm thời hạn sửa và người chịu trách nhiệm. CONDITIONAL PASS không được áp dụng cho bất kỳ mục nào trong danh sách hard-fail.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu có phát hiện Critical thì FAIL tuyệt đối, không được CONDITIONAL PASS cho mục này. Nếu secret từng bị commit thì rotate ngay trước khi làm tiếp. Nếu nguyên nhân chưa rõ thì chạy workflows/08b-systematic-debugging.md.
