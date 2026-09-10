---
name: da-analysis
description: Bước 4-5/7 - Phân tích dữ liệu và diễn giải thành insight. Bao gồm đọc báo cáo có sẵn từ bên ngoài (Kantar, Nielsen, GfK, agency deck, PDF có chart). Trigger khi data đã sạch và cần tính toán, segment, tìm nguyên nhân, dự báo, đọc chart trong file báo cáo, hoặc rút ra finding/insight.
---

# Bước 4 — Apply APPROPRIATE Analysis & Bước 5 — Interpret MEANINGFUL Information

Khoảng 80% business analytics thực tế chỉ là mô tả dựa trên tổng hợp hiệu quả quá khứ.
Đừng nhảy vào model phức tạp khi descriptive đã trả lời được objective.

---

## PHẦN A — Phân tích data thô

### Chọn kỹ thuật theo loại câu hỏi

**DESCRIPTIVE — "Chuyện gì đã xảy ra?"**
- Aggregation: sum, avg, median, distribution, share of total
- Time series: trend, YoY / MoM / QoQ, moving average, seasonality
- Ranking: top/bottom N, Pareto 80/20

**DIAGNOSTIC — "Tại sao? Nên đào đâu?"**
- Drill-down theo cây phân cấp: market → channel → category → SKU
- Segmentation theo customer group, channel, geography, thời gian
- Contribution / variance analysis
- Correlation (nhắc rõ: tương quan ≠ nhân quả)
- Funnel & conversion analysis, cohort analysis

**PREDICTIVE — "Sắp tới sẽ ra sao?"**
- Trend line, baseline, seasonal decomposition
- Forecast: moving average, exponential smoothing, regression
- Luôn kèm khoảng tin cậy và giả định đầu vào

**PRESCRIPTIVE — "Nên làm gì?"**
- Cost/benefit analysis, what-if scenarios
- Optimization phân bổ budget / mix kênh
- Simulation, A-B test design

### Nguyên tắc thực thi

1. Bám framework đã chốt ở bước 1 — mỗi nhánh của cây là một phép tính.
2. Kiểm chứng từng hypothesis tường minh: accept hay reject, bằng số nào.
3. Mỗi con số phải có **mẫu số và bối cảnh**.
4. Viết code, không tính nhẩm. Lưu script vào `analyses/<dự-án>/scripts/`.
5. Sanity check: tổng các phần có bằng tổng thể? Số có khớp nguồn gốc?

---

## PHẦN B — Đọc báo cáo có sẵn từ bên ngoài

Áp dụng khi người dùng đưa file báo cáo đã hoàn chỉnh: Kantar, Nielsen, GfK, Ipsos,
agency deck, MR report, PDF/PPT có chart.

### LUẬT: đọc đúng quan trọng hơn tiết kiệm token

- **Giao việc đọc PDF cho agent `docreader`** (context riêng). Không tự đọc 20-40 ảnh
  trong context chính.
- **Cấm** trích số từ text extraction — text mất layout, "chart là ảnh" ra rỗng,
  số bị tách khỏi cột của nó, mất màu phân biệt series.
- **Cấm** dùng contact sheet / ảnh DPI thấp để quyết định bỏ trang.
- Mọi con số đưa vào phân tích phải được `docreader` đọc từ ảnh **≥300dpi** của đúng trang.
- Trang nghi ngờ có nội dung → đọc. Chỉ bỏ bìa/agenda/mục lục/divider/lời cảm ơn.

### Quy trình

1. Gọi agent `docreader` với đường dẫn file → nhận về `02a-chart-inventory.md`
   (bảng: mỗi chart có ID, trục, đơn vị, kỳ, base size, mọi giá trị, text đè trên chart,
   chú thích, và kết luận in sẵn trên slide nếu có).
2. Chỉ đọc file inventory đó, không đọc lại ảnh.
3. **Đọc số của chính bạn trước, đọc kết luận của báo cáo sau.** Kết luận của Kantar/agency
   là **tham khảo**, không phải chân lý. Thấy khác → nêu cả hai, giải thích vì sao khác.
4. Kiểm methodology: base size, thời điểm khảo sát, phạm vi địa lý, cách chọn mẫu,
   định nghĩa metric của nhà cung cấp có khớp định nghĩa trong domain file không.

### Cảnh báo bắt buộc nêu ra (docreader đã đánh dấu, bạn phải chuyển tiếp)

- Base size nhỏ (thường < 50) → không kết luận trên nhóm đó
- Định nghĩa metric của agency lệch định nghĩa nội bộ → không trộn số
- Chart bị cắt trục Y (không bắt đầu từ 0) → biến động trông to hơn thực tế
- Số liệu cũ so với kỳ đang phân tích → nêu độ trễ
- Chỗ `docreader` ghi `[không đọc được]` → coi như thiếu data, không suy đoán

---

## PHẦN C — Diễn giải thành insight (bước 5)

