# master-vibe-coding

master-vibe-coding là một hệ điều hành phát triển phần mềm bằng AI, không chỉ là một prompt viết code. Nó giúp AI đưa một ý tưởng từ giai đoạn ý tưởng đến production, vận hành, bảo trì và bàn giao, với bằng chứng chạy thật ở mỗi bước.

## Kiến trúc 3 tầng

Tầng 1 là Master Orchestrator, bộ não trung tâm tiếp nhận yêu cầu, chọn chuyên gia, điều phối thứ tự và kiểm soát chất lượng.

Tầng 2 là 19 chuyên gia độc lập, mỗi chuyên gia có vai trò, phạm vi, đầu vào, đầu ra, quy trình, checklist và tiêu chí nghiệm thu riêng. Từ version 2.0, ngoài 14 chuyên gia của bản 1.0 còn có Design Director, Product Designer, Visual UI Designer và UX Engineer. Từ version 2.2 thêm Code Reviewer, cùng Chief AI Orchestrator điều phối toàn bộ.

Tầng 3 là Project Workspace, mỗi dự án có bộ nhớ, tài liệu và trạng thái riêng, không trộn context giữa các dự án.

## Các chuyên gia

Product Manager, Business Analyst, UX Researcher, Solution Architect, Database Architect, UI/UX Designer, Frontend Engineer, Backend Engineer, Integration Engineer, QA Engineer, Security Engineer, Performance Engineer, DevOps/SRE Engineer, Technical Project Manager, Design Director, Product Designer, Visual UI Designer, UX Engineer, Code Reviewer, và Chief AI Orchestrator điều phối toàn bộ.

Chi tiết từng chuyên gia xem trong thư mục agents.

## 12 giai đoạn

01 Idea Discovery, 02 Business Analysis, 03 Product Planning, 04 System Architecture, 05 UI/UX Design, 06 Development Environment, 07 Implementation, 08 Quality Assurance, 09 Security Audit, 09b Performance Audit, 10 Deployment, 11 Operations, 12 Documentation và Handover.

Chi tiết từng giai đoạn xem trong thư mục workflows. Từ version 2.0, bên trong giai đoạn 05, 07 và 08 còn có chuỗi Design First gồm D1-product-experience-design, D2-visual-design-system, D3-prototype-review, D4-ui-implementation và D5-visual-quality-assurance. Từ version 2.1, chuỗi này đổi tên từ 05, 06, 07, 08, 09 sang D1 tới D5 để không trùng số với 12 giai đoạn hiện có. Các file này không thay thế giai đoạn 06, 07, 08 hay 09 hiện có, mỗi file đều ghi rõ vị trí của nó trong chuỗi.

## Design First trong version 2.0

Triết lý là DESIGN FIRST, USER CENTRIC, FUNCTIONAL EXCELLENCE. Thiết kế tham gia từ phân tích sản phẩm, đi qua Information Architecture, User Flow, Visual Direction, Design System đủ 20 mục, Wireframe và Prototype, rồi mới triển khai frontend theo Design System. Không hiển thị JSON thô cho người dùng thông thường. Không nghiệm thu giao diện chỉ bằng cách đọc code mà phải chạy thật, chụp screenshot ở viewport mục tiêu và đối chiếu với thiết kế đã duyệt. Design Acceptance Gate tính theo thang 100, đạt khi tổng tối thiểu 85 và không tiêu chí nào dưới 70, kèm điều kiện không lỗi nghiêm trọng, không JSON thô và không thành phần vỡ ở viewport mục tiêu.

## Có gì mới trong version 2.1

Mọi yêu cầu bắt đầu bằng triage ở workflows/00-triage.md để phân loại mức S, mức M hay mức L rồi mới chọn đường chạy tương ứng. Mức S là sửa nhỏ, mức M chạy rút gọn, mức L chạy đủ 12 giai đoạn. Mỗi dự án mức M hoặc mức L phải có CONSTITUTION.md với 5 đến 10 nguyên tắc bất khả xâm phạm, kiểm tra ở đầu mỗi workflow lớn.

Test phải viết trước code theo nguyên tắc test thất bại trước rồi mới viết code cho test qua. Ngưỡng coverage mặc định là tối thiểu 80 phần trăm cho code mới và code thay đổi. Debug đi theo workflows/08b-systematic-debugging.md với 4 pha tái hiện, thu hẹp phạm vi, tìm nguyên nhân gốc và sửa rồi xác minh lại. Không tuyên bố xong khi chưa làm đủ 5 bước Verification Before Completion bằng lệnh chạy mới.

Security được kiểm tra từ sớm, không đợi Phase 09. Luật cơ bản là không bao giờ tin dữ liệu do client gửi. Security Gate và Testing Gate được viết lại với tiêu chí và ngưỡng số cụ thể theo mẫu Design Acceptance Gate. Template SECURITY-REPORT mới bắt buộc ghi file và dòng, attacker làm được gì, code trước và sau khi sửa cho mỗi phát hiện.

