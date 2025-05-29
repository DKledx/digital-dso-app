# 📗 Tổng kết Giai đoạn 4 – CI/CD, DB & Release Tag (Ngày 16 → Ngày 20)

🕒 Thời gian: Ngày 16 → Ngày 20  
🎯 Mục tiêu: Tự động hoá toàn bộ quy trình kiểm tra, đo lường, và phát hành sản phẩm bằng GitHub Actions, chuẩn hóa cách đánh version và tracking quality qua coverage, SonarQube, và release tag.

---

## 🧩 Tổng kết các hành động chính

| Ngày    | Hành động                                                      | Ghi chú                                               |
|---------|---------------------------------------------------------------|-------------------------------------------------------|
| 16      | Viết workflow CI phát hành theo Git tag                       | Tự động build khi có tag v*.*.*                       |
| 17      | Tổng hợp tài liệu Giai đoạn 1–2                               | Chuẩn bị base kiến thức cho dev mới                   |
| 18      | Thiết kế bảng initiative, ORM bằng SQLAlchemy, setup Alembic  | Bắt đầu kết nối dữ liệu thật                          |
| 19      | Chuẩn hóa quản lý .env theo từng môi trường                   | Dùng python-dotenv, tách DATABASE_URL, APP_PORT, LOG_LEVEL |
| 20      | Chuẩn bị script release staging theo tag v0.1.0-staging       | Tách rõ flow giữa develop và release tag staging/prod |

---

## ✅ Kết quả đạt được

- Có workflow CI chạy cho branch và CI riêng cho tag release
- Docker image được build khi tag được tạo
- Có file .env.development, .env.staging, .env.production tách biệt
- Hệ thống có DB thật, model ORM, migration đầy đủ
- Mỗi tag release gắn với 1 version cụ thể, có thể trace và rollback
- Sẵn sàng triển khai staging trong môi trường tách biệt

---

## 🎯 Điều học được

- Git tag là công cụ mạnh để quản lý release: main giữ ổn định, develop để dev
- CI/CD cần phân tách test, build, release để tránh lỗi sản xuất
- Quản lý .env động giúp code chạy mọi nơi, không hardcode gì trong repo
- ORM cần migration rõ ràng để history DB không lẫn lộn

---

## 🔧 Vấn đề gặp phải (nếu có)

- Cấu hình alembic ban đầu dễ sai import path nếu chưa thiết lập module
- Việc tách CI thành 2 workflow (ci.yml và release.yml) cần kèm rõ điều kiện trigger
- Khi chuyển DB từ mock → ORM cần chỉnh nhẹ logic cũ trong usecase/repo

---

## 📌 Hành vi tích cực

- Ghi lại tiến trình release, tagging, coverage
- Tự động hóa từ đầu giúp giảm lỗi tay
- Kiểm soát code quality bằng Sonar thay vì “cảm giác”
- Mỗi lần release có changelog, version rõ ràng

---

## 💡 Ý tưởng cải tiến cho giai đoạn sau

- Tích hợp deployment staging tự động (Docker Compose hoặc ArgoCD)
- Tạo Makefile gom lệnh build/lint/test/release
- Tích hợp rollback bản v0.x.x-rollback theo tag

---

## 🔁 Chuẩn bị cho Giai đoạn 5: Testing & Monitoring (Ngày 21–25)

Giai đoạn tới sẽ tập trung viết test tự động mở rộng, đo lường chi tiết coverage, và triển khai monitoring như logging tập trung, alert và trace request.