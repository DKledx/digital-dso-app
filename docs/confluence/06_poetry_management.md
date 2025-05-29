# 🧰 Quản lý Thư viện và Môi trường Python

## 01. Thông tin tài liệu

- **Tên tài liệu**: Quản lý thư viện và môi trường Python  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Đảm bảo môi trường phát triển đồng bộ, dễ tái tạo  
- Quản lý thư viện rõ ràng, có kiểm soát version  
- Hỗ trợ kiểm tra an toàn và cập nhật định kỳ  
- Tối ưu CI/CD bằng cache và lockfile  

---

## 🧰 03. Công cụ sử dụng

| Công cụ       | Mục đích                      | Lý do chọn                                                        |
|---------------|-------------------------------|--------------------------------------------------------------------|
| Poetry        | Quản lý dependency & env      | Thay thế pip + virtualenv, chuẩn hóa bằng `pyproject.toml`         |
| dotenv        | Quản lý biến môi trường       | Hỗ trợ `.env`, dễ cấu hình dev/test/prod                          |
| Docker        | Tái tạo môi trường            | Đồng bộ môi trường giữa local và CI/CD                           |
| Dependabot    | Cảnh báo & cập nhật package   | Bảo mật & cập nhật định kỳ trên GitHub                            |

---

## 📄 04. File cấu hình chính

### `pyproject.toml`

```toml
[tool.poetry]
name = "digital-dso-app"
version = "0.1.0"
description = "Python Clean Architecture App for SKCL Management"
authors = ["DSO Team <team@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.110.0"
uvicorn = "^0.29.0"
sqlalchemy = "^2.0"
pydantic = "^2.0"
python-dotenv = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.1"
black = "^24.3"
flake8 = "^7.0"
isort = "^5.13"
mypy = "^1.9"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
````

### `.env.example`

```env
ENV=development
DATABASE_URL=postgresql://dso_user:password@localhost:5432/dso_db
LOG_LEVEL=INFO
PORT=8000
```

✅ Mỗi developer cần copy `.env.example` thành `.env` và điều chỉnh giá trị riêng.

---

## ⚙️ 05. Hướng dẫn cài đặt & sử dụng

### 🧪 Cài lần đầu

```bash
# Cài Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Cài thư viện dự án
poetry install

# Kích hoạt virtualenv
poetry shell

# Chạy app local
uvicorn src.main:app --reload
```

### 🧼 Format & kiểm tra trước khi commit

```bash
black .
flake8 src/
isort .
mypy src/
pytest
```

---

## 🛡️ 06. Chính sách cập nhật & bảo mật

| Hoạt động         | Tần suất       | Công cụ                       |
| ----------------- | -------------- | ----------------------------- |
| Cập nhật thư viện | 2 tuần/lần     | `poetry update`, `dependabot` |
| Kiểm tra bảo mật  | Mỗi lần PR     | `poetry check` + GitHub CI    |
| Xem gói lỗi thời  | Bất kỳ lúc nào | `poetry show --outdated`      |

---

## 📦 07. Cách thêm thư viện mới

```bash
poetry add <package>               # Thêm vào production
poetry add --group dev <package>  # Thêm vào nhóm dev/test
```

### Ví dụ

```bash
poetry add requests
poetry add --group dev pytest
```

---

## 🔄 08. Môi trường Docker đồng bộ

### `docker/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `docker-compose.yml`

```yaml
services:
  app:
    build:
      context: .
      dockerfile: docker/Dockerfile
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
```

---

## 🔗 09. Liên kết nội dung liên quan

* \[Mục 03 – Tech Stack & Tooling] – Danh sách công nghệ
* \[Mục 07 – Environment Setup] – Hướng dẫn cài đặt local
* \[Mục 10 – CI/CD Pipeline] – Tích hợp poetry trong GitHub Actions

---

📌 *Tài liệu này giúp chuẩn hóa cách làm việc với môi trường Python cho mọi thành viên trong dự án Digital DSO App.*

