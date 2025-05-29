# ⚙️ Thiết lập Môi trường Phát triển & Khởi động Hệ thống

## 01. Thông tin tài liệu

- **Tên tài liệu**: Thiết lập môi trường phát triển và khởi động hệ thống  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Hướng dẫn chuẩn hóa setup môi trường cho developer mới  
- Đảm bảo mọi thành viên đều chạy được app trong vòng **10 phút**  
- Tối ưu cho local dev, CI, staging qua Docker  
- Tạo cơ sở cho kiểm thử, code review và demo nội bộ  

---

## 🧱 03. Yêu cầu Hệ thống

| Yêu cầu        | Phiên bản đề xuất                |
|----------------|----------------------------------|
| Python         | >= 3.11.x                        |
| Poetry         | >= 1.6.x                         |
| Docker         | >= 24.x                          |
| Docker Compose | >= 2.x                           |
| VS Code        | Khuyến nghị + Extension (Python, Docker, Pylance) |

---

## 📦 04. Các bước Thiết lập Môi trường Local

### 🔹 Bước 1: Clone Repository

```bash
git clone https://github.com/<your-org>/digital-dso-app.git
cd digital-dso-app
````

### 🔹 Bước 2: Cài Poetry và thư viện

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

### 🔹 Bước 3: Tạo file `.env` từ mẫu

```bash
cp .env.example .env
```

### 🔹 Bước 4: Kích hoạt môi trường ảo và chạy app

```bash
poetry shell
uvicorn src.main:app --reload
```

* App chạy tại: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 05. Thiết lập với Docker (Tùy chọn)

Nếu bạn không muốn cài trực tiếp Python/Poetry:

```bash
docker-compose up --build
```

* App chạy tại: `http://localhost:8000`
* Tự động đồng bộ `.env` và thư mục `src/`

---

## 🧪 06. Kiểm tra sau khi cài đặt

```bash
black . --check
flake8 src/
mypy src/
pytest
```

---

## 🛠 07. Script tiện ích (tùy chọn)

Tạo file `scripts/dev.sh`:

```bash
#!/bin/bash
echo "🔧 Running dev bootstrap..."
poetry install
cp .env.example .env
black . && isort . && flake8 src/ && mypy src/ && pytest
```

> Gợi ý: Bạn có thể tạo thêm `scripts/test.sh`, `scripts/format.sh` để hỗ trợ CI/CD hoặc local testing.

---

## 🌐 08. Cấu hình IDE (khuyến nghị dùng VS Code)

Tạo file `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

---

## 📚 09. Tài liệu Tham chiếu Nội bộ

* \[Mục 06 – Dependency Management]
* \[Mục 10 – CI/CD Pipeline]
* \[Mục 03 – Tech Stack & Tooling]

---

## ✅ Gợi ý Hành động Tiếp theo

1. Kiểm tra toàn bộ quy trình bootstrap trên **Mac**, **Windows**, **Linux**
2. Đảm bảo `.env.example` đầy đủ biến cho local + CI
3. Tạo folder `scripts/` chứa `dev.sh`, `test.sh`, `format.sh`
4. Đưa tóm tắt cài đặt này vào `README.md`
5. Tiếp tục viết \[Mục 08 – Feature Design & Dev Flow] để hướng dẫn phát triển một tính năng chuẩn

