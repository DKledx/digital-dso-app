📅 Ngày 24 – 24/06/2025  
🔹 Hành động chính:
- Tích hợp cloud logging: Logtail hoặc Sentry
- Gửi log & lỗi realtime từ app lên cloud
- Gắn request_id vào trace log để tìm lỗi chính xác

🔸 Ghi chú:
- Sentry rất mạnh cho lỗi dạng exception; Logtail mạnh về full log pipeline
- Sau này có thể tích hợp alert (email, Slack) từ các nền tảng này

💡 Nhận định:
- App chưa có log = app mù
- App có cloud log = app có giác quan để tự bảo vệ
