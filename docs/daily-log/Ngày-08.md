📅 Ngày 8 – 04/06/2025  
🔹 Hành động chính:
- Viết schema Pydantic cho request/response tạo SKCL
- Viết usecase `CreateInitiativeUseCase` không phụ thuộc framework
- Viết mock repo + test đơn vị với pytest

🔸 Khó khăn:
- Tách pure logic khỏi DB/ORM để test dễ
- Kiểm soát cấu trúc file và import tương đối rõ ràng
Ghi chú
- Poetry báo lỗi version Python không phù hợp (3.8.12), phải chuyển sang Python >=3.11.
- Khi chạy `pytest`, báo thiếu command do môi trường ảo mới chưa cài dependencies.
- Đã phải chạy `poetry install` để cài đầy đủ các package cho môi trường mới.
- Nhận cảnh báo `DeprecationWarning: datetime.datetime.utcnow() is deprecated`, đã sửa thành `datetime.now(UTC)` để đúng chuẩn Python mới.
- Lưu ý khi dùng `git add .` có thể add cả file không mong muốn, nên kiểm tra lại bằng `git status` trước khi commit.


📌 Ghi chú học được:
- Clean Architecture đúng nghĩa = logic thuần, không bị phụ thuộc
- Việc mock repository rất hiệu quả để test nhanh & không cần DB
