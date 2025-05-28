📅 Ngày 22 – 22/06/2025  
🔹 Hành động chính:
- Gắn middleware sinh `request_id` tự động
- Log chuẩn hóa theo format: time, level, module, request_id
- Trả `X-Request-ID` về frontend để trace lỗi dễ
🔸 Ghi chú:
- Sau này có thể gắn `request_id` vào Sentry, logtail, Prometheus, hoặc Kibana
💡 Nhận định:
- Logging không chuẩn → không trace được bug thật
- Từ hôm nay trở đi: “không có `request_id` = log không hợp lệ”
