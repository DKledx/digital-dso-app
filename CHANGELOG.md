# 📦 Changelog

## [v0.1.0] – 2025-06-13

### 🎯 Chức năng chính
- UseCase `CreateInitiative`
- API `POST /initiative`
- RequestID Middleware + Logger chuẩn
- Unit + Integration test
- CI: black, isort, flake8, pytest, coverage
- SonarQube tích hợp

### ✅ Kiến trúc
- Clean Architecture 3 lớp + Component hóa theo Room
- Folder structure chuẩn hóa

## [v0.2.0] – 2025-06-26
### 🧠 Tính năng bổ sung
- Middleware `RequestID` để trace từng request
- Logging chuẩn: console + file + Logtail
- Cloud error tracking: Sentry/Logtail integration
- Tăng test coverage toàn hệ thống lên > 85%
### ✅ CI/CD
- Gắn badge CI + coverage vào README
- Tag `v0.2.0` tự động build Docker image và log release
### 📊 Chất lượng mã nguồn
- Coverage: 87%
- Code Smell: 0 blocker
- Lỗi production traceable theo request_id
