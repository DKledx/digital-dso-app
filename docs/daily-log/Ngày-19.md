📅 Ngày 19 – 18/06/2025  
🔹 Hành động chính:
- Cài dotenv, chuẩn hóa .env theo từng môi trường
- Load động cấu hình trong code
- Cập nhật DB, PORT, LOG_LEVEL theo ENV
- Chuẩn bị sẵn sàng cho deploy staging
🔸 Ghi chú:
- Không push file `.env.*` thật, chỉ push `.env.example`
- Config động giúp dễ switch môi trường khi CI/CD
💡 Nhận định:
- Giai đoạn đầu nhiều hardcode → giờ clean và tách biệt rõ
- Multi-env là bắt buộc khi chuyển sang sản phẩm thật