## Có gì mới trong version 2.2

Quản lý context: PRD và kiến trúc lớn được chia nhỏ thành story theo templates/STORY.md, mỗi story tự chứa đủ context để một agent mới nhận là làm được. Mỗi task giao cho một agent mới khi nền tảng hỗ trợ. Khi context đã dùng quá 70 phần trăm thì dừng lại, ghi handover ngắn, compact hoặc làm mới phiên rồi mới tiếp tục.

Code review hai tầng: thêm agent Code Reviewer và workflows/07c-code-review.md. Tầng 1 kiểm tra code có đúng spec không, tầng 2 kiểm tra code có tốt không. Reviewer không được là agent vừa viết code đó trong cùng một phiên nếu có thể tách agent.

Change proposal: thêm workflows/00b-change-proposal.md và templates/CHANGE-PROPOSAL.md cho thay đổi trên ứng dụng đang có, theo vòng propose, apply và archive với delta spec ghi rõ ADDED, MODIFIED và REMOVED. Khi xong thì gộp delta vào spec sống, không để spec cũ nằm lại.

Tám gate còn lại được viết lại với bảng tiêu chí cụ thể theo mẫu Design Acceptance Gate: Discovery, Requirement, Architecture, Design, Development, Deployment, Production Acceptance và Handover. Hai gate UI Implementation và Visual QA đã cụ thể từ trước nên giữ nguyên.

Baseline và worktree: trước khi sửa phải ghi baseline gồm commit, image digest, trạng thái health, kết quả test và backup. Làm việc trên branch hoặc git worktree riêng, sau khi sửa thì so sánh với baseline, gây lỗi mới thì rollback.

Security references: thêm thư mục security/references với 9 file checklist bảo mật cho stack tự host, chỉ load file liên quan khi cần. Security test phủ định và quy trình secret đã lộ cùng accepted risk đã có từ version 2.1 nên không làm lại.

## Có gì mới trong version 3.1

Handover sống: file HANDOVER định dạng markdown trong thư mục .handoff ở gốc repo dự án, cập nhật rồi commit và push ở mỗi điểm bàn giao, gồm cuối phiên làm việc, context quá 70 phần trăm, sắp hết token, khi bị kẹt và trước khi chuyển việc cho agent khác. Trước khi viết thì đóng băng việc đang làm và kiểm chứng bằng git status với nhánh hiện tại, viết lại toàn bộ file mỗi lần bàn giao. Agent nhận việc pull mới nhất, đọc file HANDOVER, PROJECT_STATUS và git log gần nhất rồi mới code tiếp. Template handover thêm mục Cách tiếp tục và Nhật ký phiên làm việc, thành 22 mục, và chuẩn hóa dấu tiếng Việt. Handover Gate thêm tiêu chí file handover đã commit và push.

## Có gì mới trong version 3.0

Performance tách riêng: workflow 09b-performance-audit và quality-gates/performance-gate mới, với ngân sách mặc định gồm LCP tối đa 2.5 giây, API p95 tối đa 500 mili giây, bundle JavaScript tối đa 300 KB sau khi nén và query chậm nhất trong luồng chính tối đa 200 mili giây. Workflow 09 chỉ còn security.

Threat modeling và phân loại dữ liệu: Phase 04 thêm bước STRIDE với templates/THREAT-MODEL.md, templates/DATABASE-DESIGN.md thêm mục phân loại dữ liệu ghi rõ dữ liệu nào mã hóa khi lưu và khi truyền.

Security bổ sung: security/references/file-upload-and-ssrf.md mới với checklist upload file và SSRF, workflows/09-security-audit.md thêm bước kiểm tra upload và SSRF. Authentication reference thêm MFA và quản lý session gồm hết hạn, thu hồi từ xa và xoay refresh token.

Accessibility và đa ngôn ngữ: mục tiêu WCAG 2.1 mức AA cho luồng chính, ghi trong Design Acceptance Gate, D2-visual-design-system và phụ lục của templates/DESIGN-SYSTEM.md. I18n làm từ đầu với file ngôn ngữ riêng theo locale.

Vận hành: templates/POSTMORTEM.md mới, workflows/11-operations.md thêm viết postmortem trong 3 ngày sau sự cố và tập luyện incident drill định kỳ.

Ngân sách chi phí và token: ghi vào PROJECT_STATUS.md trước khi triển khai, gồm số task tối đa mỗi phiên, giới hạn context và model nào dùng cho việc nào. Khi một tài khoản sắp hết token thì handover đầy đủ để tài khoản còn lại tiếp tục ngay.

Ví dụ thật: examples/web-app, examples/api-app và examples/mobile-app, mỗi ví dụ có test thật chạy được, không còn chỉ có simulation bằng Python.

