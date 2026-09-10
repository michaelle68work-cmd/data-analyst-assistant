#!/usr/bin/env python3
"""pdfkit — công cụ đọc PDF xác định cho agent phân tích.

Nguyên tắc: chỉ hỗ trợ TRIAGE (biết trang nào nói gì) và RENDER ĐỘ PHÂN GIẢI CAO.
Không có lệnh nào trích số liệu — số liệu chỉ được đọc bằng mắt từ ảnh 300dpi.

Cách dùng:
  pdfkit.py doctor
  pdfkit.py index <file.pdf>                # bảng: trang | text có trên trang (rút gọn)
  pdfkit.py pages <file.pdf>                # tổng số trang + gợi ý trang nội dung
  pdfkit.py render <file.pdf> <spec> [dpi]  # spec: "12" | "12,18,23" | "5-40" | "all"
                                           # dpi mặc định 300. Ảnh ra scratchpad.
"""
import sys, os, re, hashlib

OUT = os.environ.get("PDFKIT_OUT") or "/tmp/pdfkit"

def _fitz():
    try:
        import fitz
        return fitz
    except ImportError:
        sys.exit("THIẾU pymupdf. Cài: pip install pymupdf")

def doctor():
    ok = []
    for m in ("fitz", "pypdf"):
        try:
            __import__(m); ok.append(f"  [OK] {m}")
        except ImportError:
            ok.append(f"  [--] {m} (không bắt buộc nếu có fitz)")
    print("pdfkit doctor")
    print("\n".join(ok))
    print(f"  OUT dir: {OUT}")

SKIP = re.compile(r"\b(agenda|mục lục|table of contents|thank you|cảm ơn|contents|disclaimer only|title slide)\b", re.I)

def index(path):
    fitz = _fitz()
    d = fitz.open(path)
    print(f"# {os.path.basename(path)} — {d.page_count} trang\n")
    print("trang | dài(char) | trích text đầu trang")
    print("------|-----------|---------------------")
    for i, p in enumerate(d):
        t = " ".join(p.get_text().split())
        head = t[:110].replace("|", "/")
        print(f"{i+1:>5} | {len(t):>9} | {head}")
    print("\nGhi chú: cột 'dài' NHỎ mà trang vẫn có nội dung => nhiều khả năng là "
          "chart dạng ảnh, PHẢI render để đọc. Đừng loại trang chỉ vì text ngắn.")

def pages(path):
    fitz = _fitz()
    d = fitz.open(path)
    content = []
    for i, p in enumerate(d):
        t = " ".join(p.get_text().split())
        if SKIP.search(t) and len(t) < 200:
            continue
        content.append(i + 1)
    print(f"Tổng: {d.page_count} trang")
    print(f"Trang nội dung nên đọc ({len(content)}): "
          + (",".join(map(str, content)) if content else "(không xác định — đọc TẤT CẢ)"))
    print("Quy tắc: trang nghi ngờ thì GIỮ. Chỉ bỏ bìa/agenda/divider/lời cảm ơn.")

def _spec(spec, n):
    if spec == "all":
        return list(range(1, n + 1))
    out = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        elif part:
            out.add(int(part))
    return sorted(x for x in out if 1 <= x <= n)

def render(path, spec, dpi=300):
    fitz = _fitz()
    dpi = int(dpi)
    d = fitz.open(path)
    tag = hashlib.md5(os.path.abspath(path).encode()).hexdigest()[:8]
    dst = os.path.join(OUT, f"{os.path.splitext(os.path.basename(path))[0]}_{tag}")
    os.makedirs(dst, exist_ok=True)
    m = fitz.Matrix(dpi / 72, dpi / 72)
    files = []
    for pg in _spec(spec, d.page_count):
        f = os.path.join(dst, f"p{pg:03d}_{dpi}dpi.png")
        d[pg - 1].get_pixmap(matrix=m).save(f)
        files.append(f)
    print(f"Render {len(files)} trang @ {dpi}dpi -> {dst}")
    for f in files:
        print(f"  {f}")
    print("\nĐọc từng ảnh này bằng Read. MỌI con số đưa vào insight phải đọc từ đây, "
          "KHÔNG từ lệnh index.")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    cmd = a[0]
    if cmd == "doctor": doctor()
    elif cmd == "index": index(a[1])
    elif cmd == "pages": pages(a[1])
    elif cmd == "render": render(a[1], a[2], a[3] if len(a) > 3 else 300)
    else: sys.exit(f"Lệnh lạ: {cmd}\n{__doc__}")
