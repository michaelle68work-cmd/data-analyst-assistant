---
name: da-story
description: Bước 6-7/7 - Trực quan hoá đúng cách và kể câu chuyện dữ liệu thuyết phục với recommendation hành động được. Trigger khi cần vẽ chart, dựng dashboard, viết report, executive summary, hay trình bày kết quả phân tích.
---

# Bước 6 — PROPER Visualization & Bước 7 — Tell A GOOD STORY

## Bước 6 — Visualization

Luôn dùng skill `dataviz` khi vẽ bất kỳ biểu đồ nào.

Chọn chart theo thông điệp, không theo thói quen:

| Thông điệp muốn truyền | Chart |
|---|---|
| Diễn biến theo thời gian | Line, area |
| So sánh giữa các hạng mục | Bar ngang (nhiều mục), column (ít mục) |
| Cơ cấu / đóng góp | Stacked bar, treemap (hạn chế pie, tối đa 3-4 lát) |
| Phân bố | Histogram, box plot |
| Quan hệ 2 biến | Scatter |
| Biến động từ A tới B | Waterfall |
| Tiến độ qua các bước | Funnel |
| Giữ chân theo nhóm thời gian | Cohort heatmap |

Quy tắc:
- Mỗi chart chỉ tải **một** thông điệp. Title của chart chính là thông điệp đó
  ("Doanh thu SKU#2 giảm 18% từ T4"), không phải nhãn dữ liệu ("Doanh thu theo tháng").
- Luôn có đường tham chiếu: target, benchmark, kỳ trước, hoặc đối thủ.
- Highlight phần cần chú ý bằng màu, phần còn lại để xám.
- Bỏ mọi thứ không phục vụ thông điệp.

## Bước 7 — Storytelling

### Cấu trúc trình bày (khác với thứ tự phân tích)

Phân tích đi theo vòng lặp; trình bày đi theo dòng chảy tuyến tính:

```
EXECUTIVE SUMMARY  (viết sau cùng, đọc đầu tiên)
  ↓
BUSINESS BACKGROUND → ANALYSIS OBJECTIVES → HYPOTHESES
  ↓
SITUATION (indicators)
  ↓
DEEP DIVE / EXPLORATION (topics → metrics/hypotheses → findings)
  ↓
INSIGHTS
  ↓
RECOMMENDATIONS
```

### KEY FINDINGS
- Ưu tiên finding trả lời trực tiếp objective
- Chỉ ra "CORE" area of focus — dùng framework marketing làm kim chỉ nam
- Giữ đơn giản: **1-2 take-away chính**, tối đa 3

### RECOMMENDATIONS
- **Mọi recommendation phải đi thẳng ra từ finding.** Không có finding đỡ lưng thì bỏ.
- Nghĩ cho business tổng thể: sếp lớn có sẵn sàng ủng hộ không, tác động sang phòng ban khác ra sao
- Chia pha: **short term** (gấp, dễ sửa) và **long term** (khó, thay đổi cuộc chơi)
- Theo SMART: Specific, Measurable, Achievable, Realistic, Timely

### Thế nào là một phân tích thành công

1. Insight hay và độc đáo — đủ sức dẫn tới quyết định kinh doanh tốt
2. Trả lời **chính xác toàn bộ** analysis objectives
3. Súc tích và đầy đủ — dồn sự chú ý vào dưới 3 key findings
4. Hợp lệ và hành động được — kèm recommendation và action plan

## Output

Ghi vào `analyses/<dự-án>/04-report.md`. Khi người dùng cần chia sẻ, publish thành Artifact.
