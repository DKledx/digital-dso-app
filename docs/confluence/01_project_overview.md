
# 📘 Digital DSO App – Dashboard Tài liệu

## 01. Thông tin Dự án

- **Tên dự án**: Digital DSO App – Python Clean Architecture Learning Project  
- **Phiên bản**: v1.0  
- **Ngày tạo**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  
- **Cập nhật lần cuối**: May 25, 2025  

## 02. Mục tiêu Chính

- Học & thực hành Clean Architecture
- Chuẩn hóa CI/CD pipeline
- Xây dựng sản phẩm thực chiến
- Tài liệu hoá & nhân bản dễ dàng

## 03. Phạm vi Chức năng (Functional Scope)

| Room            | Mô tả chức năng                                               |
|-----------------|---------------------------------------------------------------|
| Strategy Room   | Quản lý chiến lược, gắn OKR, phân bổ danh mục SKCL            |
| Portfolio Room  | Quản lý danh mục sáng kiến theo quý, theo đơn vị              |
| Initiative Room | Quản lý từng SKCL cụ thể: đề cương, tiến độ, rủi ro, lợi ích  |

## 04. Học phần kỹ thuật áp dụng

- **Clean Code**: Viết code Python rõ ràng, tách hàm hợp lý, không để lại "mùi code"
- **Clean Architecture**: Phân tầng chuẩn Domain → Application → Adapter → Framework
- **CI/CD**: Tự động kiểm tra code, test, build container, release staging
- **GitOps (Option)**: Quản lý release theo tag, mô phỏng ArgoCD
- **Test Automation**: Viết test case cho use case, logic xử lý

## 05. Tài liệu & Kho lưu trữ

- 🗃️ GitHub Repo: [Link GitHub Repository]
- 📖 Tài liệu Confluence: Trang hiện tại
- 🧪 Giao diện demo: [Link Streamlit hoặc localhost nếu có]
- 🎓 Ghi chú học tập: [Link Mục 14]

## 06. Định hướng mở rộng

| Hướng mở rộng             | Chi tiết                                                        |
|---------------------------|------------------------------------------------------------------|
| Kết nối real data         | PostgreSQL thật hoặc Google Sheets                              |
| Mở rộng sang app mobile   | Flutter / React Native demo mobile monitoring SKCL              |
| Triển khai production     | Gắn domain cụ thể của F88                                       |
| Phân hệ lợi ích mang lại  | Theo dõi ROI theo quý của từng SKCL                             |

## 07. Product Map


Digital DSO App
├── Strategy Room
│   ├── OKR Viewer
│   ├── Chiến lược theo năm
├── Portfolio Room
│   ├── Danh mục theo quý
│   ├── Gắn đơn vị phụ trách
└── Initiative Room
├── Quản lý đề cương
├── Báo cáo tiến độ Sprint
├── Theo dõi lợi ích
├── Quản lý rủi ro, vấn đề



## 08. Danh sách EPIC bắt đầu phát triển

| Mã Epic | Tên Epic                          | Room       | Ghi chú          |
|--------|-----------------------------------|------------|------------------|
| EPIC-1 | Giao diện xem danh sách SKCL      | Portfolio  | Dữ liệu giả lập  |
| EPIC-2 | Thêm SKCL mới + phê duyệt         | Initiative | Form đầu vào     |
| EPIC-3 | Xem đề cương SKCL                 | Initiative | Mẫu A1           |
| EPIC-4 | Giao diện quản lý tiến độ Sprint  | Initiative | Giao tiếp API    |

