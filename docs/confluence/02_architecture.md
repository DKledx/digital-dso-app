
# 🏗️ Kiến trúc hệ thống Digital DSO App – Mô hình Component-centric Clean Architecture

## 01. Thông tin chung

- **Tên tài liệu**: Kiến trúc hệ thống Digital DSO App – mô hình Component-centric Clean Architecture  
- **Phiên bản**: v2.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: Solution Architect / Head of DSO  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu kiến trúc cập nhật

- Tổ chức kiến trúc xoay quanh component/domain theo từng **Room**, thay vì tập trung vào tầng kỹ thuật
- Mỗi Room là một component độc lập, dễ phân quyền phát triển, kiểm thử và mở rộng
- Vẫn duy trì nguyên tắc **Clean Architecture** bên trong mỗi component (tách `domain`, `use_case`, `interface`, `infrastructure`)
- Hướng tới kiến trúc **Modular Monolith**, có thể tách dần thành Microservice nếu cần

---

## 🧱 03. Cấu trúc thư mục theo Component-based Clean Architecture

```

src/
├── components/
│   ├── strategy\_room/
│   ├── portfolio\_room/
│   └── initiative\_room/
├── shared/
│   ├── config/
│   ├── core/
│   └── utils/
├── main.py

```

Mỗi component (Room) có cấu trúc:

```

components/\<room\_name>/
├── domain/
├── application/
├── interface/
└── infrastructure/

````

---

## 🔄 04. Sơ đồ kiến trúc tổng quan

```mermaid
flowchart TD
  subgraph Shared Layer
    Config[shared.config]
    Utils[shared.utils]
  end

  subgraph Component: Initiative Room
    IR_UI[Streamlit UI]
    IR_API[FastAPI Router]
    IR_UseCase[Use Cases]
    IR_Entity[Entities]
    IR_Infra[PostgreSQL, External API]
  end

  IR_UI --> IR_API --> IR_UseCase --> IR_Entity --> IR_Infra
  IR_UseCase --> SharedLayer[shared.config/shared.utils]
````

---

## 🧩 05. Vai trò từng tầng trong một component

| Tầng            | Mô tả                                      | Ví dụ                                          |
| --------------- | ------------------------------------------ | ---------------------------------------------- |
| domain/         | Định nghĩa Entity và Business Rule cốt lõi | Initiative, Portfolio, Quarter                 |
| application/    | Các UseCase thực hiện hành vi nghiệp vụ    | CreateInitiativeUseCase, UpdateProgressUseCase |
| interface/      | Giao tiếp API hoặc UI                      | initiative\_router.py, initiative\_form.py     |
| infrastructure/ | Giao tiếp DB hoặc dịch vụ ngoài            | initiative\_repo.py, external\_benefit\_api.py |

---

## 🧠 06. Tại sao chọn kiến trúc này?

| Tiêu chí                      | Giải thích                                            |
| ----------------------------- | ----------------------------------------------------- |
| 🧱 Modular hóa theo domain    | Mỗi Room là một module độc lập, có thể dev/test riêng |
| 🧼 Tách tầng rõ ràng          | Vẫn giữ Clean Architecture trong từng Room            |
| 📦 Khả năng mở rộng           | Dễ chia đội, scale, tách sang microservice khi cần    |
| 🔁 Dễ bảo trì                 | Chỉnh sửa logic không ảnh hưởng các Room khác         |
| ⚙️ Tương thích CI/CD + GitOps | Tách pipeline hoặc deploy theo component dễ dàng      |

---

## 🔄 07. Luồng xử lý ví dụ: Tạo mới SKCL

```mermaid
sequenceDiagram
  actor User
  participant UI as Streamlit
  participant API as FastAPI Router
  participant UC as CreateInitiativeUseCase
  participant DB as InitiativeRepository

  User->>UI: Điền form tạo SKCL
  UI->>API: POST /initiative
  API->>UC: validate + execute
  UC->>DB: Save to PostgreSQL
  API->>UI: Trả về kết quả thành công
```

---

## 📚 08. Nguyên tắc kiến trúc áp dụng

| Nguyên tắc                    | Ý nghĩa                                                            |
| ----------------------------- | ------------------------------------------------------------------ |
| Screaming Architecture        | Cấu trúc thư mục phản ánh domain (strategy, portfolio, initiative) |
| Tách biệt IO với logic        | `interface/` không chứa nghiệp vụ                                  |
| Không cross-call component    | Chỉ giao tiếp qua `shared/` hoặc qua event trung gian              |
| Entity độc lập framework      | Không phụ thuộc FastAPI hoặc SQLAlchemy                            |
| UseCase không phụ thuộc infra | Chỉ nhận repo thông qua interface injection                        |

---

## 🔗 09. Liên kết nội dung liên quan

* \[Mục 01 – Project Overview] – Bản đồ Room và chức năng
* \[Mục 03 – Tech Stack & Tooling] – Framework hỗ trợ kiến trúc này
* \[Mục 05 – Folder & File Structure] – Tổ chức code theo component
* \[Mục 10 – CI/CD Pipeline] – Tự động hoá kiểm thử từng Room

---

📌 *Tài liệu này hỗ trợ cả việc học tập và triển khai thực chiến Digital DSO App tại F88 hoặc mô hình tương đương.*


