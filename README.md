# Digital DSO App

Hệ thống mẫu triển khai kiến trúc Clean Code, Component-based Architecture, CI/CD và GitOps để quản lý danh mục Sáng Kiến Chiến Lược (SKCL) tại F88.

---

## 📅 Nhật ký phát triển

### Ngày 1 – 25/05/2025  
🔹 **Hành động chính:**  
- Tạo repo `digital-dso-app` trên GitHub  
- Thiết lập nhánh `main` + `develop`  
- Bổ sung `.gitignore` cho Python/Poetry  
- Viết mô tả ban đầu vào `README.md`  

🔸 **Khó khăn:**  
- [ghi vào nếu có]  

📌 **Ghi chú học được:**  
- GitHub hỗ trợ `.gitignore` theo ngôn ngữ  
- Việc chia `main`/`develop` giúp tách sản phẩm ổn định & môi trường phát triển  
- Thử Copilot agent trên Vscode - khá bất ngờ

## 📁 Folder Structure – Component-based Clean Architecture

```
src/
├── components/
│   ├── initiative_room/
│   │   ├── domain/
│   │   ├── application/
│   │   ├── interface/
│   │   └── infrastructure/
│   ├── portfolio_room/
│   │   ├── domain/
│   │   ├── application/
│   │   ├── interface/
│   │   └── infrastructure/
│   └── strategy_room/
│       ├── domain/
│       ├── application/
│       ├── interface/
│       └── infrastructure/
├── shared/
│   ├── config/
│   ├── core/
│   └── utils/
├── main.py
tests/
└── components/
    ├── initiative_room/
    ├── portfolio_room/
    └── strategy_room/
```

- Mỗi Room là một Component có đủ các tầng: `domain`, `application`, `interface`, `infrastructure`
- `shared/` chứa cấu hình, base class, helper function
- `tests/` tổ chức song song với `src/components/`

## 🧠 Nhật ký gợi ý hôm nay

📅 Ngày 2 – 26/05/2025  
🔹 **Hành động chính:**  
- Thiết lập cấu trúc thư mục theo từng Room (component)  
- Tạo `__init__.py` để Python nhận diện package  
- Cập nhật mô tả kiến trúc trong README  

🔸 **Khó khăn:**  
- [ghi vào nếu có]  

📌 **Ghi chú học được:**  
- Cấu trúc component giúp chia nhỏ team, module hóa logic  
- `__init__.py` cần thiết để test và import hoạt động ổn định

