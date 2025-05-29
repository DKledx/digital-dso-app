# 🧪 Hướng dẫn Kiểm thử Đơn vị và Tích hợp – Digital DSO App

## 01. Thông tin tài liệu

- **Tên tài liệu**: Hướng dẫn kiểm thử đơn vị và tích hợp cho Digital DSO App  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Đảm bảo chất lượng logic nghiệp vụ qua **unit test**  
- Đảm bảo tích hợp các thành phần hoạt động đúng qua **integration test**  
- Hỗ trợ phát hiện lỗi sớm qua CI/CD  
- Tăng độ tin cậy khi **refactor** hoặc thêm tính năng mới  

---

## ⚙️ 03. Công cụ Kiểm thử Sử dụng

| Công cụ            | Mục đích                           | Lý do chọn                           |
|--------------------|------------------------------------|--------------------------------------|
| `pytest`           | Framework kiểm thử chính           | Đơn giản, phổ biến, mạnh mẽ          |
| `factory_boy`      | Sinh test data                     | Dễ dùng, hỗ trợ ORM tốt              |
| `httpx`            | Gửi HTTP request giả               | Hỗ trợ async, dùng test API          |
| `pytest-asyncio`   | Test các hàm async                 | Tương thích với FastAPI              |
| `coverage.py`      | Đo coverage toàn hệ thống          | Tích hợp CI/CD tốt                   |

---

## 🧪 04. Phân loại Test

| Loại Test        | Mục tiêu                                    | Mức độ áp dụng  |
|------------------|---------------------------------------------|-----------------|
| Unit Test        | Kiểm thử logic từng use case, entity        | Bắt buộc        |
| Integration Test | Test API hoặc nhiều module kết hợp          | Khuyến nghị     |
| E2E Test         | Test toàn hệ thống (frontend ↔ backend)     | Tuỳ chọn sau    |

---

## 📂 05. Tổ chức Thư mục Test (theo Component)

```

tests/
├── components/
│   ├── initiative\_room/
│   │   ├── test\_create\_initiative.py
│   │   ├── test\_get\_initiative.py
│   │   └── conftest.py
│   └── portfolio\_room/
│       └── ...
├── shared/
│   └── test\_utils.py
├── factories/
│   ├── initiative\_factory.py
│   └── portfolio\_factory.py
├── conftest.py

````

> Có thể chia `unit/`, `integration/` nếu số lượng test tăng cao.

---

## 🧪 06. Viết Unit Test – Use Case

```python
def test_calculate_benefit_success():
    initiative = Initiative(id=1, cost=1000, revenue=3000, status="approved")
    use_case = CalculateBenefitUseCase()
    result = use_case.execute(initiative)
    assert result.benefit == 2000
````

✅ Không cần DB
✅ Test success + edge case + invalid input

---

## 🌐 07. Viết Integration Test – FastAPI

```python
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_initiative_api():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"name": "DSO", "type": "Growth", "quarter": "Q2"}
        response = await ac.post("/initiative", json=payload)
        assert response.status_code == 201
        assert response.json()["name"] == "DSO"
```

✅ Gửi HTTP request ảo
✅ Dùng `http://test` để tránh request thật

---

## 🛠️ 08. Factory mẫu – Factory Boy

```python
import factory
from domain.entities.initiative import Initiative

class InitiativeFactory(factory.Factory):
    class Meta:
        model = Initiative

    id = factory.Sequence(lambda n: n + 1)
    name = "SKCL Demo"
    revenue = 3000
    cost = 1000
    status = "approved"
```

---

## 📈 09. Coverage & Kiểm thử Local

```bash
poetry run pytest --cov=src
```

Ví dụ kết quả:

```
---------- coverage: platform darwin ----------
Name                                      Stmts   Miss  Cover
-------------------------------------------------------------
src/application/use_cases/create.py           12      0   100%
src/interface/rest/routers/initiative.py      35      3    91%
-------------------------------------------------------------
TOTAL                                         47      3    94%
```

✅ Mục tiêu coverage ≥ **85%**

---

## 🔄 10. Tích hợp CI/CD

Trong `.github/workflows/ci.yml`:

```yaml
- name: Run tests
  run: |
    poetry run pytest --cov=src --cov-report=xml
```

Gợi ý thêm badge vào `README.md`:

```markdown
![Test Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)
```

---

## 🔗 11. Liên kết Nội dung Liên quan

* \[Mục 04 – Coding Standards] – Format + Convention
* \[Mục 08 – Feature Dev Flow] – Checklist khi làm tính năng
* \[Mục 10 – CI/CD Pipeline] – Tích hợp kiểm thử tự động
* \[Mục 15 – Template mẫu] – Mẫu test, factory, config sẵn

---

📌 *Tài liệu này là chuẩn kiểm thử để đảm bảo chất lượng hệ thống khi scale lên nhiều team và component.*

