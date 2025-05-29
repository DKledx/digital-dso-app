# 🧾 Log Sample – Digital DSO App

## INFO log – Khi xử lý request thành công
```text
[2025-06-25 10:22:15] [INFO] [initiative_router] [request_id=abc-123] Bắt đầu tạo SKCL
```

## WARNING log – Khi dữ liệu không hợp lệ nhẹ
```text
[2025-06-25 10:22:17] [WARNING] [create_usecase] [request_id=abc-123] Quý nhập sai format: '2025-Q2'
```

## ERROR log – Khi gặp exception trong quá trình xử lý
```text
[2025-06-25 10:22:20] [ERROR] [repo_sqlalchemy] [request_id=abc-123] Lỗi khi ghi DB: UNIQUE constraint failed: initiative.name
```

## Logtail (Cloud)
Có thể xem log tại: 
Có request_id → trace từng hành động người dùng