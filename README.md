# Data Analyst & BI Assistant

Trợ lý Data Analyst / Business Intelligence chạy trên Claude Code. Biến data thô thành
insight và recommendation có chứng cứ, theo quy trình 7 bước chuẩn của data analysis.

## Kiến trúc

Orchestrator (`CLAUDE.md`) điều phối 4 agent tuần tự, mỗi agent chạy trong context riêng
và chỉ trả ra outcome của bước mình:

| Agent | Bước | Outcome | Gate |
|---|---|---|---|
| `context` | 1. Define CLEAR objectives | `00-objective.md` | Sign-off objective |
| `data` | 2-3. Collect + Validate & CLEAN | `01-data-audit.md` | Xác nhận cleaning log |
| `analysis` | 4-5. Analyze + Interpret | `02-analysis.md`, `03-insights.md` | Trả lời câu hỏi ⚠️ CẦN LÀM RÕ |
| `story` | 6-7. Visualize + Storytelling | `04-report.md` | — |

`docreader` là agent phụ trợ: đọc PDF/deck nhiều chart (Kantar, Nielsen, agency report)
trong context riêng ở 300dpi, trả về chart inventory đầy đủ.

## Skill

| Skill | Dùng khi |
|---|---|
| `da-context` · `da-data` · `da-analysis` · `da-story` | 7 bước phân tích |
| `input-knowledge` | Nạp domain knowledge từ tài liệu của bạn |
| `search` | Tra cứu web / kiến thức chung để bổ trợ |
| `recommendation` | Phản biện insight, hoặc sinh prompt hỏi LLM khác |

## Domain-driven

Trợ lý không dùng kiến thức chung làm chân lý. Trước mỗi phiên, người dùng chọn một
domain trong `domain-knowledge/`; file đó là nguồn chân lý cho cả phiên.

Thứ bậc chân lý:

```
1. Dataset của người dùng                          ← cao nhất
2. Domain knowledge (digest từ tài liệu người dùng)
3. Kết quả web search (phải ghi nguồn)             ← tham khảo
4. Kiến thức chung của AI                          ← tham khảo, phải nói rõ là suy đoán
```

Kiến thức tầng 3-4 không bao giờ tự động ghi vào domain file — phải qua vòng xác nhận
của người dùng.

Thêm lĩnh vực mới (finance, ecommerce, tech...): chạy skill `input-knowledge` và đưa
tài liệu vào. Domain file được digest **từ tài liệu bạn cung cấp**, không phải từ kiến
thức sẵn có của model.

## Nguyên tắc chống mất thông tin

- **Đọc đúng > tiết kiệm token.** PDF đọc ở ≥300dpi, không dùng ảnh DPI thấp để loại trang,
  không trích số từ text extraction.
- **Nén = tách file + có index + có đường quay lại nguồn**, không bao giờ là viết ngắn lại.
- **Mọi insight phải có chứng cứ** (Chart ID / bảng / script). Không truy được nguồn → không viết ra.
- **Không đủ cơ sở thì hỏi, đừng kết luận** — trả về block ⚠️ CẦN LÀM RÕ.

## Cấu trúc

```
CLAUDE.md              # Orchestrator
.claude/agents/        # 5 agent
.claude/skills/        # 7 skill
.claude/commands/      # /analyze
domain-knowledge/      # Chân lý domain (digest từ tài liệu người dùng)
scripts/pdfkit.py      # doctor / index / pages / render — đọc PDF xác định
data/                  # Dataset thô (gitignored)
analyses/<dự-án>/      # Kết quả từng phiên (gitignored)
```

## Bắt đầu

```
/analyze                    # Phiên phân tích mới
/input-knowledge            # Nạp domain knowledge mới
python3 scripts/pdfkit.py doctor
```

Yêu cầu: `pymupdf` (`pip install pymupdf`) để đọc PDF.
