# 📊 Coverage Report – Digital DSO App

| Component              | Coverage (%) | Ghi chú                                 |
|------------------------|--------------|------------------------------------------|
| initiative_room        | 87%          | Đầy đủ unit & integration test           |
| shared/core/logger     | 95%          | Đã test middleware & log lỗi cơ bản      |
| shared/core/config     | 100%         | Config env + default fallback test tốt   |
| shared/core/db         | 75%          | Chưa test fail khi DB lỗi                |
| main.py                | -            | Không test vì không có logic nghiệp vụ   |

> Target coverage toàn hệ thống: **>= 85%**