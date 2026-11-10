# Workflow 09b: Performance Audit

Responsible Agents: Performance Engineer, QA Engineer, Backend Engineer

Note: File này thuộc version 3.0. Performance được tách riêng khỏi workflows/09-security-audit.md. Security chạy ở 09, performance chạy ở 09b, mỗi bên có gate riêng. Không gộp chung hai báo cáo vào một file nữa.

## Objective

Đo hiệu năng bằng số liệu thật dưới tải, so sánh với ngân sách hiệu năng đã định trước, tìm nút thắt và chứng minh cải thiện bằng cách đo lại.

## Input

- Mục tiêu hiệu năng và ngân sách hiệu năng của dự án
- Code đã test và đã vượt qua Testing Gate
- Dữ liệu và lượng truy cập dự kiến

## Execution Steps

1. Xác định ngân sách hiệu năng trước khi đo, ghi vào PERFORMANCE-BUDGET trong báo cáo. Ngân sách mặc định nếu Product Owner chưa đặt số khác: LCP tối đa 2.5 giây, API p95 tối đa 500 mili giây, bundle JavaScript tối đa 300 KB sau khi nén, trang chính hiển thị nội dung đầu tiên trong tối đa 1.5 giây
2. Test trên dữ liệu có kích thước gần thực tế, không chỉ vài bản ghi mẫu. Ghi rõ kích thước dữ liệu và cấu hình test
3. Đo riêng biệt từng tầng: frontend, API, database, tài nguyên máy. Ghi số đo thật cho từng tầng, không viết nhận xét chung chung như chạy mượt hay hơi chậm
4. Tìm nút thắt trước khi đề xuất tối ưu. Mỗi nút thắt ghi rõ bằng chứng đo được, mức độ ảnh hưởng và đề xuất sửa
5. Sau khi tối ưu thì chạy lại test trong cùng điều kiện như lần đo đầu, so sánh số trước và sau để chứng minh cải thiện
6. Ghi rõ giới hạn của test, ví dụ dữ liệu giả lập khác dữ liệu thật ra sao, tải test khác tải thật ra sao

## Deliverables

- Performance Report kèm số đo thật cho từng tầng
- Danh sách nút thắt có mức độ ưu tiên
- Ngân sách hiệu năng của dự án và kết quả so với ngân sách

## Quality Gate

Chỉ chuyển giai đoạn khi vượt qua gate tại quality-gates/performance-gate.md với trạng thái PASS hoặc CONDITIONAL PASS có biện pháp kiểm soát ghi rõ. CONDITIONAL PASS không được áp dụng khi LCP vượt ngân sách trên luồng chính hoặc khi API p95 vượt ngân sách gấp đôi.

## Failure Handling

Nếu không đạt ngân sách thì trả lại cho Backend Engineer và Frontend Engineer kèm số đo thật, không trả lại bằng mô tả chung chung. Nếu tối ưu không cải thiện thì chạy workflows/08b-systematic-debugging.md để tìm nguyên nhân gốc, không tối ưu mò.

## Next Workflow

10-deployment.md
