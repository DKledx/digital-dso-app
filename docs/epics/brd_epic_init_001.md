# 📄 BRD – EPIC-INIT-001: Tạo mới SKCL

## 🎯 Mục tiêu nghiệp vụ
Giúp Deliver Manager tạo mới Sáng Kiến Chiến Lược (SKCL), lưu trữ đầy đủ thông tin cần thiết để quản lý, theo dõi và phân loại.

## 🧩 Mô tả chức năng
Người dùng (quản lý sáng kiến) tạo mới 1 SKCL qua form hoặc API. SKCL sẽ có trạng thái khởi tạo là `"draft"` và có thể chỉnh sửa sau đó.

## ✅ Business Rules
- Trường `name` là bắt buộc và duy nhất trong mỗi quý
- `quarter` có định dạng: `Q1/2025`, `Q2/2025`, v.v.
- `owner_unit` phải nằm trong danh sách đơn vị được phép tạo sáng kiến
- Trạng thái khởi tạo: `"draft"`

## 🧱 Data Schema

### Request (InitiativeCreateRequest)
```json
{
  "name": "Triển khai hệ thống DSO",
  "description": "Xây dựng nền tảng quản lý chiến lược",
  "quarter": "Q3/2025",
  "owner_unit": "DSO",
  "expected_outcome": "Giao diện MVP, quản lý danh mục"
}
```

### Response (InitiativeCreateResponse)
```json
{
  "id": 123,
  "status": "draft",
  "created_at": "2025-06-01T08:00:00"
}
```

## 🔁 Luồng xử lý (sequence)
1. Người dùng gửi request tạo mới
2. Hệ thống validate input theo rule
3. Tạo bản ghi mới vào DB
4. Trả về ID + trạng thái "draft"

## 🔗 Liên kết tài liệu
- Mục 08 – Feature Dev Flow
- Mục 05 – Folder Structure (initiative_room/application/)
- Mục 09 – Testing
- Mục 14 – Learning Note (tuần viết usecase đầu tiên)

## 📦 Output liên quan
- File schema: `initiative_schemas.py`
- Use case: `create_initiative_usecase.py`
- Test: `test_create_initiative.py`