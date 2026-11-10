# Design First D2: Visual Design System

Responsible Agents: Visual UI Designer, Design Director, Product Designer

Note: File này thuộc chuỗi Design First của version 2.0. Nó chạy bên trong Phase 05 UI UX Design hiện có, ngay sau Product Experience Design.

## Objective

Xây dựng một ngôn ngữ thiết kế có bản sắc riêng và một Design System dùng chung cho toàn bộ ứng dụng, trước khi vẽ màn hình chi tiết ở quy mô lớn.

## Input

- Information Architecture và User Flow từ D1-product-experience-design
- Design Vision từ Design Director
- Thương hiệu, phân khúc và đối tượng người dùng

## Execution Steps

1. STEP 4 Visual Direction. Xác định phân khúc sản phẩm, đối tượng, phong cách thương hiệu, mức độ chuyên nghiệp mong muốn, mật độ thông tin, màu chủ đạo, typography, visual hierarchy và design references. Nghiên cứu sản phẩm tốt trong cùng lĩnh vực như Linear, Stripe, Notion, Apple, Figma hoặc ứng dụng chuyên ngành tương ứng. Rút ra nguyên tắc, không sao chép nguyên mẫu.
2. STEP 5 Design System. Xây đủ 20 mục bắt buộc: Brand Identity, Color Palette, Typography Scale, Spacing Scale, Layout Grid, Border và Radius, Shadows, Icon System, Button System, Form System, Table System, Card System, Navigation Components, Modal và Dialog, Toast và Notification, Charts và Data Visualization, Loading States, Empty States, Error States, Responsive Rules.
3. Định nghĩa Design Tokens và tái sử dụng thống nhất. Không tạo mỗi màn hình một phong cách riêng. Không dùng component mặc định làm Design System hoàn chỉnh.
4. Định nghĩa quy tắc hiển thị dữ liệu theo JSON và Developer Interface Policy: object thành field có tên rõ ràng, array thành bảng hoặc danh sách, boolean thành trạng thái trực quan, ngày định dạng theo ngôn ngữ người dùng, tiền tệ kèm đơn vị, trạng thái có nhãn dễ hiểu, ID kỹ thuật bị ẩn nếu không có giá trị sử dụng. JSON chỉ ở khu vực Advanced hoặc Developer Settings có hướng dẫn rõ ràng.
5. Định nghĩa quy tắc dashboard, bảng dữ liệu và form. Dashboard phải có chỉ số quan trọng, hành động cần làm, cảnh báo, hoạt động gần đây và biểu đồ thực sự hữu ích, không tạo biểu đồ để trang trí. Bảng phải hỗ trợ search, filter, sort, phân trang, row action và bulk action khi cần. Form phải có nhóm trường, label rõ ràng, validation, thông báo lỗi dễ hiểu, trạng thái loading và success, autocomplete khi phù hợp và input chuyên biệt theo loại dữ liệu.
6. Định nghĩa quy tắc accessibility và đa ngôn ngữ. Accessibility theo WCAG 2.1 mức AA cho luồng chính: điều hướng bằng bàn phím cho mỗi chức năng, độ tương phản chữ tối thiểu 4.5 cho chữ thường và 3 cho chữ lớn, trạng thái focus nhìn thấy được, ảnh có alt text, form có label gắn đúng trường, thông báo lỗi đọc được bằng trình đọc màn hình, tôn trọng tùy chọn giảm chuyển động. I18n: mỗi chuỗi hiển thị nằm trong file ngôn ngữ riêng theo từng locale, ngày giờ số và tiền tệ định dạng theo locale của user, bố cục chịu được chuỗi dịch dài hơn chuỗi gốc. Ghi cả hai quy tắc vào phụ lục của DESIGN-SYSTEM.md.
7. Design Director duyệt Visual Direction và Design System trước khi vẽ màn hình chi tiết.

## Deliverables

- DESIGN-BRIEF.md
- VISUAL-DIRECTION.md
- DESIGN-SYSTEM.md
- Design Tokens có thể dùng trực tiếp khi code
- Quy tắc Dashboard, Table, Form và JSON Policy được ghi trong DESIGN-SYSTEM.md

## Quality Gate

Chỉ chuyển sang Prototype khi Design System có đủ 20 mục và được Design Director duyệt. Gate áp dụng là quality-gates/design-acceptance-gate.md ở mục Design Consistency và Visual Quality. Nếu mỗi màn hình dùng một phong cách riêng thì FAIL, không sửa bằng cách thêm theme phụ.

## Failure Handling

Nếu Visual Direction không phù hợp phân khúc hoặc người dùng thì quay lại Step 4 và chọn lại phong cách có lý do, không giữ phong cách chung chung vì dễ vẽ. Nếu Design System thiếu mục thì bổ sung mục đó trước khi vẽ màn hình, không để màn hình tự định nghĩa kiểu riêng rồi hợp nhất sau.

## Next Workflow

D3-prototype-review.md
