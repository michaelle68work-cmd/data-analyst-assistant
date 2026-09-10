---
name: da-data
description: Bước 2-3/7 - Thu thập data liên quan và validate + clean data trước khi phân tích. Trigger khi đã chốt objective và bắt đầu đụng vào dataset, file CSV/Excel/database, hoặc khi cần kiểm tra chất lượng dữ liệu.
---

# Bước 2 — Collect RELEVANT Data & Bước 3 — Validate + CLEAN

"Garbage in, garbage out." Đây là công việc thầm lặng nhưng quyết định toàn bộ độ tin cậy.

## Bước 2 — Data Inventory

Với mỗi metric trong objective, xác định nguồn. Tra bảng dưới, đối chiếu với phần
"Data sources" trong domain knowledge file.

| Nhóm | Nguồn INTERNAL | Nguồn EXTERNAL |
|---|---|---|
| Business/Competition | P&L, cash flow, org chart, supply chain | Competitive intelligence |
| Customers | Customer database, CRM, supplier DB | Panel data, 3rd-party audience |
| Sales | Sales report, shipments, distribution network, trade strategy | Retail audit |
| Transactions | Transaction DB, inventory matrix, OOS, turnover | Marketplace data |
| Market research | MR reports cũ, in-house survey, staff survey | Public articles, MR agency |
| Marketing | MKT strategy, spends, KPI tracking, BTL | Ad platform, media monitoring |
| Voice of customer | CRM, hotline, CS mailbox, sales feedback | Social listening, review |

Với mỗi nguồn phải trả lời:
- INTERNAL → có truy cập được không? có bảo mật/chia sẻ được không?
- EXTERNAL → có mất phí không? có đáng tin không? có thực sự cần không?

## Bước 3a — Reliability Check (5 câu hỏi)

- **COMPLIANCE** — Đúng loại data cần? Đủ lượng? Sample size có đủ robust để đọc?
- **SOURCES** — Nội bộ: nguồn có được audit đàng hoàng? Ngoại bộ: nhà cung cấp là ai, quy trình audit của họ có tin được?
- **TIMING** — Data "xảy ra" lúc nào? Được thu thập lúc nào? (hai mốc này thường khác nhau)
- **COVERAGE** — Xảy ra ở đâu? Thu thập ở đâu? Lưu ở đâu?
- **PROCESS** — Thu thập bằng cách nào? Methodology có gì hạn chế (qual/quant/survey/measurement)?

## Bước 3b — Data Cleaning (4 nhóm việc)

**1. Remove unwanted observations**
- Duplicate: hay xảy ra khi gộp nhiều nguồn hoặc nhận data từ phòng ban khác
- Irrelevant: quan sát không thuộc phạm vi bài toán (VD: phân tích chung cư mà có nhà phố)

**2. Fix structural errors**
- Typo, sai syntax, viết hoa không nhất quán: `Morning / morning / MORNING`
- Mã số lệch định dạng: `000313` vs `313`
- Mislabeled classes cần gộp: `N/A` + `Not Applicable`; `M / Male / male / Men`

**3. Filter unwanted outliers**
- Outlier **vô tội cho đến khi bị chứng minh có tội**. KHÔNG xoá chỉ vì "số to bất thường".
- Xoá được: giá trị bất khả thi về mặt logic (chiều cao âm, khối lượng âm)
- Phải giữ và điều tra: doanh thu vọt của một cửa hàng, số khiếu nại dồn vào một chi nhánh
  — đây thường chính là insight.

**4. Handle missing data**
- Hai cách phổ biến nhất đều là bẫy: (1) drop dòng thiếu, (2) impute từ dòng khác.
- **"Missing-ness" tự nó đã là thông tin.** Luôn điều tra vì sao thiếu trước khi xử lý.
- Nêu rõ cách xử lý đã chọn và ảnh hưởng của nó lên kết luận.

## Output

Ghi vào `analyses/<dự-án>/01-data-audit.md`:
data inventory (nguồn + trạng thái truy cập) · kết quả 5 reliability check ·
cleaning log (làm gì, bao nhiêu dòng bị ảnh hưởng, vì sao) · limitation đã biết.

Báo cáo cleaning log cho người dùng và xin xác nhận trước khi sang bước 4.
