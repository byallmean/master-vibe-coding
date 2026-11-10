# Design First D3: Prototype Review

Responsible Agents: Product Designer, Visual UI Designer, Design Director, Product Manager, UI UX Designer

Note: File này thuộc chuỗi Design First của version 2.0. Nó chạy bên trong Phase 05 UI UX Design hiện có, ngay sau Visual Design System. Tên file D3 không có nghĩa là Phase 07 Implementation.

## Objective

Thiết kế và kiểm tra các màn hình quan trọng trước khi lập trình ở quy mô lớn, để lỗi về cấu trúc và luồng được phát hiện khi sửa còn rẻ.

## Input

- Information Architecture, User Flow và Screen Architecture
- Design System và Design Tokens
- Visual Direction đã duyệt

## Execution Steps

1. STEP 6 Wireframe và Prototype. Vẽ các màn hình quan trọng trước khi lập trình. Mỗi màn hình phải thể hiện header, sidebar hoặc navigation, content area, information hierarchy, primary actions, secondary actions, data presentation và interaction states.
2. Prototype phải cho phép kiểm tra các luồng sử dụng chính. Với sản phẩm phức tạp, thiết kế và kiểm tra các module độc lập trước.
3. STEP 7 Design Review và Approval. Design Director, Product Designer và Product Manager cùng review. Chỉ chuyển sang triển khai khi các màn hình chính đã có thiết kế, các luồng nghiệp vụ chính đã được xác định, Design System đã được xây dựng và không có mâu thuẫn lớn giữa yêu cầu và thiết kế.
4. Có thể dùng vertical slice để kiểm chứng thiết kế sớm, nhưng phải duy trì tiêu chuẩn thiết kế đã duyệt, không hạ tiêu chuẩn để chạy nhanh.
5. Ghi quyết định review theo mẫu DESIGN-REVIEW.md, kèm danh sách lỗi phân loại Critical, High, Medium, Low và người chịu trách nhiệm sửa.

## Deliverables

- Wireframes cho màn hình chính
- Prototype có thể kiểm tra luồng chính
- SCREEN-SPECIFICATION.md cho mỗi màn hình chính
- DESIGN-REVIEW.md có quyết định duyệt hoặc từ chối

## Quality Gate

Chỉ chuyển sang UI Implementation khi có quyết định duyệt bằng văn bản của Design Director, Product Designer và Product Manager. Gate áp dụng là quality-gates/design-acceptance-gate.md ở mục thiết kế, chưa tính điểm Visual QA vì chưa có giao diện thật. Nếu màn hình chính thiếu trạng thái rỗng, lỗi hoặc thành công thì CONDITIONAL PASS chỉ khi ghi rõ việc bổ sung trước khi code màn hình đó.

## Failure Handling

Nếu review phát hiện mâu thuẫn lớn giữa yêu cầu và thiết kế thì dừng triển khai và quay lại Product Experience Design hoặc Visual Design System tùy theo gốc lỗi, không sửa màn hình đơn lẻ để che mâu thuẫn. Nếu prototype không kiểm tra được luồng chính thì làm lại prototype, không dùng mô tả bằng lời thay cho kiểm tra luồng.

## Next Workflow

D4-ui-implementation.md