Cài đặt một lệnh: scripts/install.sh cài skill lên Muse, Claude Code, Cursor hoặc Codex rồi tự chạy validator kiểm tra.

Validator: thêm kiểm tra broken link cho mọi file .md, kiểm tra tên template trần trong templates và project-workspace. Số lượng kỳ vọng mới là 22 workflow, 30 template, 14 gate và 10 security reference.

Chuẩn hóa dấu tiếng Việt: toàn bộ file trong agents, workflows và quality-gates đã chuyển sang tiếng Việt có dấu, không đổi logic. Validator kiểm tra tên section bằng tiếng Việt có dấu.

## Quality Gates

Mỗi giai đoạn có gate riêng với entry criteria, deliverables, exit criteria, evidence và approval. Trạng thái gate chỉ có PASS, CONDITIONAL PASS hoặc FAIL. Không tự đánh dấu PASS khi thiếu bằng chứng.

Các gate: Discovery, Requirement, Architecture, Design, Development, Testing, Security, Deployment, Production Acceptance, Handover, và từ version 2.0 thêm Design Acceptance, UI Implementation và Visual QA. Từ version 3.0 thêm Performance Gate.

## GitHub-first

GitHub là trung tâm quản lý mã nguồn, lịch sử và tài liệu. Quy trình chuẩn là Issue, Task, Branch, Development, Test, Pull Request, Review, Merge, Release, Deployment.

Không xóa repository, không xóa branch, không force push, không ghi đè dữ liệu, không xóa migration, không thay đổi production database và không thay đổi secret khi chưa có phê duyệt.

## Bắt đầu dự án mới

1. Mở SKILL.md và đọc phần Bắt đầu dự án mới.
2. Chạy workflows/00-triage.md, ghi quyết định vào templates/TRIAGE.md và tạo CONSTITUTION.md nếu là mức M hoặc mức L.
3. Sao chép thư mục project-workspace sang thư mục dự án riêng.
4. Chạy workflow 01-discovery và ghi kết quả vào PROJECT_CONTEXT.md và PROJECT_STATUS.md.
5. Dừng lại ở mỗi quality gate và chỉ chuyển giai đoạn khi gate đạt.

## Tiếp tục dự án đang làm

1. Đọc PROJECT_CONTEXT.md, PROJECT_STATUS.md, CURRENT_TASK.md, BLOCKERS.md và file HANDOVER trong thư mục .handoff.
2. Kiểm tra repository, branch và commit hiện tại.
3. Xác định việc đã xong và việc còn dở từ code và bằng chứng thật.
4. Nêu trạng thái hiện tại và bước tiếp theo trước khi chạm vào code.
5. Tiếp tục từ trạng thái thật đó.

## Cài đặt

Xem docs/installation.md cho Muse, Claude Code, Cursor và GitHub Copilot. Xem docs/platform-adapters.md để biết cách ánh xạ việc điều phối subagent sang từng nền tảng, vì không phải nền tảng nào cũng hỗ trợ cùng một hệ thống subagent.

## Mở rộng skill

Xem docs/extension.md. Khi thêm chuyên gia, workflow hoặc gate mới, hãy cập nhật SKILL.md, README.md, CHANGELOG.md và chạy validator.

## Kiểm tra skill

Chạy:

python3 scripts/validate-skill.py
python3 scripts/validate-project-docs.py examples/simulation-project

Kết quả validation của bản phát hành 3.1.0 xem trong VALIDATION.md.

## Mô phỏng và ví dụ thật

Xem examples/simulation.md. Mô phỏng này đi qua dự án giả định có 3 module và có một test thật chạy bằng unittest cho logic chống trùng lịch hẹn. Kết quả test thật được ghi trong file mô phỏng, không phải số liệu tưởng tượng.

Ví dụ thật từ version 3.0: examples/web-app là ứng dụng web nhỏ bằng Node.js, examples/api-app là API nhỏ bằng Python, examples/mobile-app là khung mobile với logic thuần có test. Mỗi ví dụ có README riêng ghi rõ cách chạy test.

## Giới hạn còn tồn tại

- Skill này không tự chạy được nếu nền tảng không cho đọc file và chạy lệnh. Cần người dùng phê duyệt cho các tác vụ nguy hiểm.
- Skill này không thay thế quyết định của Product Owner về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn.
- Các MCP server chỉ được dùng khi server đó có thật, đã kết nối và có tài liệu connector hiện tại. Skill không tự đặt tên công cụ MCP.
- Các mục tiêu hiệu năng và coverage trong gate là mức mặc định, Product Owner có thể điều chỉnh và ghi rõ lý do. Từ version 2.1, ngưỡng coverage mặc định là tối thiểu 80 phần trăm cho code mới và code thay đổi.

## Hướng phát triển tiếp theo

- Thêm adapter cụ thể cho từng nền tảng khi có tài liệu chính thức mới.
- Mở rộng ví dụ thật theo stack mới khi dự án thực tế cần.
