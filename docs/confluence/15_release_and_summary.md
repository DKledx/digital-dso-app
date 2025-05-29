# 📎 Mục 15 – Appendix & Templates – Digital DSO App

## Thông tin tài liệu

- **Tên tài liệu**: Phụ lục và bộ mẫu chuẩn hoá tài liệu, mã nguồn, cấu hình CI/CD  
- **Phiên bản**: v2.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: DSO Coordinator / Tech Coach  
- **Người sở hữu**: Khuong Le  

---

## 🎯 1. Mục tiêu

- Cung cấp bộ mẫu tài liệu, cấu hình và đoạn mã chuẩn để sử dụng xuyên suốt dự án  
- Hỗ trợ phát triển nhanh, đúng chuẩn Clean Code, dễ kiểm thử và triển khai  
- Là công cụ hỗ trợ đào tạo nội bộ, onboarding, review code và CI/CD  

---

## 📂 2. Cấu trúc thư mục `templates/` trong repository

```plaintext
templates/
├── docs/
│   ├── brd_template.md
│   ├── pr_template.md
│   ├── test_case_template.md
│   └── learning_note_template.md
├── code/
│   ├── usecase_skeleton.py
│   ├── router_skeleton.py
│   ├── test_skeleton.py
│   └── logger_sample.py
├── ci/
│   ├── ci_template.yml
│   ├── release_template.yml
│   └── sonar-project.properties
├── scripts/
│   └── dev_check.sh
````

---

## 📘 3. Danh sách mẫu tài liệu

### 📄 brd\_template.md

```markdown
### 🎯 User Story / Feature
Khi tôi là [vai trò], tôi muốn [mong muốn] để [giá trị mong muốn].

### 📋 Business Rule
- Rule 1
- Rule 2

### 🧱 Data Schema liên quan
- Request
- Response

### 📎 Tài liệu liên kết
- Mockup
- BPMN
```

### 🔁 pr\_template.md (.github/pull\_request\_template.md)

```markdown
## 🎯 Mục tiêu
Giải thích mục tiêu của PR (gắn link Epic nếu có)

## 🧱 Thay đổi chính
- Tính năng mới
- Sửa lỗi
- Refactor

## ✅ Checklist
- [x] SonarQube pass (No Blocker/Bug/Vuln)
- [x] Code format chuẩn (black, isort, flake8)
- [x] Đã test local
- [x] Đủ test case success/fail
- [x] Được reviewer approve
```

### 🧪 test\_case\_template.md

```markdown
## 🎯 Tên chức năng
Thêm SKCL theo quý

### ✅ Test case

| ID   | Mô tả         | Input         | Output | Kết quả mong đợi  |
|------|----------------|---------------|--------|--------------------|
| TC01 | Thành công     | name="DSO"     | 201    | Trả về ID          |
| TC02 | Thiếu quý      | quarter=None   | 422    | Báo lỗi             |
```

---

## 🧱 4. Mẫu mã nguồn chuẩn

### ✅ usecase\_skeleton.py

```python
class CreateInitiativeUseCase:
    def __init__(self, repo: InitiativeRepository):
        self.repo = repo

    def execute(self, data: InitiativeCreateRequest) -> InitiativeResponse:
        initiative = Initiative(**data.dict())
        self.repo.save(initiative)
        return initiative
```

### ✅ test\_skeleton.py

```python
def test_create_initiative_success():
    data = InitiativeFactory.build()
    uc = CreateInitiativeUseCase(MockRepo())
    result = uc.execute(data)
    assert result.id is not None
```

### ✅ router\_skeleton.py

```python
@router.post("/initiative", status_code=201)
def create_initiative(request: InitiativeCreateRequest):
    uc = CreateInitiativeUseCase()
    return uc.execute(request)
```

### ✅ logger\_sample.py

```python
logger.info("[INITIATIVE] Created new initiative %s", initiative.id, extra={"request_id": request_id})
```

---

## ⚙️ 5. CI/CD & SonarQube

### ✅ ci\_template.yml

```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install poetry && poetry install
      - run: poetry run black . --check
      - run: poetry run flake8 src/
      - run: poetry run mypy src/
      - run: poetry run pytest --cov=src
```

### ✅ sonar-project.properties

```properties
sonar.projectKey=digital-dso-app
sonar.organization=f88
sonar.sources=src
sonar.tests=tests
sonar.language=python
sonar.sourceEncoding=UTF-8
sonar.python.coverage.reportPaths=coverage.xml
```

---

## 🔧 6. Scripts hỗ trợ

### ✅ scripts/dev\_check.sh

```bash
#!/bin/bash
echo "▶️ Run: Format + Lint + Test + Type Check"
poetry run black .
poetry run isort .
poetry run flake8 src/
poetry run mypy src/
poetry run pytest --cov=src
```

---

## 🧠 7. Ghi chú học tập

### ✅ learning\_note\_template.md

```markdown
## 📚 Tuần 01: Clean Code

### 🔑 3 Ý chính học được
- Tên hàm nên mô tả hành vi
- Viết hàm ngắn dễ test
- Không nên dùng comment để thay logic xấu

### 💡 Ứng dụng thực tế
Refactor UseCase `CreateInitiative` để ngắn hơn

### 📎 Link tham khảo
- Clean Code – Robert C. Martin
```

---

## 🔗 8. Liên kết nội dung liên quan

* \[Mục 04 – Clean Code Rulebook] – Mapping với Sonar rules
* \[Mục 08 – Feature Dev Flow] – Sử dụng BRD + UseCase skeleton
* \[Mục 10 – CI/CD Pipeline] – Dùng CI template
* \[Mục 14 – Learning Notes] – Dùng learning template tuần/quý

---

### Gợi ý hành động tiếp theo

1. **Đưa toàn bộ thư mục `templates/` vào repository chính**, tránh trôi tài liệu.
2. **Gắn `pull_request_template.md` vào `.github/` để enforce review tốt hơn.**
3. **Thêm đường dẫn tới Mục 15 này trên dashboard Confluence.**
4. **Tổ chức mini workshop giới thiệu cách dùng từng file template cho team mới.**
5. **Kết nối CI pipeline với SonarCloud và coverage badge trên README.**

---

✍️ *Dự án chuyên nghiệp không chỉ nằm ở mã nguồn – mà còn ở cách bạn tổ chức, chuẩn hoá, và chia sẻ kiến thức.*
