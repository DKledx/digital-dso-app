# 🚀 Quy trình Phát hành và Triển khai Ứng dụng theo GitOps – Digital DSO App

## 01. Thông tin tài liệu

- **Tên tài liệu**: Quy trình phát hành và triển khai ứng dụng theo GitOps  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Áp dụng mô hình GitOps: triển khai được kiểm soát qua Git tag / GitHub Release  
- Phân tách rõ ràng giữa CI (build, test) và CD (release, deploy)  
- Mỗi bản phát hành có thể **rollback nhanh**, theo dõi được qua version  
- Chuẩn bị sẵn sàng cho tích hợp ArgoCD hoặc FluxCD  

---

## 🧭 03. Tổng quan Quy trình GitOps

```mermaid
graph LR
  Code[Push code] --> PR[Pull Request]
  PR --> Merge[Merge vào main]
  Merge --> Tag[Git Tag v1.0.0]
  Tag --> Release[Trigger CI/CD release]
  Release --> Build[Build & Push Docker Image]
  Build --> Deploy[Trigger Deploy Staging/Prod]
````

---

## 🏷️ 04. Chính sách Version & Tag

| Mức    | Ý nghĩa                 | Ví dụ    |
| ------ | ----------------------- | -------- |
| v1.0.0 | Major release / staging | `v1.0.0` |
| v1.0.1 | Bug fix nhỏ             | `v1.0.1` |
| v1.1.0 | Thêm tính năng mới      | `v1.1.0` |

✅ Format tag bắt buộc: `v<major>.<minor>.<patch>`

---

## 🐳 05. Quy trình Deploy Staging (Tag → Docker → Deploy)

Khi bạn push một tag như `v1.1.0`, GitHub sẽ:

1. Build Docker image từ source code
2. Push image lên **GitHub Container Registry** (GHCR)
3. Trigger cập nhật YAML tại repo `infra-deployments`
4. (Nếu dùng ArgoCD) → Tự động đồng bộ staging/prod từ YAML

---

## 📂 06. Cấu trúc Triển khai GitOps (Mô phỏng)

```
infra-deployments/
├── environments/
│   ├── staging/
│   │   └── digital-dso-app.yaml
│   └── production/
│       └── digital-dso-app.yaml
├── kustomization.yaml
└── README.md
```

### `digital-dso-app.yaml` ví dụ

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: digital-dso-app
spec:
  template:
    spec:
      containers:
        - name: app
          image: ghcr.io/your-org/digital-dso-app:v1.1.0
```

---

## 🤖 07. Tự động hóa qua GitHub Actions

Trong `release.yml`:

```yaml
on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  release-and-deploy:
    steps:
    - name: Build & Push Image
      # dùng docker/build-push-action (xem tài liệu CI/CD)

    - name: Bump deployment YAML (optional)
      run: |
        sed -i "s|image: .*|image: ghcr.io/your-org/digital-dso-app:${{ github.ref_name }}|" environments/staging/digital-dso-app.yaml
        git config user.name "github-actions"
        git config user.email "actions@github.com"
        git commit -am "Update staging to ${{ github.ref_name }}"
        git push
```

---

## 📦 08. Thực hành Release

```bash
# Kiểm tra trước khi release
poetry run pytest && black . && flake8

# Tạo tag release
git tag v1.1.0
git push origin v1.1.0
```

👉 GitHub sẽ tự động:

* Build image
* Publish GHCR
* Trigger cập nhật YAML hoặc ArgoCD

---

## 🛡️ 09. Rollback (khi cần)

| Cách                     | Hành động                                    |
| ------------------------ | -------------------------------------------- |
| Tạo hotfix               | Tạo tag `v1.1.1-fix`                         |
| Quay về version ổn định  | Revert YAML → `v1.0.0`                       |
| Dùng ArgoCD UI           | Chọn lại tag cũ → Sync                       |
| Manual deploy (khẩn cấp) | Dùng `kubectl apply -f` với image version cũ |

---

## 🔗 10. Liên kết Nội dung Liên quan

* \[Mục 10 – CI/CD Pipeline] – Kiểm tra, build, Sonar, Docker
* \[Mục 06 – Poetry & Docker] – Môi trường, lock, container
* \[Mục 01 – Project Overview] – Danh sách release theo Epic

---

📌 *Tài liệu này giúp đảm bảo việc phát hành và triển khai có kiểm soát, theo dõi được và rollback dễ dàng – nền tảng của phát triển chuyên nghiệp theo GitOps.*
