# 🚀 Quy trình Thiết kế và Phát triển Tính năng

## 01. Thông tin tài liệu

- **Tên tài liệu**: Quy trình thiết kế và phát triển tính năng  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Chuẩn hoá cách phát triển một tính năng trong dự án  
- Từ BRD → Git branch → Code → Test → Pull Request → Release  
- Gắn kết chặt giữa business logic – technical implementation – test  
- Dễ dàng chia việc theo từng component (Room)  

---

## 🔄 03. Luồng phát triển tính năng

```mermaid
graph TD
  BRD[Viết BRD User Story] --> Branch[Tạo nhánh Git riêng]
  Branch --> Dev[Phát triển tính năng]
  Dev --> Test[Viết Unit + Integration Test]
  Test --> PR[Pull Request lên GitHub]
  PR --> Review[Code Review + CI Pass]
  Review --> Merge[Merge vào nhánh main/staging]
  Merge --> Deploy[Release staging]
````

---

## 🧾 04. Cấu trúc BRD / User Story

| Trường             | Nội dung mẫu                                                             |
| ------------------ | ------------------------------------------------------------------------ |
| Epic               | `EPIC-INIT-001 – Quản lý danh sách SKCL`                                 |
| User Story         | Khi tôi là **deliver manager**, tôi muốn **xem danh sách SKCL theo quý** |
| Input/Output       | Filter theo quý, đơn vị; xuất danh sách SKCL                             |
| Rule               | Chỉ hiển thị các SKCL đã được phê duyệt đề cương                         |
| Tài liệu liên quan | Mockup, Schema, API Contract (liên kết Confluence hoặc thư mục feature)  |

---

## 🌿 05. Quy ước đặt tên nhánh Git

```bash
# Cú pháp: loại / component / chức năng
feat/initiative/add-benefit-tracking
fix/portfolio/filter-quarter
test/strategy/okr-view
refactor/initiative/domain-cleanup
```

---

## 📁 06. Cấu trúc thư mục feature (ví dụ theo `initiative_room`)

```
components/
└── initiative_room/
    ├── domain/
    │   └── entities/initiative.py
    ├── application/
    │   └── use_cases/add_benefit.py
    ├── interface/
    │   ├── rest/routers/initiative.py
    │   └── schemas/initiative.py
    ├── infrastructure/
    │   └── database/initiative_repo.py

tests/
└── components/initiative_room/test_add_benefit.py
```

---

## 🧪 07. Checklist Phát triển Tính năng

* ✅ Viết BRD rõ ràng, gắn rule nghiệp vụ
* ✅ Tạo schema input/output với Pydantic
* ✅ Viết use case + test logic unit
* ✅ Viết router/API + test endpoint
* ✅ Format code: `black`, `isort`, `flake8`, `mypy`
* ✅ Tạo Pull Request và link tới issue/Epic
* ✅ Viết ít nhất 2 test: success + fail case

---

## 📂 08. Template Pull Request (PR)

```markdown
### 🎯 Mục tiêu
Thêm tính năng theo `EPIC-INIT-001`: theo dõi lợi ích từng SKCL

### 🧱 Thay đổi chính
- Thêm use case `AddBenefitTracker`
- API `POST /initiative/{id}/benefit`
- Test coverage đạt 92%

### ✅ Checklist
- [x] Đã test local
- [x] Đã viết unit + integration test
- [x] CI pass
- [x] Review 1/2 OK
```

---

## 🔗 09. Liên kết nội dung liên quan

* \[Mục 01 – Project Overview] – Danh sách EPIC
* \[Mục 05 – Folder Structure] – Tổ chức file theo component
* \[Mục 09 – Testing Guide] – Cách viết và tổ chức test
* \[Mục 12 – Code Review & Merge] – Chính sách review/merge

---

📌 *Tài liệu này là xương sống để đảm bảo quy trình phát triển tính năng có chất lượng, logic và kiểm thử rõ ràng.*
