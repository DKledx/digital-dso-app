📅 Ngày 15 – 13/06/2025  
🔹 Hành động chính:
- Merge develop vào main
- Tạo Git tag v0.1.0
- Ghi changelog đầy đủ
- Gắn changelog vào README

🔸 Ghi chú:
- Tag = bản snapshot có thể deploy hoặc rollback
- Changelog rõ ràng giúp người khác dễ review và build dựa trên trạng thái hệ thống

- **Luôn pull mới nhất từ remote cho cả develop và main trước khi merge.**
- Khi merge develop vào main, nếu có conflict:
  - Mở từng file bị conflict, đọc kỹ phần khác biệt giữa hai nhánh.
  - Ưu tiên giữ lại logic đã kiểm thử, code sạch, hoặc code đã chuẩn hóa trên develop.
  - Nếu main có hotfix hoặc cấu hình CI/CD đặc biệt, cần cân nhắc giữ lại hoặc hợp nhất với thay đổi từ develop.
  - Xóa toàn bộ dấu conflict (`<<<<<<<`, `=======`, `>>>>>>>`) sau khi chọn nội dung đúng.
  - Test lại toàn bộ hệ thống sau khi resolve conflict.
- Sau khi resolve conflict, commit với message rõ ràng, push lên remote và kiểm tra lại CI/CD.

💡 Nhận định:
- GitOps bắt đầu từ cách mình tôn trọng release nhỏ nhất
- Đừng để release là "tôi nghĩ là ổn", hãy để tag tự nói lên chất lượng
