# 🚀 Digital DSO App

Hệ thống quản lý danh mục Sáng Kiến Chiến Lược (SKCL), được xây dựng theo kiến trúc Clean Code, Component-based Architecture, và DevOps-ready.

---

## 📦 Tech Stack

- Python 3.11
- FastAPI, Pydantic, SQLAlchemy
- Poetry, Docker, GitHub Actions
- SonarQube (coming)
- PostgreSQL (coming)

---

## 🧱 Kiến trúc thư mục

```
src/
├── components/
│   ├── initiative_room/
│   ├── strategy_room/
│   └── portfolio_room/
├── shared/
tests/
```

---

## ▶️ Cách chạy (Local)

```bash
poetry install
poetry run uvicorn src.main:app --reload
```

---

## 🐳 Cách chạy (Docker)

```bash
cp .env.example .env
docker compose up --build
```

---

## ✅ Roadmap

- Setup base structure
- Poetry + Docker
- Viết module Initiative Room
- CI/CD + Sonar + Test
- Release Staging

---

## 📊 Badge (placeholder)

![CI](https://img.shields.io/badge/ci-passing-brightgreen)  
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

---

## 📅 Nhật ký phát triển

### Ngày 1 – 25/05/2025  
- Khởi tạo repo, nhánh main/develop, mô tả ban đầu

### Ngày 2 – 26/05/2025  
- Thiết lập cấu trúc thư mục component-based

### Ngày 3 – 27/05/2025  
- Poetry, pyproject.toml, FastAPI Hello World

### Ngày 4 – 28/05/2025  
- Dockerfile, docker-compose, .env.example

### Ngày 5 – 29/05/2025  
- Viết README chuẩn, mô tả kiến trúc, tech stack, hướng dẫn
- Gắn badge CI và coverage (placeholder)
- Merge develop → main, tạo tag v0.0.1

---

## 🧠 Nhật ký gợi ý hôm nay

📅 Ngày 5 – 29/05/2025  
🔹 **Hành động chính:**  
- Viết README đầy đủ: mô tả hệ thống, hướng dẫn chạy, kiến trúc  
- Gắn badge CI và coverage (tạm placeholder)  
- Merge develop → main, tạo tag v0.0.1  

🔸 **Khó khăn:**  
- [ghi nếu có]  

📌 **Ghi chú học được:**  
- README rõ ràng giúp team mới onboard rất nhanh  
- Gắn tag version giúp chuẩn bị cho CI/CD tự động  

---

## 📘 Kết thúc Giai đoạn 1: Khởi tạo hệ thống

| Hạng mục                  | Trạng thái |
|-------------------------  |:----------:|
| GitHub repo & branch      | ✅         |
| Clean folder structure    | ✅         |
| Poetry, env, docker setup | ✅       |
| Chạy thử app              | ✅         |
| README, tag milestone     | ✅         |

---

