# 🧠 Learning Note #01 – Clean Code, Testing & Logging
📅 Thời điểm viết: Ngày 27 – 27/06/2025  
📂 Chủ đề: Hành trình viết module đầu tiên đúng cách và hiểu rõ giá trị việc **viết sạch, test kỹ, log rõ**
---
## 🔎 Bối cảnh
- Module đầu tiên: `initiative_room`  
- Tập trung viết UseCase, schema, API  
- Bắt đầu gắn CI, test, log, và quan sát
---
## 🔑 5 Bài học cá nhân rút ra
### 1. **Clean Code không phải là style – đó là hợp đồng với chính mình trong tương lai**
> Khi tôi đọc lại code sau 2 tuần, tôi biết ơn mình đã viết rõ từng `usecase`, không nhét logic vào API.
Ví dụ: `CreateInitiativeUseCase.execute()` chỉ chứa xử lý nghiệp vụ – dễ test, dễ mở rộng.
---
### 2. **Test tốt không chỉ giúp code sống – mà giúp tôi ngủ ngon**
> Lúc đầu tôi sợ test, nhưng sau khi viết xong `test_create_initiative_api.py`, tôi thấy:  
> - Khi thêm feature mới, tôi dám refactor.  
> - Khi lỗi, tôi debug dễ hơn vì biết logic sai, không phải framework.
---
### 3. **RequestID là sợi chỉ đỏ xuyên suốt toàn hệ thống**
> Gắn `request_id` từ middleware vào toàn bộ log giúp tôi trace lỗi như đi ngược timeline – biết request nào sinh ra lỗi gì, ở đâu.
---
### 4. **Log không phải là noise – nó là giác quan của hệ thống**
> Khi ghi log ra file + cloud, tôi bắt đầu nhìn hệ thống như sinh vật sống.  
> Mỗi hành động user → có log tương ứng, có thể phân tích lại nếu cần.
---
### 5. **Chưa gắn CI = chưa gọi là “đã code xong”**
> Viết xong, chưa test CI, chưa pass coverage → chưa xong.  
> Sau Ngày 20, tôi hiểu rõ thế nào là "xong sạch": push tag, CI chạy, Docker image build, log đầy đủ.
---
## 📌 Gắn link minh hoạ
- Test mẫu: [`test_create_initiative_api.py`](../../tests/components/initiative_room/test_create_initiative_api.py)
- Log mẫu: [`log_samples.md`](../summary/log_samples.md)
- Log thật trên cloud: [Logtail Dashboard](https://logtail.com/project/*/logs)
---
## ✍️ Ghi chú cuối
> “Viết code tốt không phải để giỏi – mà để người khác không phải sợ khi đọc lại.”
---
## 📁 Vị trí file lưu
📄 `docs/learning_notes/learning_note_01_clean_code_testing_logging.md`