# 🚀 Digital DSO App

Hệ thống quản lý danh mục Sáng Kiến Chiến Lược (SKCL), xây dựng theo **Clean Architecture**, **Component-based**, sẵn sàng DevOps và CI/CD.

---

## 📦 Tech Stack

- **Python 3.11**
- **FastAPI** (API backend)
- **Pydantic** (Schema/Validation)
- **SQLAlchemy** (ORM)
- **Poetry** (Dependency management)
- **Docker** (Containerization)
- **GitHub Actions** (CI/CD)
- **SonarQube/SonarCloud** (Code Quality & Coverage)
- **PostgreSQL** (coming soon)

---

## 🧱 Kiến trúc thư mục (Clean Architecture)

```
src/
├── components/
│   ├── initiative_room/
│   │   ├── application/    # UseCase, business logic
│   │   ├── domain/         # Entity, domain model
│   │   ├── infrastructure/ # Repository, external service
│   │   └── interface/      # API router, schema, controller
│   ├── strategy_room/
│   └── portfolio_room/
├── shared/                 # Common utils, config, core
tests/                      # Unit & integration tests
.github/workflows/          # CI/CD pipelines
```

- **Component-based:** Mỗi Room là một module độc lập, dễ mở rộng, dễ test.
- **Clean Architecture:** Tách biệt rõ ràng giữa domain, usecase, interface, infrastructure.

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

## 🧪 Kiểm thử & Coverage

- **Chạy test:**  
  ```bash
  poetry run pytest
  ```
- **Kiểm tra coverage:**  
  ```bash
  poetry run pytest --cov=src --cov-report=xml
  ```
  Kết quả coverage sẽ lưu tại `coverage.xml`.

---

## 🤖 CI/CD & Code Quality

![CI](https://github.com/DKledx/digital-dso-app/actions/workflows/ci.yml/badge.svg)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=digital-dso-app&metric=coverage)](https://sonarcloud.io/summary/new_code?id=digital-dso-app)

- **CI/CD:** Tự động lint, test, đo coverage trên mọi push/pull request (GitHub Actions).
- **SonarQube/SonarCloud:** Theo dõi chất lượng code, coverage, bug, code smell.
- **TODO:** Đang tạm thời comment kiểm tra Black/isort trong CI, sẽ chuẩn hóa lại sau.

---

## 🚦 Quy trình phát triển

1. **Mỗi tính năng lớn tạo branch feature/**.
2. **Commit code nhỏ, rõ ràng, thường xuyên.**
3. **Viết test cho từng usecase và API.**
4. **Kiểm tra CI/CD pass trước khi merge.**
5. **Đảm bảo coverage và chất lượng code qua SonarQube.**

---

## ✅ Roadmap

- [x] Setup base structure
- [x] Poetry + Docker
- [x] Viết module Initiative Room
- [x] CI/CD (GitHub Actions)
- [x] Test & Coverage
- [ ] SonarQube tích hợp
- [ ] Release Staging

---

## 📘 Kết thúc Giai đoạn 1: Khởi tạo hệ thống

| Hạng mục                  | Trạng thái |
|-------------------------  |:----------:|
| GitHub repo & branch      | ✅         |
| Clean folder structure    | ✅         |
| Poetry, env, docker setup | ✅         |
| Chạy thử app              | ✅         |
| README, tag milestone     | ✅         |

---

## 📘 Tài liệu kỹ thuật
- [Changelog](CHANGELOG.md)

## 📚 Tài liệu tham khảo

- [Clean Architecture (Uncle Bob)](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Poetry Docs](https://python-poetry.org/docs/)
- [SonarCloud Docs](https://docs.sonarcloud.io/)