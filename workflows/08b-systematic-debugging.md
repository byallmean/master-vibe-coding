# Workflow 08b: Systematic Debugging

Responsible Agents: QA Engineer, Backend Engineer, Frontend Engineer, Security Engineer khi lỗi liên quan bảo mật

Note: File này thuộc version 2.1. Được gọi từ Failure Handling của workflows 07-development và 08-testing, và từ bất kỳ giai đoạn nào khi test thất bại hoặc app lỗi mà nguyên nhân chưa rõ. Không sửa code khi chưa biết nguyên nhân gốc.

## Objective

Tìm nguyên nhân gốc của lỗi bằng bằng chứng, sửa đúng chỗ đó, và xác minh lại bằng lệnh chạy mới trước khi tuyên bố xong.

## Input

- Lỗi cụ thể: thông báo lỗi, log, bước tái hiện, dữ liệu đầu vào
- Code, commit, branch và trạng thái hiện tại
- Kết quả test thất bại và phạm vi ảnh hưởng

## Execution Steps

1. Pha 1 Tái hiện. Tái hiện lỗi bằng các bước cụ thể và ghi lại mỗi lần tái hiện được hay không. Nếu không tái hiện được thì ghi rõ môi trường, dữ liệu và thời điểm, không dự đoán lỗi đã tự hết. Lưu log và ảnh chụp nếu có.
2. Pha 2 Thu hẹp phạm vi. Xác định lỗi nằm ở tầng nào: giao diện, API, logic nghiệp vụ, database, tích hợp bên ngoài, môi trường hay deploy. Loại trừ từng tầng bằng test nhỏ hoặc bằng cách đọc code thật, không đoán theo cảm tính. Ghi lại baseline trước khi sửa: commit hiện tại, trạng thái health, kết quả test trước khi sửa.
3. Pha 3 Tìm nguyên nhân gốc. Hỏi tại sao 5 lần cho đến khi gặp nguyên nhân gốc, không dừng ở triệu chứng. Kiểm tra các nguyên nhân thường gặp: dữ liệu đầu vào sai định dạng, quyền truy cập thiếu, cấu hình môi trường lệch, migration chưa chạy, dependency đổi phiên bản, race condition, cache cũ. Ghi nguyên nhân gốc vào templates/DEBUG-REPORT.md kèm bằng chứng.
4. Pha 4 Sửa và xác minh lại. Viết test thất bại cho lỗi trước khi sửa nếu có thể, rồi sửa đúng chỗ nguyên nhân gốc, không sửa triệu chứng. Chạy lại toàn bộ test liên quan và regression. Kiểm tra lại theo checklist Verification Before Completion ở dưới đây.
5. Nếu sửa không được sau 3 lần thử có lý do thì dừng lại, ghi lại những gì đã thử và kết quả, và đưa cho Orchestrator hoặc Product Owner quyết định hướng khác, không sửa mở rộng phạm vi để thử vận may.

## Verification Before Completion

Không được tuyên bố xong nếu chưa làm đủ 5 bước sau, mỗi lần đều phải làm mới, không dùng kết quả cũ:

1. Xác định lệnh chứng minh: lệnh test, lệnh build, lệnh health check hoặc thao tác giao diện cụ thể sẽ chứng minh lỗi đã hết.
2. Chạy lệnh đó mới hoàn toàn, không dùng output của lần chạy trước.
3. Đọc toàn bộ output, không chỉ đọc dòng cuối.
4. Đối chiếu output với tuyên bố sẽ nói: lỗi đã hết, test đã đậu, không có lỗi mới xuất hiện.
5. Chỉ sau đó mới được nói xong, kèm lệnh đã chạy và output làm bằng chứng.

## Deliverables

- DEBUG-REPORT.md có 4 pha, nguyên nhân gốc và bằng chứng
- Test mới cho lỗi nếu có thể, phải thất bại trước khi sửa và đậu sau khi sửa
- Log test và regression sau khi sửa
- Quyết định tiếp tục hoặc dừng lại nếu sửa không được

## Quality Gate

Chỉ trở lại workflow gọi debug khi lỗi gốc đã có trong DEBUG-REPORT, test cho lỗi đã đậu, regression không có lỗi mới, và 5 bước Verification Before Completion đã làm đủ. Nếu chỉ sửa được triệu chứng thì ghi rõ là tạm thời, có hạn sửa gốc và người chịu trách nhiệm, không đánh dấu xong.

## Failure Handling

Nếu không tái hiện được lỗi thì ghi rõ giới hạn và theo dõi thêm, không đóng lỗi vì không thấy. Nếu nguyên nhân gốc nằm ngoài phạm vi dự án, ví dụ dịch vụ bên ngoài lỗi hoặc hạ tầng lỗi, thì ghi rõ và chuyển cho người phụ trách hạ tầng, kèm bằng chứng đã thu thập. Nếu sửa gây ra lỗi mới thì rollback về baseline đã ghi ở Pha 2 trước khi thử hướng khác.

## Next Workflow

07-development.md hoặc 08-testing.md, tùy workflow nào đã gọi debug
