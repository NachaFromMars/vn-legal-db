#!/usr/bin/env python3
"""
VN Legal DB — Offline law lookup tool.
Search Vietnamese legal codes by article number, keyword, or topic.

Usage:
  python3 lookup.py article 226 BLHS          # Lookup Điều 226 BLHS
  python3 lookup.py article 175 BLHS          # Lookup Điều 175 BLHS
  python3 lookup.py search "sở hữu trí tuệ"  # Search keyword across all laws
  python3 lookup.py search "lạm dụng" BLHS    # Search within specific law
  python3 lookup.py list                       # List available laws
  python3 lookup.py stats                      # Show database stats
"""

import sys
import os
import re
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(SCRIPT_DIR, "..", "references")

LAW_FILES = {
    "BLHS": ("BLHS-2015-2017.md", "Bộ luật Hình sự 2015 (sửa đổi 2017)"),
    "SHTT": ("Luat-SHTT-2005.md", "Luật Sở hữu trí tuệ 2005 (sửa đổi 2022)"),
    "BLDS": ("BLDS-2015.md", "Bộ luật Dân sự 2015"),
    "BLLD": ("BLLD-2019.md", "Bộ luật Lao động 2019"),
    "BLTTHS": ("BLTTHS-2015.md", "Bộ luật Tố tụng hình sự 2015 (sửa đổi 2021)"),
}

# Aliases
LAW_ALIASES = {
    "HINHSU": "BLHS", "HS": "BLHS", "HINH_SU": "BLHS",
    "DANSU": "BLDS", "DS": "BLDS", "DAN_SU": "BLDS",
    "LAODONG": "BLLD", "LD": "BLLD", "LAO_DONG": "BLLD",
    "TOTUNG": "BLTTHS", "TT": "BLTTHS", "TTHS": "BLTTHS",
    "SHTT": "SHTT", "SOHUUTRITUE": "SHTT",
}

def resolve_law(code):
    """Resolve law code alias to canonical name."""
    code = code.upper().replace(" ", "").replace("-", "")
    if code in LAW_FILES:
        return code
    return LAW_ALIASES.get(code, None)

def load_law(code):
    """Load law text from file."""
    if code not in LAW_FILES:
        return None
    filepath = os.path.join(REF_DIR, LAW_FILES[code][0])
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def lookup_article(article_num, law_code=None):
    """Find a specific article (Điều) by number."""
    results = []
    laws_to_search = [law_code] if law_code else list(LAW_FILES.keys())
    
    pattern = re.compile(
        rf'(Điều\s+{article_num}[a-z]?\.\s+[^\n]+(?:\n(?!Điều\s+\d)[^\n]*)*)',
        re.MULTILINE
    )
    
    for code in laws_to_search:
        text = load_law(code)
        if not text:
            continue
        matches = pattern.findall(text)
        for match in matches:
            # Trim to reasonable length (first 3000 chars)
            trimmed = match[:3000]
            if len(match) > 3000:
                trimmed += f"\n\n... [cắt bớt, tổng {len(match):,} ký tự]"
            results.append({
                "law": code,
                "law_name": LAW_FILES[code][1],
                "text": trimmed.strip()
            })
    
    return results

def search_keyword(keyword, law_code=None, context_lines=3, max_results=20):
    """Search keyword across laws, return matching paragraphs."""
    results = []
    laws_to_search = [law_code] if law_code else list(LAW_FILES.keys())
    
    for code in laws_to_search:
        text = load_law(code)
        if not text:
            continue
        
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if keyword.lower() in line.lower():
                # Get context
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                context = "\n".join(lines[start:end])
                results.append({
                    "law": code,
                    "law_name": LAW_FILES[code][1],
                    "line": i + 1,
                    "context": context.strip()
                })
                if len(results) >= max_results:
                    break
        
        if len(results) >= max_results:
            break
    
    return results

def show_stats():
    """Show database statistics."""
    print("📚 VN Legal DB — Thống Kê")
    print("=" * 50)
    total_size = 0
    total_articles = 0
    for code, (filename, name) in LAW_FILES.items():
        filepath = os.path.join(REF_DIR, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            total_size += size
            with open(filepath, "r") as f:
                text = f.read()
            articles = len(re.findall(r'Điều\s+\d+[a-z]?\.', text))
            total_articles += articles
            print(f"  {code:8s} | {name:50s} | {size/1024:7.0f} KB | {articles:4d} điều")
        else:
            print(f"  {code:8s} | ❌ MISSING")
    print("=" * 50)
    print(f"  {'TỔNG':8s} | {'':50s} | {total_size/1024:7.0f} KB | {total_articles:4d} điều")

def main():
    parser = argparse.ArgumentParser(description="VN Legal DB — Tra cứu luật VN offline")
    sub = parser.add_subparsers(dest="command")
    
    # article
    p_art = sub.add_parser("article", aliases=["dieu", "a"], help="Tra cứu điều luật theo số")
    p_art.add_argument("number", help="Số điều (vd: 226, 175)")
    p_art.add_argument("law", nargs="?", default=None, help="Mã luật (BLHS, SHTT, BLDS, BLLD, BLTTHS)")
    
    # search
    p_search = sub.add_parser("search", aliases=["tim", "s"], help="Tìm từ khóa")
    p_search.add_argument("keyword", help="Từ khóa tìm kiếm")
    p_search.add_argument("law", nargs="?", default=None, help="Mã luật (tùy chọn)")
    p_search.add_argument("--max", type=int, default=20, help="Số kết quả tối đa")
    p_search.add_argument("--context", type=int, default=3, help="Số dòng context")
    
    # list
    sub.add_parser("list", aliases=["ls"], help="Liệt kê các bộ luật")
    
    # stats
    sub.add_parser("stats", help="Thống kê database")
    
    args = parser.parse_args()
    
    if args.command in ("article", "dieu", "a"):
        law = resolve_law(args.law) if args.law else None
        if args.law and not law:
            print(f"❌ Không tìm thấy luật '{args.law}'. Dùng: BLHS, SHTT, BLDS, BLLD, BLTTHS")
            sys.exit(1)
        
        results = lookup_article(args.number, law)
        if not results:
            print(f"❌ Không tìm thấy Điều {args.number}" + (f" trong {law}" if law else ""))
            sys.exit(1)
        
        for r in results:
            print(f"\n📖 {r['law']} — {r['law_name']}")
            print("─" * 50)
            print(r['text'])
            print()
    
    elif args.command in ("search", "tim", "s"):
        law = resolve_law(args.law) if args.law else None
        results = search_keyword(args.keyword, law, args.context, args.max)
        
        if not results:
            print(f"❌ Không tìm thấy '{args.keyword}'" + (f" trong {law}" if law else ""))
            sys.exit(1)
        
        print(f"🔍 Tìm thấy {len(results)} kết quả cho '{args.keyword}':\n")
        for i, r in enumerate(results, 1):
            print(f"[{i}] {r['law']} dòng {r['line']} — {r['law_name']}")
            print("─" * 50)
            print(r['context'])
            print()
    
    elif args.command in ("list", "ls"):
        print("📚 Bộ Luật VN Offline:")
        for code, (filename, name) in LAW_FILES.items():
            filepath = os.path.join(REF_DIR, filename)
            status = "✅" if os.path.exists(filepath) else "❌"
            print(f"  {status} {code:8s} — {name}")
        print(f"\nAlias: HS=BLHS, DS=BLDS, LD=BLLD, TT=BLTTHS")
    
    elif args.command == "stats":
        show_stats()
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
