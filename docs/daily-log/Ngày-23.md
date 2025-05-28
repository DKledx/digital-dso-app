📅 Ngày 23 – 23/06/2025  
🔹 Hành động chính:
- Ghi log ra file + console cùng lúc
- Tạo thư mục `logs/` tự động
- Log format có timestamp, level, module, request_id
🔸 Ghi chú:
- File log sẽ là input cho ELK, Loki, hoặc upload qua Logtail, Fluentd
- Logfile sẽ được mount volume nếu chạy Docker
💡 Nhận định:
- Log có request_id = trace được user
- Log lưu file = audit, debug production hoặc phân tích forensic
