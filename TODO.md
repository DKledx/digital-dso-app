# TODO kỹ thuật – Digital DSO App

## CI/CD & Code Style

- [ ] Đã tạm thời comment kiểm tra Black/isort trong CI (`.github/workflows/ci.yml`) để tránh block tiến độ.
- [ ] Sau khi hoàn thiện chức năng chính, cần:
    - Bỏ comment các dòng kiểm tra Black/isort trong CI.
    - Chạy lại `poetry run isort .` và `poetry run black .` trên toàn bộ project.
    - Commit lại để đảm bảo code chuẩn hóa và CI luôn xanh.

## Ghi chú

- Lý do: Đang gặp lỗi format/import do Black/isort, cần ưu tiên tiến độ. Sẽ hoàn thiện sau.
- Có thể cân nhắc dùng [ruff](https://github.com/astral-sh/ruff) thay thế cho black, isort, flake8 nếu muốn đơn giản hóa về sau.

---

*Ghi chú này giúp team không quên chuẩn hóa code khi quay lại hoàn thiện CI/CD.*