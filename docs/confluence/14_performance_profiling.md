# 🎓 Mục 14 – Training & Learning Notes – Digital DSO App

## 01. Thông tin tài liệu

- **Tên tài liệu**: Ghi chú đào tạo và học tập từ dự án  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Ghi lại tiến trình học tập & triển khai theo từng giai đoạn  
- Cập nhật tài liệu, khóa học, best practice  
- Chuẩn hóa checklist học và thử nghiệm công nghệ mới  
- Làm nền tảng nhân bản đội ngũ & training nội bộ  

---

## 📘 03. Tổng hợp học phần đã áp dụng

| Chủ đề          | Nội dung học được                                | Ứng dụng thực tế                        |
|------------------|---------------------------------------------------|------------------------------------------|
| Clean Architecture | Tách tầng domain/use case/interface/infrastructure | Cấu trúc repo theo component             |
| Clean Code        | Hàm nhỏ, đặt tên rõ, tránh nested logic         | Rule [Mục 04]                            |
| FastAPI           | API async, schema validation                    | Triển khai toàn bộ router                |
| Pydantic          | Schema input/output                             | Tạo file trong `schemas/`                |
| SQLAlchemy        | ORM + session + repository pattern              | `initiative_repo.py`, test repo          |
| Poetry            | Quản lý dependency, build                       | `pyproject.toml`                         |
| Docker            | Tái tạo môi trường dev                          | `docker-compose.yml`                    |
| CI/CD             | Build, test, lint                                | `ci.yml`                                 |
| GitOps            | Release theo tag                                | `release.yml` + tag `v1.0.0`             |
| Logging           | Structured log, gắn request_id                  | `logger.py`, `RequestIdMiddleware`       |
| Unit Test         | Kiểm thử use case, logic                        | `test_create_initiative.py`             |
| Integration Test  | Giả lập API call                                | `test_get_initiative_api.py`            |

---

## 📚 04. Danh sách tài nguyên học tập

| Chủ đề            | Tài liệu                  | Link                                        |
|--------------------|----------------------------|---------------------------------------------|
| Clean Architecture | Uncle Bob Blog            | [Clean Coder](https://blog.cleancoder.com) |
| FastAPI            | Docs chính thức           | [FastAPI](https://fastapi.tiangolo.com)    |
| Pytest             | Plugin + hướng dẫn        | [Pytest Docs](https://docs.pytest.org)     |
| GitHub Actions     | CI/CD workflow            | [GitHub Actions](https://docs.github.com/actions) |
| Docker & Compose   | Volume, mạng, build       | [Docker Docs](https://docs.docker.com)     |
| GitOps & ArgoCD    | Workshop căn bản          | [ArgoCD](https://argo-cd.readthedocs.io)   |
| Prometheus         | Monitoring & metrics      | [Prometheus](https://prometheus.io/docs)   |

---

## 📝 05. Bài học rút ra theo giai đoạn

### 🔹 Giai đoạn 1: Setup ban đầu

- ⚠️ Poetry dễ xung đột system Python → nên cài độc lập  
- ✅ Tách tầng sớm → onboarding nhanh  
- 🔍 Setup logger sớm → trace logic trong lúc dev

### 🔹 Giai đoạn 2: Tạo Epic đầu tiên

- ✅ BRD rõ → code nhanh, ít vòng sửa  
- 🔁 Chia component theo Room dễ scale  
- ⚠️ Cần tích hợp `coverage` từ đầu để theo dõi test

### 🔹 Giai đoạn 3: CI/CD + GitOps

- ✅ Squash merge giúp lịch sử clean  
- ⚠️ Pin version Docker base để tránh bug ngẫu nhiên  
- ✅ Release theo tag rất ổn định khi deploy staging

---

## ✅ 06. Checklist đào tạo nội bộ

| Kỹ năng               | Mức độ yêu cầu | Tài liệu liên quan                |
|------------------------|----------------|-----------------------------------|
| Git + GitHub Flow      | Bắt buộc        | [Mục 08]                          |
| FastAPI + Pydantic     | Bắt buộc        | [Mục 03], [Mục 04]                |
| Clean Code / Arch      | Bắt buộc        | [Mục 01–05]                       |
| Docker Compose         | Trung bình      | [Mục 06], [Mục 07]                |
| CI/CD + GitOps         | Nâng cao        | [Mục 10], [Mục 11]                |
| Monitoring + Logging   | Tuỳ chọn        | [Mục 13]                          |

---

## 📂 07. Cấu trúc thư mục `learning/` (đề xuất)

```plaintext
learning/
├── week01_clean_code.md
├── week02_fastapi_usecase.md
├── week03_ci_cd_pipeline.md
├── week04_gitops_tagging.md
└── summary_checklist.md
````

---

## 🔗 08. Liên kết nội dung liên quan

* \[Mục 01 – Project Overview] – Tổng quan skill và kiến trúc
* \[Mục 08 – Feature Dev Flow] – Template BRD + Checklist dev
* \[Mục 15 – Appendix] – Template học, cấu hình mẫu

---

### Gợi ý hành động tiếp theo

1. **Tạo thư mục `learning/`** lưu các ghi chú theo tuần hoặc chủ đề.
2. **Khởi động mô hình Tech Friday** – mỗi dev chia sẻ 1 chủ đề/ngày.
3. **Tạo sheet tổng hợp kỹ năng + độ tự tin** của từng thành viên.
4. **Gắn Mục 14 này lên dashboard Confluence** để theo dõi hành trình học tập.
5. **Tạo `week01_clean_code.md`** và template chuẩn hóa để triển khai nội dung đầu tiên.

---

🧠 *Học tập là một hành trình liên tục. Việc ghi chép – phản tư – nhân bản giúp tăng tốc năng lực tập thể theo chiều sâu.*

