# 🔄 Quy trình Tích hợp & Triển khai Liên tục (CI/CD) – Digital DSO App

## 01. Thông tin tài liệu

- **Tên tài liệu**: Quy trình tích hợp & triển khai liên tục  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Tự động hoá kiểm tra chất lượng mã nguồn (lint, type, test, coverage)  
- Build và đóng gói app khi được merge  
- Tự động publish Docker image (GHCR) khi có tag  
- Hỗ trợ release staging theo version  
- Tối ưu thời gian phản hồi & chất lượng khi merge code  

---

## 🔄 03. Pipeline chuẩn

```mermaid
graph LR
  A[Push/PR] --> B[Check Format (Black, isort)]
  B --> C[Lint (flake8)]
  C --> D[Static Type Check (mypy)]
  D --> E[Unit & Integration Test (pytest)]
  E --> F[Coverage Report]
  F --> G{Main branch?}
  G -- Yes --> H[Build Docker Image]
  H --> I[Publish Image to GHCR]
  I --> J[Trigger Staging Deploy]
````

---

## 🧱 04. Cấu trúc thư mục

```
.github/
└── workflows/
    ├── ci.yml               # CI cho PR và push
    └── release.yml          # Release staging/prod theo tag
```

---

## 🧪 05. Nội dung file `ci.yml` – kiểm tra & test

```yaml
name: CI Pipeline

on:
  push:
    branches: [main, staging]
  pull_request:
    branches: [main, staging]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.11"

    - name: Install Poetry
      run: curl -sSL https://install.python-poetry.org | python3 -

    - name: Install dependencies
      run: poetry install

    - name: Check code format
      run: |
        poetry run black . --check
        poetry run isort . --check-only

    - name: Lint
      run: poetry run flake8 src/

    - name: Static type check
      run: poetry run mypy src/

    - name: Run Tests
      run: poetry run pytest --cov=src --cov-report=xml

    - name: Upload coverage report
      uses: actions/upload-artifact@v4
      with:
        name: coverage-report
        path: coverage.xml

    - name: SonarQube Scan
      uses: sonarsource/sonarqube-scan-action@v1.0.0
      with:
        projectBaseDir: .
        args: >
          -Dsonar.projectKey=your_project_key
          -Dsonar.organization=your_org
          -Dsonar.host.url=https://sonarcloud.io
          -Dsonar.login=${{ secrets.SONAR_TOKEN }}
```

---

## 🐳 06. Nội dung file `release.yml` – build & publish Docker (theo tag)

```yaml
name: Release & Publish Image

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build-publish:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Log in to GitHub Container Registry
      uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Build & Push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        file: docker/Dockerfile
        tags: ghcr.io/${{ github.repository }}:${{ github.ref_name }}
        push: true
```

---

## 📦 07. Cấu hình `Dockerfile` mẫu

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📊 08. Badge CI & Coverage (README.md)

```markdown
![CI](https://github.com/<org>/digital-dso-app/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)
```

---

## 🔗 09. Liên kết nội dung liên quan

* \[Mục 06 – Dependency Management] – Poetry & Docker
* \[Mục 09 – Testing Guide] – Coverage + Factory test
* \[Mục 11 – GitOps & Release] – Trigger deploy staging/prod
* \[Mục 15 – Template mẫu] – scripts, test config, sonar

---

## ✅ Gợi ý hành động tiếp theo

1. Tạo file `.github/workflows/ci.yml` và test bằng PR đầu tiên
2. Thiết lập `SONAR_TOKEN` trong GitHub Secrets
3. Tạo file `release.yml` để hỗ trợ staging/prod khi tag `vX.Y.Z`
4. Thêm badge CI + Coverage vào `README.md`
5. Tiếp tục viết \[Mục 11 – GitOps & Release Flow]

---

📌 *Tài liệu này là chuẩn CI/CD giúp dự án Digital DSO App đạt được chất lượng cao và phản hồi nhanh chóng khi phát triển.*
