📅 Ngày 10 – 06/06/2025  
🔹 Hành động chính:
- Viết integration test đầu tiên với `httpx`
- Gọi trực tiếp FastAPI app trong test
- Kiểm tra luồng từ schema → usecase → response
- 
🔸 Khó khăn:
- Phải dùng base_url ảo khi test FastAPI không chạy thật
- Đảm bảo test không bị phụ thuộc trạng thái hệ thống

🔹 Bài học rút ra:
- Viết test end-to-end giúp kiểm soát toàn bộ luồng nghiệp vụ, đảm bảo API hoạt động đúng từ validate đến phản hồi.
- Sử dụng `TestClient` của FastAPI đơn giản, dễ dùng cho kiểm thử API sync.
- Khi gặp lỗi với async test hoặc httpx, nên kiểm tra lại cách khởi tạo client và cân nhắc chuyển sang sync test nếu không cần thiết.
- Đảm bảo cấu trúc project rõ ràng, tách biệt giữa unit test (logic) và integration test (API).
- Kiểm tra kỹ log khi chạy test để phát hiện và xử lý lỗi import, cấu hình môi trường, hoặc thiếu package.
- Commit code thường xuyên sau mỗi bước hoàn thành để tránh mất mát và dễ kiểm soát thay đổi.

📌 Ghi chú:
- Test tự động giúp phát hiện lỗi sớm, tiết kiệm thời gian kiểm thử thủ công.
- Clean Architecture giúp code dễ kiểm thử, dễ mở rộng và bảo trì.

- Integration test là bước trung gian giữa unit và e2e
- Sử dụng `httpx.AsyncClient` rất tiện để test FastAPI không cần server thật
