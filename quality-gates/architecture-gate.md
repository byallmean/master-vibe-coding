# Architecture Gate

Gate này được viết lại ở version 2.2 với bảng tiêu chí cụ thể, theo mẫu của Design Acceptance Gate.

## Entry Criteria

- Requirement Gate đã vượt qua.
- CONSTITUTION.md của dự án đã được kiểm tra.
- Đánh giá công nghệ đã có bằng chứng, không chỉ theo cảm tính.

## Required Activities

- Kiểm tra từng tiêu chí trong bảng dưới đây, kèm bằng chứng cho từng tiêu chí.
- Đối chiếu bằng chứng chạy thật, không chỉ đọc mô tả.
- Ghi lại quyết định và người phê duyệt.

## Bảng tiêu chí

- Kiến trúc phù hợp yêu cầu. Mỗi module trong kiến trúc ánh xạ tới yêu cầu trong PRD, không có module thừa và không có yêu cầu nào chưa có module phụ trách.
- Database thiết kế đầy đủ. ERD có đủ bảng, khóa chính, khóa ngoại và quan hệ. Mỗi thay đổi schema đều có migration kèm rollback.
- API thiết kế đầy đủ. Mỗi endpoint có method, đường dẫn, input, output, mã lỗi và quyền truy cập. API đối tượng trước phải có phiên bản.
- Xác thực và phân quyền thiết kế rõ. Ghi rõ cách xác thực, cách phân quyền, cách kiểm tra quyền sở hữu resource và cách lưu session. Security Engineer đã review thiết kế xác thực.
- Tích hợp bên ngoài thiết kế rõ. Mỗi tích hợp có chủ sở hữu, dữ liệu trao đổi, giới hạn tần suất, cách xử lý lỗi và thử lại.
- ADR cho quyết định lớn. Mỗi quyết định kiến trúc lớn đều có ADR ghi lý do, phương án đã loại và trade-off. Quyết định lớn mà không có ADR thì FAIL.
- Rủi ro kỹ thuật đã đánh giá. Mỗi rủi ro lớn có mức độ, ảnh hưởng và phương án giảm thiểu.

## Deliverables

- System Architecture Document, ERD, API Specification, ADR

## Exit Criteria, điều kiện PASS

Tất cả các tiêu chí trong bảng trên đều đạt. Không được bù trừ tiêu chí này bằng tiêu chí khác.

## Evidence

- Link tới file, commit, pull request, log test, log deploy hoặc ảnh chụp kết quả kiểm tra khi phù hợp.
- Mỗi bằng chứng đều có ngày và phạm vi kiểm tra.
- ADR phải đính kèm, mỗi ADR có ngày, người quyết định và trade-off.

## Approval Requirements

- Product Owner phê duyệt kiến trúc và ADR cho quyết định lớn.
- Các quyết định về bảo mật, mất dữ liệu, chi phí hạ tầng, deploy production và thay đổi kiến trúc lớn phải có phê duyệt của Product Owner.
- Gate chỉ được đánh dấu PASS khi có phê duyệt và bằng chứng đầy đủ.

## Trạng thái gate

- PASS: Đủ điều kiện chuyển giai đoạn.
- CONDITIONAL PASS: Được tiếp tục với các hạn chế được ghi nhận và có biện pháp kiểm soát. CONDITIONAL PASS không được áp dụng khi thiếu ADR cho quyết định lớn, thiếu thiết kế xác thực hoặc thiếu ERD.
- FAIL: Không được chuyển giai đoạn.

## Xử lý khi không đạt

Nếu thiếu ADR cho quyết định lớn thì FAIL, không được bắt đầu code dựa trên kiến trúc chưa chốt.
