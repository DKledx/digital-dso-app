
# 🧰 Danh mục Công nghệ và Công cụ Sử dụng

## 01. Thông tin tài liệu

- **Tên tài liệu**: Danh mục công nghệ và công cụ sử dụng  
- **Phiên bản**: v2.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Chuẩn hóa toàn bộ công nghệ sử dụng trong dự án **Digital DSO App**
- Đảm bảo đồng bộ codebase, tooling, CI/CD và khả năng scale
- Ưu tiên công nghệ: dễ học, hiện đại, DevOps-ready, hỗ trợ Clean Architecture và Modular Design
- Hỗ trợ kiểm tra chất lượng, bảo mật, kiểm thử, phát hành tự động

---

## 📦 03. Bảng tổng hợp Tech Stack chính

| Nhóm công cụ   | Thành phần             | Công nghệ                  | Ghi chú                                           |
|----------------|------------------------|----------------------------|---------------------------------------------------|
| **Ngôn ngữ**   | Core Language          | Python 3.11                | Async friendly, phổ biến, dễ học                  |
| **Backend**    | API Framework          | FastAPI                    | Chuẩn OpenAPI, async-native, auto docs           |
|                | ORM                    | SQLAlchemy 2.x             | Tương thích Clean Architecture                    |
|                | Validation             | Pydantic 2.x               | Tách schema input/output rõ ràng                 |
| **Frontend**   | UI demo                | Streamlit                  | Dễ build prototype nhanh                         |
| **Database**   | RDBMS                  | PostgreSQL                 | Tương thích ORM và công cụ BI                    |
| **Dev Env**    | Dependency Manager     | Poetry                     | Quản lý lock + pyproject.toml                    |
|                | Environment            | .env, dotenv               | Quản lý biến môi trường local + CI              |
| **Container**  | Runtime                | Docker + Docker Compose    | Chuẩn hóa môi trường dev/test/deploy             |
| **Testing**    | Unit + Integration     | Pytest + Factory Boy       | Kết hợp với coverage, test async tốt             |
| **Static**     | Format & Lint          | Black, isort, flake8, mypy | Tự động kiểm tra style, type, import             |
| **Code Quality**| Static Code Analysis  | SonarQube / SonarCloud     | Kiểm tra code smells, security, duplication      |
| **CI/CD**      | Pipeline Engine        | GitHub Actions             | Tự động hóa build, test, sonar, release          |
|                | Registry               | GitHub Container Registry  | Push Docker image theo version/tag               |
|                | Release Deploy         | Git Tag + ArgoCD (option)  | GitOps, cập nhật YAML staging theo tag           |
| **Monitoring** | Logging                | Python logging + RequestID | Ghi log chuẩn, trace xuyên suốt request          |
|                | Error Tracking         | Sentry (optional)          | Theo dõi exception theo component                |
|                | Metrics                | Prometheus + Grafana       | Theo dõi API latency, error rate (optional)      |

---

## 🛠 04. Chính sách chọn công nghệ

| Tiêu chí                  | Mục tiêu                                                  |
|---------------------------|-----------------------------------------------------------|
| Clean Architecture        | Dễ tách tầng, test, maintain                              |
| Modular                   | Hỗ trợ component-based structure theo Room               |
| DevOps ready              | Có thể tích hợp CI/CD, logging, metrics                   |
| Learning friendly         | Tài liệu tốt, cộng đồng hỗ trợ mạnh                       |
| Security-aware            | Hỗ trợ kiểm tra lỗ hổng qua SonarQube                    |
| Scalable                  | Có thể mở rộng từ MVP → production với ít thay đổi        |

---

## 🧪 05. Cách cài đặt & sử dụng

### Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry install
poetry shell
````

### Docker

```bash
docker-compose up --build
```

### SonarQube (optional)

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube
```

* Kết nối với GitHub Actions bằng `SONAR_TOKEN` trong secrets

---

## 🧭 06. Tool hỗ trợ mở rộng / đào tạo

| Nhóm       | Công cụ                 | Mục tiêu                                     |
| ---------- | ----------------------- | -------------------------------------------- |
| Onboarding | Confluence              | Lưu trữ 15 mục tài liệu, dashboard kiến trúc |
| Review     | GitHub PR + SonarQube   | Đánh giá chất lượng PR trước khi merge       |
| Học tập    | Markdown + weekly notes | Tạo thư mục `learning/`, ghi lại theo tuần   |
| Template   | `folder templates/`     | Dùng lại file BRD, PR, UseCase, Test mẫu     |

---

## 🔗 07. Liên kết nội dung liên quan

* \[Mục 02 – Architecture Vision] – Kiến trúc modular theo Room
* \[Mục 05 – Folder & File Structure] – Tổ chức source theo component
* \[Mục 10 – CI/CD Pipeline] – Tích hợp poetry + sonar + test
* \[Mục 15 – Template] – File `sonar-project.properties`, script docker, test mẫu

---

📌 *Tài liệu này là phần lõi trong bộ hướng dẫn triển khai & vận hành Digital DSO App.*
