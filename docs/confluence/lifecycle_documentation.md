# 📌 Mục 00 – Tài liệu quản trị vòng đời tài liệu Digital DSO App

- **Phiên bản**: v1.0  
- **Ngày cập nhật**: 2025-05-25  
- **Người phụ trách**: LDK – Head of Digital Steering Office (DSO)

---

## 🎯 Mục tiêu

- Đảm bảo 15 mục tài liệu chuẩn (từ Mục 01–15) luôn đồng hành với tiến trình phát triển sản phẩm  
- Giúp đội ngũ:
  - Có bộ khung tài liệu sống (living documentation)  
  - Tích hợp đào tạo, triển khai, kiểm thử, giám sát vào một hệ thống  
  - Đảm bảo ứng dụng Digital DSO luôn vận hành đúng triết lý Clean Architecture – Clean Code – DevOps  

---

## 🔄 1. Vòng đời phát triển ứng dụng Digital DSO

```mermaid
graph LR
Idea[Khởi tạo ý tưởng] --> POC[POC kỹ thuật]
POC --> MVP[MVP & Team Setup]
MVP --> Expansion[Mở rộng tính năng]
Expansion --> Production[Triển khai production]
Production --> Scale[Scale toàn công ty]
Scale --> Evolve[Tiếp tục đổi mới, tích hợp hệ thống lớn]
````

---

## 🧭 2. Phân bổ trách nhiệm cập nhật từng mục theo giai đoạn

| Giai đoạn  | Mục cần tạo mới / cập nhật | Người phụ trách                     |
| ---------- | -------------------------- | ----------------------------------- |
| Khởi tạo   | 01, 02, 03                 | CTO / Tech Lead / DSO               |
| POC        | 04, 05, 06, 07             | Lead Dev / Solution Architect       |
| MVP        | 08, 09, 10                 | Feature Lead / QA                   |
| Expansion  | 11, 12, 13                 | DevOps / Infra / Reviewer           |
| Production | 14, 15                     | Head of DSO / Trainer / QA          |
| Scale      | Toàn bộ 01–15              | Chủ trì: DSO Team, chia theo module |
| Evolve     | Bổ sung như Mục 16 (AI...) | Innovation Squad                    |

---

## 🛠 3. Cách quản lý và duy trì 15 mục hiệu quả

### 📁 3.1. Cấu trúc thư mục Confluence gợi ý

```plaintext
Digital DSO App (Confluence Space)
├── 🔹 00. Project Dashboard
├── 📘 01. Project Overview
├── 🏗️ 02. Architecture Vision
├── 🧰 03. Tech Stack & Tooling
├── ✨ 04. Clean Code Rulebook
├── 🗂️ 05. Folder & Component Structure
├── 📦 06. Dependency Management
├── ⚙️ 07. Environment Setup
├── 🧩 08. Feature Dev Flow
├── 🧪 09. Unit & Integration Test
├── 🚀 10. CI/CD Pipeline
├── 🚦 11. GitOps & Release Flow
├── 🔍 12. Code Review & Merge Rule
├── 📈 13. Monitoring & Logging
├── 🎓 14. Training & Learning Notes
├── 📎 15. Appendix & Templates
```

✅ Mỗi mục là 1 trang riêng, có **owner** chịu trách nhiệm cập nhật và liên kết vào **Project Dashboard**

---

### 📆 3.2. Chu kỳ cập nhật định kỳ

| Loại cập nhật           | Chu kỳ                     | Người kiểm soát     |
| ----------------------- | -------------------------- | ------------------- |
| Định kỳ 2 tuần (Sprint) | Update mục 08–10–12–09     | Feature Lead        |
| Định kỳ theo quý        | Review lại 01–07–13–15     | DSO / DevOps        |
| Khi có release mới      | Cập nhật mục 11–14         | DevOps / Trainer    |
| Khi onboard nhân sự mới | Review 03–04–05–14–15      | Onboarding Champion |
| Khi refactor kiến trúc  | Update toàn bộ 02–04–05–06 | CTO / Architect     |

---

## 🧩 4. Gắn vòng đời với từng mục

| Mục                       | Giai đoạn chính     | Ghi chú                       |
| ------------------------- | ------------------- | ----------------------------- |
| 01 – Project Overview     | Tạo khi lên ý tưởng | Giữ nguyên, bổ sung milestone |
| 02 – Architecture Vision  | POC → MVP           | Vẽ lại sơ đồ nếu thay đổi lớn |
| 03 – Tech Stack & Tooling | POC + update lib    | Đánh dấu lib deprecated       |
| 04 – Coding Standards     | Đào tạo + refactor  | "Luật chơi" sống còn          |
| 05 – Folder Structure     | POC → chia team     | Gắn chặt Clean Architecture   |
| 06 – Dependency Mgmt      | Update lib          | Check security, compat.       |
| 07 – Environment Setup    | Onboarding dev mới  | Hoạt động trong 10 phút       |
| 08 – Feature Dev Flow     | Trước mỗi Epic      | Có template riêng theo Room   |
| 09 – Testing Guide        | Khi thêm tính năng  | Coverage theo component       |
| 10 – CI/CD                | Khi đổi workflow    | Tách job & policy rõ ràng     |
| 11 – GitOps & Release     | Khi có staging      | Gắn version/tag chuẩn         |
| 12 – Code Review Rules    | Khi scale team      | Có thể training mẫu           |
| 13 – Monitoring & Logging | Sau MVP             | Log bắt buộc có request\_id   |
| 14 – Learning Notes       | Theo tuần/quý       | Gắn với OKR học tập           |
| 15 – Appendix/Templates   | Ngay từ đầu         | Càng đầy đủ onboard càng dễ   |

---

## 📌 5. Gợi ý vai trò đảm trách

| Vai trò         | Trách nhiệm                                            |
| --------------- | ------------------------------------------------------ |
| DSO / CTO       | Quản trị tổng thể 15 mục, bảo đảm áp dụng đúng         |
| Tech Lead       | Định kỳ review & cải tiến 02, 04, 05                   |
| DevOps          | Duy trì 10, 11, 13 – CI/CD, GitOps, Logging            |
| Feature Owner   | Tạo Epic BRD, cập nhật 08, 09, 12                      |
| QA              | Gắn test coverage + checklist cho mỗi PR               |
| Trainer / Coach | Duy trì mục 14 (training), hướng dẫn mục 15 (template) |

---

## ✅ 6. Nguyên tắc quản lý sống (Living Documentation)

* **Không viết rồi để đó**: Gắn chặt vào lifecycle dev → test → release
* **Mỗi mục có owner** – người chịu trách nhiệm cuối cùng trước khi merge
* **Gắn link vào README hoặc Project Dashboard** để dễ truy cập
* **Tích hợp tài liệu với công cụ đào tạo (LMS, Confluence template, Notion...)**

