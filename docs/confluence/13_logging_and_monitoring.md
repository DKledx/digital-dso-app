# 📈 Mục 13 – Hướng dẫn Ghi Log và Giám sát Hệ thống – Digital DSO App

## 01. Thông tin tài liệu

- **Tên tài liệu**: Hướng dẫn ghi log và giám sát hệ thống  
- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người biên soạn**: LDK  
- **Người sở hữu**: Khuong Le  

---

## 🎯 02. Mục tiêu

- Ghi log có cấu trúc rõ ràng để **debug, truy vết, và phân tích sự cố**  
- Phát hiện lỗi sớm và hỗ trợ **tự động cảnh báo** khi lên staging/production  
- Giám sát hiệu suất hệ thống: latency, tần suất gọi API, lỗi phổ biến  
- Chuẩn bị tích hợp hệ thống như **Sentry**, **Prometheus/Grafana**  

---

## 🧱 03. Tiêu chuẩn Ghi Log

| Yếu tố               | Quy định                                                        |
|----------------------|------------------------------------------------------------------|
| Format               | JSON hoặc structured string                                      |
| Level                | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`                 |
| Request ID           | Gắn `UUID` vào mỗi request để trace                              |
| Không ghi log nhạy cảm | Không log password, token, thông tin định danh cá nhân (PII)     |
| Theo Component       | Mỗi Room có logger riêng: `strategy_room`, `initiative_room`... |

---

## 📝 04. Mẫu cấu hình logging (`shared/config/logger.py`)

```python
import logging
import sys

FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] [%(request_id)s] %(message)s"

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(record, 'request_id', '-')
        return True

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    handler.addFilter(RequestIdFilter())
    logger.addHandler(handler)
    return logger
````

---

## 🌐 05. Gắn `request_id` bằng FastAPI Middleware

```python
# shared/middleware/request_id.py
from starlette.middleware.base import BaseHTTPMiddleware
from uuid import uuid4

class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = str(uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
```

Trong `main.py`:

```python
from fastapi import FastAPI
from shared.config.logger import setup_logger
from shared.middleware.request_id import RequestIdMiddleware

app = FastAPI()
app.add_middleware(RequestIdMiddleware)

logger = setup_logger("initiative_room")
```

---

## 🧪 06. Mẫu Log Chuẩn

```
[2025-05-25 08:00:23] [INFO] [initiative_room] [13ca-345b] Created initiative ID=123
[2025-05-25 08:00:25] [ERROR] [portfolio_room] [13ca-345b] Failed to fetch quarter=Q5: InvalidQuarterException
```

---

## 🛠️ 07. Hệ thống Giám sát Nâng cao (Tùy chọn)

| Công cụ              | Mục tiêu             | Tích hợp                                           |
| -------------------- | -------------------- | -------------------------------------------------- |
| Sentry               | Theo dõi lỗi runtime | Gắn SDK vào FastAPI, set tag theo Room             |
| Prometheus + Grafana | Theo dõi hiệu suất   | Export metrics từ FastAPI / Docker                 |
| Logtail / ELK        | Phân tích log        | Gửi stdout hoặc tập tin vào nền tảng log phân tích |

> Chỉ triển khai khi đã có staging + sản phẩm thật đang hoạt động.

---

## 🧪 08. Các chỉ số cần giám sát

| Chỉ số                     | Mục tiêu theo dõi                        |
| -------------------------- | ---------------------------------------- |
| **API Latency**            | Giảm độ trễ trung bình theo endpoint     |
| **Số lỗi 5xx theo ngày**   | Phát hiện lỗi backend hoặc bất thường DB |
| **Tần suất tạo SKCL**      | Đo lường mức độ sử dụng tính năng        |
| **Lỗi logic / validation** | Phát hiện input xấu, sai nghiệp vụ       |

---

## 🔗 09. Liên kết Nội dung Liên quan

* \[Mục 06 – Dependency Management] – Thêm logging & sentry vào `pyproject.toml`
* \[Mục 10 – CI/CD Pipeline] – Gắn log stdout trong CI
* \[Mục 11 – GitOps & Release] – Ghi log khi release/deploy
* \[Mục 15 – Appendix] – Mẫu cấu hình logger & middleware

