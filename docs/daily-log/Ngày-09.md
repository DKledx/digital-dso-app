📅 Ngày 9 – 05/06/2025  
🔹 Hành động chính:
- Viết endpoint POST /initiative
- Tách interface khỏi logic nghiệp vụ
- Sử dụng Depends để inject use case

🔸 Khó khăn:
- Tổ chức import cho đúng theo module
- Kiểm soát schema và dependency injection

Đảm bảo đăng ký router đúng trong main.py để endpoint xuất hiện trên Swagger UI.
Kiểm tra kỹ lỗi import: Nếu có lỗi import ở bất kỳ file nào liên quan, FastAPI sẽ không load endpoint.
Chạy đúng lệnh uvicorn với đường dẫn module chính xác (src.main:app), tránh nhầm lẫn khi có nhiều file main.
Xóa cache .pyc khi cần nếu gặp lỗi không rõ nguyên nhân hoặc endpoint không xuất hiện.
Kiểm tra lại Swagger UI sau mỗi thay đổi lớn, dùng hard refresh (Cmd+Shift+R) để tránh cache trình duyệt.
Kiểm soát file commit: Chỉ commit những file thực sự cần thiết, tránh dùng git add . nếu workspace có nhiều file tạm.
Kiểm thử API kỹ lưỡng với nhiều trường hợp dữ liệu để đảm bảo logic hoạt động đúng.


📌 Ghi chú học được:
- Interface nên cực kỳ mỏng – không nên có logic
- Việc giữ repo mock tách biệt giúp test nhanh và không cần DB
