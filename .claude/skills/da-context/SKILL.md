---
name: da-context
description: Bước 1/7 - Dựng context và chốt mục tiêu phân tích rõ ràng trước khi đụng vào data. Trigger khi user nói "phân tích giúp tôi", "tại sao doanh số giảm", "xem data này", hoặc bất kỳ yêu cầu phân tích nào chưa có objective được chốt.
---

# Bước 1 — Context & Define CLEAR Objectives

"The right question asked is already half the answer found."
Không có objective rõ ràng thì: không bao giờ xong việc, và gần như chắc chắn trượt mục tiêu.

## Bắt buộc làm

1. **Đọc domain knowledge** đã chọn — lấy business context, KPI chuẩn, benchmark.
   Nếu domain file trống hoặc thiếu mục cần dùng → dừng, báo người dùng nạp qua
   skill `input-knowledge`. **Không tự lấp bằng kiến thức chung.**
2. **Hỏi lại business background** nếu chưa rõ: chuyện gì đang xảy ra, ai cần kết quả này,
   quyết định nào sẽ được đưa ra sau khi có kết quả.
3. **Viết Analysis Objective** theo checklist dưới.
4. **Xin sign-off** — người dùng phải xác nhận trước khi sang bước 2.

## Analysis Objective Checklist

- [ ] Câu hỏi rõ ràng, súc tích, đầy đủ (1 câu)
- [ ] Metrics đo được — liệt kê tên metric + công thức (công thức lấy từ domain file)
- [ ] Có nền business vững — gắn với tình hình thực tế
- [ ] Link tới Marketing/Business Objective dạng SMART
- [ ] Hypotheses để kiểm chứng (khuyến khích, 2-4 giả thuyết)

## Mapping Business Objective → Analysis Objective

| Business Objective | Analysis Objective |
|---|---|
| Giữ tăng trưởng 10% YoY | Revenue đang diễn biến ra sao trong các kỳ gần đây? |
| Chiếm 45% market share trong 1 năm | Target này có khả thi không, dựa trên cơ sở nào? |
| Giữ margin ≥30% ở 3 thành phố chính | Vì sao một thành phố tụt dưới 30%? |

## Xác định loại phân tích cần dùng

- "Bao nhiêu / khi nào / ở đâu / chuyện gì đã xảy ra?" → **Descriptive**
- "Tại sao / nên đào sâu chỗ nào?" → **Diagnostic**
- "Sắp tới sẽ thế nào?" → **Predictive**
- "Nên chọn phương án nào / nếu làm X thì sao?" → **Prescriptive**

## Chọn Analytical Framework

Framework = "bản đồ" chống lạc hướng. Chọn 1 và vẽ ra dạng cây trước khi phân tích.

Ưu tiên framework được liệt kê trong `domain-knowledge/<domain>.md`. Nếu domain file
chưa có framework nào, đề xuất từ danh sách chung dưới đây và **nói rõ đây là đề xuất
ngoài tài liệu nguồn, cần người dùng xác nhận**:

- **Revenue / Profitability tree** — bóc doanh thu hoặc lợi nhuận thành các nhánh cấu thành
- **Porter's Five Forces** — độ hấp dẫn & tiềm năng lợi nhuận ngành
- **5C Situation Analysis** — yếu tố nội tại + ngoại cảnh
- **BCG Growth-Share Matrix** — phân bổ nguồn lực giữa SKU/business unit
- **Industry Lifecycle** — dự báo xu hướng ngành, giai đoạn trưởng thành
- **Value Chain / Value Drivers** — cấu trúc chi phí & doanh thu vs ngành
- **McKinsey 7S** — hiệu quả sử dụng nguồn lực nội bộ

## Output (chỉ trả ra đúng bước này)

Ghi vào `analyses/<dự-án>/00-objective.md`:
business background · analysis objective · metrics + công thức · hypotheses ·
framework đã chọn · loại analytics · data cần có ở bước 2 · điểm còn thiếu cần người dùng xác nhận.

**Không** thu thập data, **không** tính toán, **không** kết luận. Dừng lại xin sign-off.
