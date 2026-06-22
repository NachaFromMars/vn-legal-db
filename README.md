---
name: vn-legal-db
description: "Tra cứu bộ luật Việt Nam offline. 5 bộ luật chính: BLHS 2015 (sửa đổi 2017), Luật SHTT 2005 (sửa đổi 2022), BLDS 2015, BLLĐ 2019, BLTTHS 2015 (sửa đổi 2021). Tổng 4.4 MB, 72K+ dòng. Use when: (1) tra cứu điều luật VN cụ thể, (2) tìm căn cứ pháp lý cho vụ việc, (3) phân tích pháp lý theo luật VN, (4) trích dẫn điều khoản luật VN, (5) so sánh các điều luật. Triggers: luật VN, điều luật, bộ luật hình sự, BLHS, luật dân sự, BLDS, sở hữu trí tuệ, SHTT, lao động, BLLĐ, tố tụng, pháp lý, legal Vietnam, Vietnamese law."
---

# VN Legal DB — Bộ Luật Việt Nam Offline

## Database (references/)

| Mã | File | Nội dung | Size |
|----|------|----------|------|
| BLHS | BLHS-2015-2017.md | Bộ luật Hình sự 2015 (sửa đổi 2017) — 26 chương | 852 KB |
| SHTT | Luat-SHTT-2005.md | Luật SHTT 2005 (bản 2009 + 2019 + **2022 mới nhất**) | 1.4 MB |
| BLDS | BLDS-2015.md | Bộ luật Dân sự 2015 — 6 phần | 503 KB |
| BLLD | BLLD-2019.md | Bộ luật Lao động 2019 — 17 chương | 259 KB |
| BLTTHS | BLTTHS-2015.md | Bộ luật Tố tụng hình sự 2015 (sửa đổi 2021) | 1.4 MB |

**Nguồn:** vi.wikisource.org (Wikimedia Foundation) — Tải 16/03/2026

## CLI Tra Cứu (scripts/lookup.py)

```bash
# Tra điều luật theo số
python3 scripts/lookup.py article 226 BLHS      # Điều 226 BLHS
python3 scripts/lookup.py article 175 BLHS      # Điều 175 BLHS
python3 scripts/lookup.py article 130 SHTT      # Điều 130 Luật SHTT

# Tìm từ khóa
python3 scripts/lookup.py search "sở hữu công nghiệp"        # Tất cả luật
python3 scripts/lookup.py search "lạm dụng tín nhiệm" BLHS   # Chỉ BLHS
python3 scripts/lookup.py search "bồi thường" BLDS            # Chỉ BLDS

# Liệt kê / thống kê
python3 scripts/lookup.py list
python3 scripts/lookup.py stats
```

**Alias:** HS=BLHS, DS=BLDS, LD=BLLD, TT=BLTTHS

## Workflow Tra Cứu

1. Xác định vấn đề pháp lý → chọn bộ luật phù hợp
2. Tra điều luật cụ thể: `article <số> <mã luật>`
3. Hoặc tìm từ khóa: `search "<từ khóa>" [mã luật]`
4. Trích dẫn: ghi rõ **Điều X, Khoản Y, Bộ luật Z (sửa đổi năm)**
5. Nếu cần đọc nguyên văn dài: `read references/BLHS-2015-2017.md --offset <line>`

## Lưu Ý Quan Trọng

- Luật SHTT có 3 phiên bản: **dùng bản 2022** (mới nhất) khi tư vấn
- Nguồn WikiSource có thể thiếu sửa đổi nhỏ — verify trên thuvienphapluat.vn cho case quan trọng
- Đây là công cụ **tham khảo**, không thay thế luật sư chuyên nghiệp
- Khi trích dẫn, LUÔN ghi đầy đủ: `Điều X, Khoản Y, [Tên luật] số [XX/năm/QH]`