Data → Information là kỹ thuật. Information → Knowledge là **context**.

### Bài học gốc

Sales 6 tháng đầu 2020: `100, 120, 135, 70, 65, 55`
→ Kết luận vội: "Đội sales tụt hiệu suất từ tháng 4 và ngày càng tệ."

Nhưng nếu biết thêm: Q2 năm nào cũng thấp nhất vì nóng · toàn ngành giảm từ T4 do quy định
mới ban hành T3 · Q1 đã thuê thêm 30% part-time sales và vượt 20% ngân sách marketing
→ kết luận ngược lại hoàn toàn. **Không có context thì không có insight.**

### Quy trình đọc 5 bước

**1. COMPREHEND** — hiểu từng metric được đo thế nào, hàm ý gì
**2. COMPARE** — *đừng bao giờ tin con số đứng một mình*. So theo thời gian, trong danh sách,
với đối thủ, với benchmark ngành, với target. Tìm trend, min/max, bottleneck, rate of change.
**3. DEEP DIVE** — bóc xuống cấp thấp nhất: market → category → sub-cat → variant → SKU.
Lọc theo consumer group, kênh, thị trường. Với feedback định tính: hỏi "họ thực sự muốn nói gì?"
**4. CONNECT** — gom data/chart liên quan thành "theme" hoàn chỉnh
(customer profile ↔ U&A ↔ sales growth ↔ market share). Đặt vào bối cảnh ngành và thị trường.
**5. RECONFIRM** — đối chiếu qua nhiều nguồn, tự phản biện tới khi bị thuyết phục,
kết luận hypothesis accept/reject.

### QUY TẮC CHỨNG CỨ — bắt buộc, không ngoại lệ

**Mỗi insight phải ghi rõ nó dựa trên chart/bảng/nguồn nào.** Định dạng bắt buộc:

```
INSIGHT #n: <phát biểu>
  Chứng cứ: [Chart ID / bảng / script] — chỉ rõ số nào trên đó
  Context: <bối cảnh làm cho con số này có nghĩa>
  Độ chắc chắn: CAO / TRUNG BÌNH / THẤP
```

Insight không truy được về một chart hoặc bảng cụ thể thì **không được viết ra**.

### QUY TẮC KHÔNG ĐỦ CƠ SỞ — khi nào phải trả về câu hỏi thay vì kết luận

Nếu rơi vào bất kỳ tình huống nào dưới đây, **cấm tự kết luận**. Thay vào đó trả ra
mục "CẦN LÀM RÕ" dưới dạng câu hỏi kèm cảnh báo:

- Chỉ có một nguồn/một chart cho một hiện tượng, không có data khác đỡ lưng
- Thấy biến động nhưng không có dữ liệu giải thích nguyên nhân
- Có nhiều cách giải thích hợp lý mà data hiện có không phân biệt được
- Metric cần dùng không có trong domain file và bạn không chắc định nghĩa
- Base size / kỳ dữ liệu không đủ để đọc

Định dạng bắt buộc:

```
⚠️ CẦN LÀM RÕ #n
  Quan sát được: <hiện tượng, kèm Chart ID>
  Thiếu gì: <dữ liệu/thông tin còn thiếu để kết luận>
  Câu hỏi cho bạn: <câu hỏi cụ thể>
  Nếu có <data X> thì tôi sẽ khẳng định được <điều gì>
```

Ví dụ: *Chart K-p12-c1 cho thấy tỷ lệ chuyển từ awareness sang consideration tụt từ 42%
xuống 28% trong Q2. Nhưng không có data nào khác support cho sự sụt giảm này — không có
số về thay đổi creative, giá, hay động thái đối thủ trong kỳ. Tôi không kết luận nguyên nhân.
Câu hỏi: có thay đổi gì về thông điệp truyền thông hoặc giá trong Q2 không?*

Thà trả về 1 insight chắc chắn + 3 câu hỏi, còn hơn 4 kết luận đoán mò.

### Checklist trước khi gọi một câu là "insight"

- [ ] Có Chart ID / bảng cụ thể làm chứng cứ
- [ ] Có context, không chỉ mô tả lại số
- [ ] Trả lời trực tiếp analysis objective
- [ ] Đã xác nhận chéo ít nhất 2 nguồn hoặc 2 góc cắt
- [ ] Đã loại trừ các giải thích thay thế hiển nhiên
- [ ] Dẫn tới được một hành động cụ thể

## Output (chỉ trả ra đúng bước này)

`analyses/<dự-án>/02-analysis.md` — chart inventory · từng hypothesis + phương pháp + kết quả + verdict
`analyses/<dự-án>/03-insights.md` — tối đa 3 insight (đúng định dạng chứng cứ) + toàn bộ mục ⚠️ CẦN LÀM RÕ

**Không** vẽ chart trình bày, **không** viết recommendation. Đó là bước 6-7.
Dừng lại để người dùng trả lời các câu hỏi CẦN LÀM RÕ trước khi sang bước sau.
