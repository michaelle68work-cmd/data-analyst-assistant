---
name: input-knowledge
description: Nạp domain knowledge từ tài liệu người dùng cung cấp thành file chuẩn trong domain-knowledge/. Trigger khi user nói "nạp kiến thức", "input knowledge", "thêm domain", "tôi muốn phân tích lĩnh vực mới", hoặc đưa tài liệu/PDF/slide/note về một ngành.
---

# Input Knowledge — Nạp domain knowledge

Biến tài liệu người dùng cung cấp thành file domain chuẩn trong `domain-knowledge/`.

## LUẬT TỐI THƯỢNG: chỉ tài liệu người dùng đưa mới là chân lý

**Domain file chỉ được chứa nội dung digest từ tài liệu người dùng input vào.**

Bất kỳ kiến thức nào không có trong tài liệu nguồn — dù bạn biết chắc, dù nó phổ biến,
dù nó "hiển nhiên đúng" — đều phải:

1. Đặt trong mục riêng `## [BỔ SUNG NGOÀI TÀI LIỆU — CHỜ XÁC NHẬN]`
2. Ghi rõ bạn lấy từ đâu (kiến thức chung / web search / suy luận)
3. Hỏi người dùng xác nhận từng mục
4. Chỉ khi người dùng **đồng ý rõ ràng** mới chuyển lên phần thân file và đánh dấu
   `(người dùng xác nhận YYYY-MM-DD)`
5. Người dùng từ chối → xoá hẳn, không giữ lại

Tuyệt đối không trộn kiến thức tự thêm vào chung với nội dung từ tài liệu.

## Quy trình

1. **Nhận tài liệu** — text dán, PDF, DOCX, slide, ảnh, hoặc phỏng vấn miệng người dùng.
   Nếu là file: đọc và trích xuất trước. Không có tài liệu → hỏi, không tự viết.
2. **Xác định domain name** — kebab-case: `marketing-sales`, `finance`, `ecommerce`, `saas-tech`.
   Đã tồn tại file → hỏi: cập nhật hay tạo mới?
3. **Digest theo `_TEMPLATE.md`** — gom nội dung tài liệu về đúng 9 mục. Tổng hợp và
   sắp xếp lại, không chép nguyên văn dài dòng. Giữ lại thứ dùng được khi phân tích.
4. **Ghi nguồn cho từng mục** — mỗi mục ghi tài liệu nào, trang nào.
5. **Đánh dấu khoảng trống** — mục nào tài liệu không đề cập thì ghi `[CHƯA CÓ]`.
   **Không lấp bằng kiến thức của bạn.**
6. **Liệt kê phần bổ sung ngoài tài liệu** (nếu có) và hỏi xác nhận theo luật ở trên.
7. **Ghi file** `domain-knowledge/<domain>.md`, rồi báo cáo lại:
   nạp được gì · còn thiếu gì · đang chờ xác nhận gì.

## Nguyên tắc

- **Không bịa benchmark, không bịa công thức.** Con số chỉ ghi khi tài liệu có, kèm nguồn + năm.
- Ưu tiên thứ có tính quyết định khi phân tích: định nghĩa metric, công thức, business rule,
  ngưỡng cảnh báo, cách phân segment.
- **TÁCH FILE, KHÔNG TÓM TẮT.** Không có trần dòng cho tổng lượng kiến thức.
  Chỉ có trần cho phần *luôn được nạp*: file chính ~200 dòng giữ thứ dùng ở MỌI phân tích
  (định nghĩa metric, công thức, business rule, framework ưu tiên).
  Phần tra cứu dài chuyển **nguyên văn, không rút gọn** sang
  `domain-knowledge/<domain>.refs/<chủ-đề>.md`.
- **Bắt buộc có mục lục refs** ở cuối file chính: liệt kê mọi file refs + một dòng
  "nạp khi nào". Không có index = kiến thức tàng hình = mất trên thực tế.
- **Giữ tài liệu gốc** ở `domain-knowledge/<domain>.sources/`. Mỗi mục trong domain file
  ghi rõ nguồn + trang. Digest là bản cache tra nhanh, KHÔNG thay thế tài liệu gốc —
  nghi ngờ chỗ nào thì mở lại nguồn.
- Ghi rõ danh sách tài liệu nguồn và ngày cập nhật cuối ở đầu file.
- Cần tra cứu thêm từ web → dùng skill `search`, kết quả vẫn phải qua vòng xác nhận.
