# 📙 Tổng kết Giai đoạn 5 – Testing & Monitoring (Ngày 21 → Ngày 25)

🕒 Thời gian: Ngày 21 → Ngày 25  
🎯 Mục tiêu: Tăng cường độ tin cậy hệ thống thông qua kiểm thử toàn diện, trace log, chuẩn hóa ghi log, và bắt đầu tích hợp monitoring ở cấp độ production (cloud log, error tracking, dashboard coverage).

---

## 🧩 Tổng kết các hành động chính

| Ngày    | Hành động                                                      | Ghi chú                                               |
|---------|---------------------------------------------------------------|-------------------------------------------------------|
| 21      | Viết test cho fail case & edge case của CreateInitiativeUseCase| Kiểm tra đầu vào thiếu, sai định dạng, trùng dữ liệu  |
| 22      | Tạo middleware RequestID + chuẩn hóa logging                   | Mỗi request có ID riêng, trace được toàn hệ thống     |
| 23      | Ghi log song song ra file + console                            | Tạo thư mục logs/, định dạng log chuẩn                |
| 24      | Tích hợp Logtail/Sentry – gửi log & lỗi lên cloud              | Quan sát realtime, tạo trace có request_id            |
| 25      | Tổng hợp báo cáo coverage + log sample + ghi vào dashboard kỹ thuật | Tài liệu hoá toàn bộ kết quả quan sát & kiểm thử  |

---

## ✅ Kết quả đạt được

- Toàn bộ use case chính có test case đầy đủ (success + fail + edge)
- Đo coverage chi tiết theo component (target đạt 85%+)
- Mỗi request sinh request_id, log ra file chuẩn, có thể trace
- Gửi được log & lỗi realtime lên Logtail hoặc Sentry
- Có dashboard kỹ thuật ghi coverage, log mẫu, và status kiểm thử

---

## 🎯 Điều học được

- Test tốt không chỉ để pass CI mà là dám chắc code không gãy
- Logging chuẩn là cách duy nhất để hiểu app đang sống hay đang chết
- Cloud log giúp team không phải SSH vào máy chủ để xem lỗi
- Tài liệu hoá log + test giúp QA, dev mới và cả người vận hành hiểu hệ thống

---

## 🔧 Vấn đề gặp phải (nếu có)

- Sentry ban đầu cần kiểm soát traces_sample_rate để tránh gửi log quá nhiều
- Nếu chưa cài Logtail handler đúng, log cloud không hiện request_id
- File log cần được mount volume khi dùng Docker để tránh mất log khi container reset

---

## 📌 Hành vi tích cực

- Log message luôn gắn request_id → chuẩn trace
- Test có assert cụ thể từng case → tránh mơ hồ
- Commit mỗi ngày đều có mục tiêu rõ ràng
- Ghi lại toàn bộ coverage & log sample thành tài liệu training

---

## 💡 Ý tưởng cải tiến cho giai đoạn sau

- Tích hợp alert từ Sentry hoặc Logtail (Slack, Email)
- Viết command CLI để truy xuất log theo request_id
- Gắn coverage badge và log link realtime vào CI/CD notification

---

## 🔁 Chuẩn bị cho Giai đoạn 6 – Release & Learning (Ngày 26–30)

Giai đoạn tới sẽ phát hành version v0.2.0, viết Learning Note, review toàn bộ 15 mục tài liệu, và tổng kết bài học 30 ngày đầu tiên để mở rộng cho dev mới hoặc triển khai production.