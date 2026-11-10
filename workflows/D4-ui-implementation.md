# Design First D4: UI Implementation

Responsible Agents: UX Engineer, Frontend Engineer, Visual UI Designer

Note: File này thuộc chuỗi Design First của version 2.0. Nó chạy cùng Phase 07 Implementation hiện có, riêng cho phần frontend. Tên file D4 không có nghĩa là Phase 08 Quality Assurance.

## Objective

Xây dựng frontend theo đúng Design System đã duyệt, với nguyên tắc Professional, Modern, Clean, Consistent, Intuitive, Responsive, Accessible và Visually Balanced. Phong cách phải phù hợp ngành nghề, thương hiệu và người dùng, không mặc định mỗi ứng dụng đều dùng một phong cách.

## Input

- Design System và Design Tokens
- Screen Specification và Prototype đã duyệt
- API Specification
- Quyết định Design Review

## Execution Steps

1. Chọn công nghệ frontend theo yêu cầu dự án: React, Next.js, Vue, Nuxt, Angular, Tailwind CSS, CSS Modules, Component Libraries, Chart Libraries. Có thể dùng thư viện UI như shadcn ui, Radix UI, Ant Design, MUI hoặc thư viện phù hợp khác. Không bắt buộc một công nghệ cho mỗi dự án.
2. Cài đặt token thành biến dùng chung một lần. Mỗi component chỉ tham chiếu token, không ghi giá trị màu hay spacing riêng lẻ. Hạn chế custom code trùng lặp.
3. Triển khai theo module, theo đúng Screen Architecture. Mỗi module xong thì UX Engineer đối chiếu ngay với thiết kế, không đợi hết dự án.
4. Triển khai đầy đủ interaction và micro-interactions có mục đích: hover, focus, active, disabled, loading, success, error, confirmation, transition. Animation phải có mục đích, không lạm dụng.
5. Áp dụng UI Implementation Standard cho dashboard, bảng, form và hiển thị dữ liệu. Áp dụng JSON Policy tuyệt đối cho người dùng thường. Không dùng form mặc định hoặc bảng mặc định làm sản phẩm cuối mà chưa đánh giá.
6. Triển khai responsive thật ở viewport mục tiêu, không chỉ co nhỏ giao diện desktop. Triển khai accessibility cơ bản: bàn phím, màn hình đọc, tương phản và kích thước chữ.

## Deliverables

- Code frontend theo module, dùng token chung
- Component Library đã triển khai, ánh xạ 1-1 với Design System
- Báo cáo Design Consistency Audit của UX Engineer cho từng module
- Ảnh chụp thực tế ban đầu cho từng module, làm đầu vào cho Visual QA

## Quality Gate

Mỗi module chỉ được coi là xong phần implementation khi vượt qua quality-gates/ui-implementation-gate.md. Gate này kiểm tra token, component, trạng thái, JSON Policy, responsive và accessibility ở mức code và chạy thật, nhưng điểm Visual QA đầy đủ chỉ được tính ở workflow tiếp theo.

## Failure Handling

Nếu giao diện lệch thiết kế thì sửa giao diện, không tự sửa thiết kế trong lúc code. Nếu thiết kế không thể code đúng thì đưa về Visual UI Designer và Design Director. Nếu một module phá vỡ module trước thì dừng lại, sửa hoặc rollback module đó, không đẩy tiếp tính năng mới lên trên lỗi.

## Next Workflow

D5-visual-quality-assurance.md
