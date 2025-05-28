📅 Ngày 16 – 14/06/2025  
🔹 Hành động chính:
- Viết workflow `release.yml` chạy khi có tag `v*.*.*`
- Build Docker image với tag tương ứng
- Tạo tag v0.1.1 để test CI/CD phát hành
🔸 Ghi chú:
- Git tag = signal để phát hành → CI sẽ không tự chạy nếu chỉ push code
- Cấu hình đúng ref `${GITHUB_REF##*/}` để lấy version tag
💡 Nhận định:
- Từ giờ mỗi lần merge lên main → tạo tag → tự build, tự deploy
- Đây là triết lý GitOps: control = tag, tracking = CI
