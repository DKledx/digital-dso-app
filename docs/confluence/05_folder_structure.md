
# 🗂️ Cấu trúc Thư mục và Tổ chức Mã nguồn theo Clean Architecture + Component Layer

## 01. Thông tin tài liệu

- **Tên tài liệu**: Cấu trúc thư mục và tổ chức mã nguồn theo Clean Architecture + Component Layer  
- **Phiên bản**: v1.1  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu cập nhật

- Phân chia theo business domain rõ ràng: mỗi Room là một **Component** độc lập  
- Dễ scale team phát triển: mỗi nhóm phụ trách một component  
- Tách rời logic xử lý riêng biệt, dễ test, dễ triển khai riêng biệt  
- Tuân thủ **Clean Architecture** kết hợp **Modular Monolith**, sẵn sàng microservice hoá khi cần  

---

## 🧱 03. Cấu trúc thư mục tổng thể

```

digital-dso-app/
├── src/
│   ├── components/                        # NEW: tổ chức theo room / domain
│   │   ├── strategy\_room/                 # Component 1
│   │   │   ├── domain/
│   │   │   ├── application/
│   │   │   ├── interface/
│   │   │   └── infrastructure/
│   │   ├── portfolio\_room/               # Component 2
│   │   │   └── ...
│   │   └── initiative\_room/              # Component 3
│   │       └── ...
│   ├── shared/                            # Thành phần dùng chung
│   │   ├── config/
│   │   ├── core/                          # Base class, error handler, constants
│   │   └── utils/
│   ├── main.py
│   └── **init**.py
├── tests/
│   ├── components/
│   └── shared/
├── docker/
│   └── docker-compose.yml
├── .github/
│   └── workflows/
├── pyproject.toml
├── README.md

```

---

## 🧩 04. Giải thích vai trò các tầng trong component

| Tầng           | Vai trò                                    | Ví dụ                                           |
|----------------|---------------------------------------------|--------------------------------------------------|
| components/    | Mỗi Room là 1 đơn vị business độc lập       | `strategy_room`, `initiative_room`              |
| domain/        | Định nghĩa entity, value object, rule       | `Initiative`, `Portfolio`, `TimeFrame`          |
| application/   | Logic xử lý nghiệp vụ (UseCase)             | `CreateInitiativeUseCase`                       |
| interface/     | API, schema, message handler                | `FastAPI Router`, `Streamlit Widget`            |
| infrastructure/| Giao tiếp DB, external system               | `PostgresRepo`, `HTTPClient`                    |
| shared/        | Cấu hình, utils, constants dùng chung       | `logger`, `env`, `base_exception`               |

---

## 🧪 05. Nguyên tắc thiết kế tầng component

| Quy tắc                                 | Diễn giải                                                            |
|-----------------------------------------|----------------------------------------------------------------------|
| Mỗi component có đủ 4 tầng              | Clean Architecture áp dụng riêng trong từng Room                     |
| Không gọi chéo giữa các component       | Giao tiếp thông qua `shared/` hoặc `interface adapter`               |
| Có thể tách thành microservice về sau   | Mỗi component tự xử lý toàn bộ logic nghiệp vụ                       |
| Tên component đặt theo domain nghiệp vụ | Ví dụ: `initiative_room`, `portfolio_room`, `strategy_room`         |

---

## 📦 06. Ví dụ chi tiết cho `initiative_room`

```

components/initiative\_room/
├── domain/
│   ├── entities/
│   │   └── initiative.py
│   └── value\_objects/
│       └── initiative\_status.py
├── application/
│   └── use\_cases/
│       ├── create\_initiative.py
│       └── update\_progress.py
├── interface/
│   ├── rest/
│   │   ├── routers/
│   │   │   └── initiative.py
│   │   └── schemas/
│   │       └── initiative.py
│   └── streamlit\_ui/
│       └── form\_create.py
├── infrastructure/
│   ├── database/
│   │   └── initiative\_repo.py
│   └── external\_services/
│       └── initiative\_forecast\_adapter.py

```

---

## 🔗 07. Liên kết nội dung liên quan

- [Mục 02 – Architecture Vision] – Bản đồ logic theo Clean Architecture  
- [Mục 04 – Clean Code Standards] – Quy tắc đặt tên module, function, class  
- [Mục 10 – CI/CD Pipeline] – Build/test theo từng component  
- [Mục 09 – Testing Guide] – Cấu trúc test theo component tương ứng  

---

📌 *Tài liệu này là hướng dẫn chính thức về tổ chức mã nguồn cho toàn bộ dự án Digital DSO App.*

