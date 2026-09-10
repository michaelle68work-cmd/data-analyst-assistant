---
name: search
description: Tra cứu kiến thức từ web hoặc từ kiến thức chung của AI để bổ trợ phân tích. Trigger khi user hỏi "search giúp tôi", "tìm hiểu về", "benchmark ngành này là bao nhiêu", "đối thủ đang làm gì", hoặc cần thông tin không có trong domain knowledge và dataset.
---

# Search — Tra cứu kiến thức bổ trợ

Dùng khi cần thông tin nằm ngoài domain file và dataset hiện có.

## LUẬT: kết quả search KHÔNG tự động thành chân lý

Kiến thức từ search là **tham khảo**, đứng ở tầng thấp hơn:

```
1. Dataset của người dùng          ← chân lý cao nhất
2. Domain knowledge đã xác nhận    ← chân lý cho phiên làm việc
3. Kết quả web search              ← tham khảo, phải ghi nguồn
4. Kiến thức chung của AI          ← tham khảo, phải nói rõ là suy đoán
```

Không bao giờ dùng tầng 3-4 để lật đổ tầng 1-2 mà không báo người dùng.

## Quy trình

1. **Làm rõ câu hỏi** — cần biết chính xác điều gì, để phục vụ quyết định nào.
2. **Chọn kênh**:
   - Số liệu, sự kiện, benchmark, tin thị trường, động thái đối thủ → **web search** (bắt buộc)
   - Khái niệm, phương pháp luận, định nghĩa framework → kiến thức chung là đủ
   - Số liệu nội bộ ngành không công khai → nói thẳng là không tra được
3. **Ưu tiên nguồn**: báo cáo của tổ chức nghiên cứu > báo chí kinh tế uy tín >
   blog ngành > nội dung marketing của nhà cung cấp. Ưu tiên nguồn ≤ 2 năm.
4. **Đối chiếu chéo** — số liệu quan trọng cần ≥ 2 nguồn độc lập. Lệch nhau → nêu cả hai.

## Định dạng trả về bắt buộc

```
CÂU HỎI: <đang tìm gì>

PHÁT HIỆN
  • <thông tin> — Nguồn: <tên>, <năm>, <link>
  • <thông tin> — Nguồn: <tên>, <năm>, <link>

TỪ KIẾN THỨC CHUNG (không có nguồn kiểm chứng)
  • <nội dung> — mức tin cậy: cao/trung bình/thấp

KHÔNG TÌM ĐƯỢC
  • <điều gì> — vì sao

ÁP DỤNG THẾ NÀO
  <liên hệ ngược về analysis objective đang làm>
```

## Sau khi search

- Thông tin đáng giữ lâu dài → hỏi người dùng có muốn nạp vào domain file qua
  skill `input-knowledge` không. Không tự ghi vào domain file.
- Không tìm được thì nói "không tìm được", tuyệt đối không lấp bằng số ước lượng.
