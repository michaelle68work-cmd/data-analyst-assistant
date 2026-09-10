---
name: recommendation
description: Tham khảo ý kiến AI để verify insight hoặc gợi ý hành động - sinh prompt chất lượng cao để hỏi LLM khác, hoặc tự đóng vai phản biện. Trigger khi user nói "cho tôi ý kiến", "verify insight này", "nên làm gì tiếp", "hỏi AI khác", "viết prompt để tôi hỏi ChatGPT/Gemini", hoặc muốn kiểm chứng kết luận trước khi trình bày.
---

# Recommendation — Tham khảo & phản biện bằng AI

Hai chế độ. Hỏi người dùng muốn chế độ nào nếu chưa rõ.

---

## CHẾ ĐỘ 1 — Tự phản biện (devil's advocate)

Đóng vai người phản biện khó tính với insight đang có. Với **mỗi** insight, chạy đủ 5 câu:

1. **Giải thích thay thế** — còn cách nào khác giải thích cùng dữ liệu này không?
2. **Chứng cứ ngược** — nếu insight này SAI thì dữ liệu sẽ trông thế nào? Ta có kiểm tra chưa?
3. **Nhân quả** — đây là causation hay chỉ correlation? Có biến ẩn nào không?
4. **Tính đại diện** — mẫu/kỳ dữ liệu có đại diện được cho kết luận rộng như vậy không?
5. **Bias** — có survivorship, selection, hay confirmation bias không?

Trả về theo định dạng:

```
INSIGHT: <phát biểu gốc>
  Điểm mạnh: <chứng cứ vững ở đâu>
  Điểm yếu: <chỗ dễ bị bắt bẻ nhất>
  Phản biện mạnh nhất: <lập luận ngược thuyết phục nhất>
  Cần thêm gì để chắc chắn: <dữ liệu/kiểm tra cụ thể>
  Kết luận: GIỮ NGUYÊN / HẠ ĐỘ CHẮC CHẮN / RÚT LẠI
```

---

## CHẾ ĐỘ 2 — Sinh prompt để hỏi LLM khác

Khi người dùng muốn hỏi ChatGPT, Gemini, Perplexity... Viết prompt **đầy đủ ngữ cảnh
để dán thẳng vào**, không cần chỉnh.

### Cấu trúc prompt bắt buộc

```
[VAI TRÒ]      Bạn là <chuyên gia gì>, <bao nhiêu năm> kinh nghiệm trong <ngành>.
[BỐI CẢNH]     Doanh nghiệp: <mô tả>. Thị trường: <mô tả>. Kỳ dữ liệu: <thời gian>.
[DỮ LIỆU]      <các con số cụ thể, kèm đơn vị và nguồn>
[ĐÃ PHÂN TÍCH] <những gì đã làm, đã loại trừ được gì>
[CÂU HỎI]      <1 câu hỏi chính, rõ ràng>
[RÀNG BUỘC]    <ngân sách, thời gian, nguồn lực, giới hạn pháp lý>
[ĐỊNH DẠNG]    <muốn trả lời dạng gì, dài bao nhiêu>
[YÊU CẦU]      Nếu không đủ dữ liệu để kết luận, hãy nói rõ thiếu gì thay vì đoán.
```

### Nguyên tắc viết prompt

- Đưa **số thật**, không đưa mô tả mơ hồ kiểu "doanh số giảm nhiều"
- Nêu rõ những gì đã loại trừ, để LLM không lặp lại đường cụt
- Một prompt = một câu hỏi chính
- Luôn có dòng "nếu không đủ dữ liệu thì nói rõ" để chặn LLM bịa
- **Ẩn danh dữ liệu nhạy cảm** trước khi đưa ra công cụ ngoài — cảnh báo người dùng
  nếu prompt chứa tên khách hàng, số liệu tài chính chưa công bố, hay thông tin bảo mật

### Sau khi người dùng mang câu trả lời về

Đừng nhận nguyên. Sàng theo 3 bước:
1. Phần nào **khớp** với dữ liệu ta có → giữ, nâng độ chắc chắn
2. Phần nào **mâu thuẫn** → nêu rõ mâu thuẫn, ta tin dữ liệu của ta hơn
3. Phần nào **không kiểm chứng được bằng dữ liệu hiện có** → xếp vào giả thuyết cần test,
   không đưa thành finding

---

## Gợi ý hành động (áp dụng cho cả hai chế độ)

Mọi recommendation đưa ra phải:
- Xuất phát từ một insight cụ thể (ghi rõ insight nào)
- Theo SMART: Specific, Measurable, Achievable, Realistic, Timely
- Chia pha: short term (gấp, dễ làm) vs long term (khó, thay đổi cuộc chơi)
- Ghi rõ cần nguồn lực gì và đo thành công bằng metric nào

Không có insight đỡ lưng thì không đưa recommendation — nói thẳng là chưa đủ cơ sở.
