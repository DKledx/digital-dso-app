📅 Ngày 13 – 11/06/2025  
🔹 Hành động chính:
- Viết test cho API khi input sai
- Mô phỏng thiếu trường `name`, `None`, format `quarter` sai
- Tăng độ an toàn và coverage cho hệ thống

🔸 Khó khăn:
- Một số lỗi chưa bắt nếu schema chưa có validator cụ thể
- Cần tách rõ validation logic ra schema hoặc UseCase
- Gặp lỗi test fail case không trả về 422 do schema chưa có validator cho trường `quarter`.
- Import schema không đồng nhất giữa các module, dẫn đến validator không chạy đúng.
- Một số lỗi import (ImportError) do thiếu hoặc sai định nghĩa response model.

🔸Cách khắc phục & kết quả:
- Đã bổ sung validator Pydantic v2 (`@field_validator`) cho trường `quarter` trong schema.
- Chuẩn hóa lại import schema ở router để đảm bảo FastAPI sử dụng đúng schema có validator.
- Bổ sung đầy đủ response model (`InitiativeCreateResponse`) trong schema để tránh lỗi import.
- Sau khi sửa, toàn bộ test fail case đã pass, hệ thống validate đúng và coverage tăng lên.

📌 Ghi chú học được:
- Không test fail case = tự đẩy rủi ro về production
- Pydantic validator rất tiện để kiểm tra format + rule domain
