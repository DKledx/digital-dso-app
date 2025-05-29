# 🧼 Quy chuẩn Viết Mã Sạch và Chất Lượng Cao

## 01. Thông tin tài liệu

- **Tên tài liệu**: Quy chuẩn viết mã sạch và chất lượng cao  
- **Phiên bản**: v2.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: Tech Coach / DSO Architect  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Thiết lập bộ quy tắc đồng nhất để viết mã Python rõ ràng, dễ đọc, dễ mở rộng  
- Chuẩn hóa với **SonarQube RuleSet** để kiểm tra tự động trong CI/CD  
- Nâng cao chất lượng codebase, giảm bugs, tăng maintainability và readability  
- Làm nền tảng để **review code hiệu quả**, đào tạo kỹ sư, và scale dự án  

---

## 🧭 03. Nguyên lý Clean Code áp dụng

| Nguyên lý              | Mô tả ngắn gọn                                      | SonarQube Rule liên quan   |
|------------------------|-----------------------------------------------------|-----------------------------|
| Khai báo rõ ràng       | Tên biến, hàm, class phải mô tả chức năng           | S1121, S100                 |
| Hàm ngắn gọn           | Mỗi hàm chỉ làm 1 việc, dài tối đa 20 dòng          | S138, S3776                 |
| Không lặp lại          | Tránh duplicate → extract method/class              | S1066, S1117                |
| Không để mã chết       | Xóa code comment cũ, `print`, `pass`, `TODO`        | S125, S1172                 |
| Không hardcode         | Không chèn số, token trực tiếp vào logic            | S1192, S109                 |
| Viết test tốt          | Tự động hóa, rõ ràng, ít phụ thuộc                  | Ảnh hưởng coverage          |
| Không lạm dụng try     | Không nuốt lỗi, bắt lỗi chính xác                   | S2228, S108                 |
| Tuân thủ PEP8          | Dùng black, isort, flake8 để chuẩn hóa style        | Kết hợp CI/CD               |

---

## 📝 04. Quy tắc đặt tên (Naming Rules)

| Đối tượng      | Cách đặt tên   | Ví dụ đúng            |
|----------------|----------------|------------------------|
| Biến           | snake_case     | `total_count`          |
| Hàm            | snake_case     | `calculate_benefit()`  |
| Class          | PascalCase     | `InitiativeService`    |
| Hằng số        | UPPER_CASE     | `MAX_LENGTH = 255`     |
| File/module    | snake_case.py  | `benefit_tracker.py`   |
| Gói (package)  | lowercase       | `initiative_room`      |

---

## 🧪 05. Công cụ kiểm tra & tự động hoá

| Công cụ      | Vai trò                        | Lệnh                          |
|--------------|-------------------------------|-------------------------------|
| black        | Format code chuẩn PEP8        | `poetry run black .`         |
| isort        | Chuẩn hóa thứ tự import       | `poetry run isort .`         |
| flake8       | Lint kiểm tra style           | `poetry run flake8 src/`     |
| mypy         | Kiểm tra type hint            | `poetry run mypy src/`       |
| SonarQube    | Clean Code + bug + coverage   | Tích hợp CI/CD                |
| pytest --cov | Đo test coverage              | `poetry run pytest --cov=src`|

---

## ✅ 06. Mẫu mã đúng và sai

### Đúng:

```python
def calculate_benefit(initiative: Initiative) -> float:
    if initiative.status != "approved":
        return 0.0
    return initiative.revenue - initiative.cost
````

### Sai:

```python
def cb(i):
    if i.s != "a":
        return
    return i.r - i.c
```

---

## 🔁 07. Mapping với SonarQube Rule ID

| Clean Code Vi phạm       | Rule ID      | Cách xử lý                                 |
| ------------------------ | ------------ | ------------------------------------------ |
| Hàm quá dài              | S138, S3776  | Tách nhỏ, mỗi nhánh logic là một hàm riêng |
| Biến không sử dụng       | S1172, S1481 | Xoá hoặc dùng đúng mục đích                |
| Magic numbers            | S109, S1192  | Đưa vào constant hoặc cấu hình             |
| Duplicate logic          | S1066, S1117 | Sử dụng hàm helper hoặc extract object     |
| Hàm thiếu return rõ ràng | S1143, S1186 | Tránh `return None` không kiểm soát        |

---

## 📁 08. Kiểm tra trước khi commit

Tạo file `scripts/dev.sh`:

```bash
#!/bin/bash
echo "🔍 Pre-commit check"
black . && isort . && flake8 src/ && mypy src/ && pytest --cov=src
```

---

## 🔍 09. Áp dụng trong Code Review

### Checklist PR:

| Kiểm tra                | Mục tiêu                           |
| ----------------------- | ---------------------------------- |
| ✅ Tên biến/hàm rõ ràng? | Không viết tắt, rõ nghĩa           |
| ✅ Hàm ngắn và dễ test?  | Mỗi hàm < 20 dòng                  |
| ✅ Không hardcode?       | Dùng biến constant hoặc config     |
| ✅ SonarQube pass?       | Không có Blocker/Bug/Vulnerability |
| ✅ Có test success/fail? | Có test case tự động               |

---

## 🔗 10. Liên kết nội dung liên quan

* \[Mục 03 – Tech Stack & Tooling] – SonarQube + Lint
* \[Mục 09 – Unit & Integration Test] – Coverage + Test case
* \[Mục 12 – Code Review Rules] – Checklist bắt buộc dùng Rulebook này
* \[Mục 15 – Appendix] – Mẫu rule, test, Sonar config

---

📌 *Tài liệu này là một phần không thể thiếu để xây dựng văn hóa kỹ thuật chất lượng cao trong đội ngũ DSO.*
`
