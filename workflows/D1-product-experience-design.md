# Design First D1: Product Experience Design

Responsible Agents: Product Designer, UX Researcher, Design Director, Product Manager

Note: File này thuộc chuỗi Design First của version 2.0. Nó chạy bên trong Phase 05 UI UX Design hiện có, không thay thế số thứ tự 12 giai đoạn và không phải là một phase mới độc lập.

## Objective

Hiểu đúng người dùng và công việc của họ trước khi vẽ bất kỳ màn hình nào, rồi tổ chức thông tin và luồng thao tác theo cách người dùng hiểu, không theo cấu trúc database hoặc backend.

Triết lý: DESIGN FIRST, USER CENTRIC, FUNCTIONAL EXCELLENCE. Một sản phẩm tốt phải đồng thời đạt chức năng chính xác, trải nghiệm dễ hiểu dễ dùng, và thị giác đẹp chuyên nghiệp nhất quán.

## Input

- User Personas và User Journey
- Mục tiêu sản phẩm và thứ tự ưu tiên tính năng
- Yêu cầu nghiệp vụ
- Thiết bị mục tiêu và trình độ công nghệ của người dùng

## Execution Steps

1. STEP 1 Product và User Understanding. Trả lời: người dùng là ai, họ dùng app để làm gì, việc quan trọng nhất là gì, thao tác nào dùng thường xuyên, họ cần xem thông tin gì đầu tiên, khó khăn có thể gặp, họ dùng desktop tablet hay mobile, trình độ công nghệ ra sao. Đầu ra là User Personas, User Journey và Key Tasks.
2. STEP 2 Information Architecture. Thiết kế sitemap, navigation, menu hierarchy, module structure, screen hierarchy và information grouping theo cách người dùng gọi tên công việc.
3. STEP 3 User Flow và Interaction Design. Thiết kế luồng đăng nhập, dashboard, tìm kiếm, tạo, sửa, xóa, phê duyệt, báo cáo, upload và download, xử lý lỗi và nghiệp vụ đặc thù. Mỗi chức năng quan trọng phải có luồng rõ ràng. Tối ưu số bước, khả năng khám phá và tính nhất quán.
4. Kiểm tra luồng bằng kịch bản tác vụ cụ thể, ghi tỷ lệ hoàn thành và điểm tắc, không chỉ hỏi cảm tính chung chung.
5. Design Director duyệt Information Architecture trước khi chuyển sang Visual Direction.

## Deliverables

- USER-PERSONA.md
- USER-JOURNEY.md
- INFORMATION-ARCHITECTURE.md
- USER-FLOW.md
- Screen Architecture cho mỗi màn hình chính: mục đích, việc chính, hành động chính, hành động phụ, thứ tự khối thông tin

## Quality Gate

Chỉ chuyển sang Visual Design khi Design Director và Product Manager cùng duyệt Information Architecture và các luồng chính. Gate áp dụng là quality-gates/design-acceptance-gate.md ở mục Information Architecture, nhưng điểm tổng chỉ được tính sau khi có Visual QA. Nếu luồng chính còn thiếu trạng thái lỗi hoặc còn bước thừa không có lý do thì FAIL ở bước này, không đẩy sang vẽ màn hình.

## Failure Handling

Nếu Information Architecture khớp cấu trúc database hơn cách người dùng hiểu thì quay lại Step 2, không sửa bằng cách thêm menu phụ. Nếu luồng chính có quá nhiều bước thì cắt bớt bước và gom trường trùng lặp trước khi vẽ màn hình, không để việc tối ưu lại cho giai đoạn code.

## Next Workflow

D2-visual-design-system.md
