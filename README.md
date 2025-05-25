# Digital DSO App

Hệ thống mẫu triển khai kiến trúc Clean Code, Component-based Architecture, CI/CD và GitOps để quản lý danh mục Sáng Kiến Chiến Lược (SKCL) tại F88.

---

## 📅 Nhật ký phát triển

### Ngày 1 – 25/05/2025  
🔹 **Hành động chính:**  
- Tạo repo `digital-dso-app` trên GitHub  
- Thiết lập nhánh `main` + `develop`  
- Bổ sung `.gitignore` cho Python/Poetry  
- Viết mô tả ban đầu vào `README.md`  

🔸 **Khó khăn:**  
- [ghi vào nếu có]  

📌 **Ghi chú học được:**  
- GitHub hỗ trợ `.gitignore` theo ngôn ngữ  
- Việc chia `main`/`develop` giúp tách sản phẩm ổn định & môi trường phát triển  
- Thử Copilot agent trên Vscode - khá bất ngờ

## 📁 Folder Structure – Component-based Clean Architecture

```
src/
├── components/
│   ├── initiative_room/
│   │   ├── domain/
│   │   ├── application/
│   │   ├── interface/
│   │   └── infrastructure/
│   ├── portfolio_room/
│   │   ├── domain/
│   │   ├── application/
│   │   ├── interface/
│   │   └── infrastructure/
│   └── strategy_room/
│       ├── domain/
│       ├── application/
│       ├── interface/
│       └── infrastructure/
├── shared/
│   ├── config/
│   ├── core/
│   └── utils/
├── main.py
tests/
└── components/
    ├── initiative_room/
    ├── portfolio_room/
    └── strategy_room/
```

- Mỗi Room là một Component có đủ các tầng: `domain`, `application`, `interface`, `infrastructure`
- `shared/` chứa cấu hình, base class, helper function
- `tests/` tổ chức song song với `src/components/`

## 🧠 Nhật ký gợi ý hôm nay

📅 Ngày 2 – 26/05/2025  
🔹 **Hành động chính:**  
- Thiết lập cấu trúc thư mục theo từng Room (component)  
- Tạo `__init__.py` để Python nhận diện package  
- Cập nhật mô tả kiến trúc trong README  

🔸 **Khó khăn:**  
- [ghi vào nếu có]  

📌 **Ghi chú học được:**  
- Cấu trúc component giúp chia nhỏ team, module hóa logic  
- `__init__.py` cần thiết để test và import hoạt động ổn định

📅 Ngày 3 – 27/05/2025  
🔹 **Hành động chính:**  
- Cài Poetry  
- Tạo `pyproject.toml` với FastAPI, SQLAlchemy, Pydantic  
- Cài pytest, black, isort, flake8 cho dev  
- Chạy FastAPI Hello World  

🔸 **Khó khăn:**  
- Gặp vấn đề cài đặt Poetry - Do chưa update 
  - Lỗi không tìm thấy phiên bản Poetry 2.1.3:
Quá trình cài đặt Poetry báo lỗi vì không tồn tại phiên bản 2.1.3 trên PyPI. Poetry hiện chỉ có bản 1.x.

Lỗi khi cài qua pipx:
Quá trình cài đặt Poetry bằng pipx gặp lỗi build các package C extension (cffi, msgpack) do thiếu môi trường build hoặc thư viện hệ thống.

Nguyên nhân:

Chưa cập nhật pip, setuptools, wheel.
Thiếu Xcode Command Line Tools hoặc các thư viện build cần thiết (OpenSSL, header files).
Biến môi trường PATH chưa nhận diện pipx/poetry sau khi cài.
Cách khắc phục:

Cập nhật pip, setuptools, wheel.
Đảm bảo đã cài Xcode Command Line Tools (xcode-select --install).
Cài thêm OpenSSL nếu cần, và export biến môi trường.
Sử dụng lệnh cài đặt Poetry chính thức để lấy bản mới nhất.
Thêm $HOME/.local/bin vào PATH nếu cần.
Kết quả:
Sau khi thực hiện các bước trên, bạn đã cài đặt Poetry thành công và tiếp tục được các bước tiếp theo.

📌 **Ghi chú học được:**  
- Poetry quản lý dependencies rất gọn gàng  
- FastAPI có Swagger tích hợp cực tiện

📅 Ngày 4 – 28/05/2025  

🔹 **Hành động chính:**  
- Tạo Dockerfile chạy app FastAPI qua poetry
- Tạo docker-compose.yml chạy local
- Tạo file .env.example để quản lý cấu hình
- Build & chạy app qua Docker
  
🔸 **Khó khăn:**  
- [ghi nếu có]

📌 **Ghi chú học được:**  
- Docker giúp chạy app mọi nơi mà không cần cài đặt local
- Tách rõ config `.env` giúp dễ CI/CD


