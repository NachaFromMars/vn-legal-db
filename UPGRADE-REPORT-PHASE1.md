# UPGRADE REPORT — Phase 1: Án Lệ + Bảng Tra Cứu Pháp Lý
> Ngày: 29/03/2026
> Thực hiện bởi: Sub-agent legal-upgrade-1

---

## Tóm Tắt Kết Quả

### ✅ Bước 1: Tạo thư mục
- `skills/vn-legal-db/references/an-le/` ✓
- `skills/vn-legal-db/references/nghi-dinh/` ✓
- `skills/your-next-lawyer/references/templates/` ✓

### ✅ Bước 2: Án Lệ Việt Nam

**Danh mục tổng hợp:**
- File: `references/an-le/danh-muc-an-le.md`
- Nội dung: **Toàn bộ 82 án lệ** đang có hiệu lực (cập nhật tới QĐ 339/QĐ-CA ngày 24/12/2025)
- Phân loại theo lĩnh vực: Hình sự (~20), Dân sự (~37), Hành chính (4), HN&GĐ (~6), KD-TM (~11), Lao động (~3)
- Bao gồm 10 án lệ mới nhất (73-82/2025/AL) có hiệu lực từ 01/02/2026

**File chi tiết từng án lệ (13 file):**

| File | Lĩnh vực | Lý do chọn |
|------|----------|-----------|
| an-le-01-2016.md | Hình sự | Án lệ đầu tiên, phân biệt Giết người vs CYGTT |
| an-le-04-2016.md | Dân sự | HĐ chuyển nhượng QSDĐ không công chứng — rất phổ biến |
| an-le-05-2016.md | Dân sự | Thừa kế → tài sản chung khi hết thời hiệu |
| an-le-17-2018.md | Hình sự | Tình tiết côn đồ trong đồng phạm |
| an-le-25-2018.md | Dân sự | Phạt cọc vì lý do khách quan — hay gặp trong BĐS |
| an-le-26-2018.md | Dân sự | Thời hiệu chia di sản thừa kế BĐS |
| an-le-28-2019.md | Hình sự | Giết người kích động mạnh (Đ125 vs Đ123) |
| an-le-29-2019.md | Hình sự | Cướp tài sản — cấu thành hình thức |
| an-le-36-2020.md | Dân sự | HĐ thế chấp khi GCN bị thu hồi — quan trọng cho ngân hàng |
| an-le-73-2025.md | Hình sự | MỚI — "Cố tình thực hiện tội phạm đến cùng" |
| an-le-74-2025.md | Hình sự | MỚI — Trộm cắp tài sản của mình đang bị tạm giữ |
| an-le-79-2025.md | Dân sự | MỚI — HĐ đặt cọc khi đất đang thế chấp |
| an-le-82-2025.md | HN&GĐ | MỚI — Tài sản chung vợ chồng trước đăng ký kết hôn |

**Nguồn dữ liệu:**
- lienvietlaw.com (danh sách 72 án lệ có hiệu lực)
- luatsubaochua.vn (10 án lệ mới 2025 — đầy đủ tình huống + giải pháp pháp lý)
- anle.toaan.gov.vn (xác nhận nguồn chính thức)
- Lưu ý: thuvienphapluat.vn bị Cloudflare block, anle.toaan.gov.vn dùng Oracle WebCenter khó fetch trực tiếp

### ✅ Bước 3: 4 Bảng Tra Cứu Pháp Lý

Lưu tại `skills/your-next-lawyer/references/`:

| File | Nội dung | Kích thước |
|------|---------|-----------|
| **an-phi-le-phi.md** | Án phí sơ thẩm DS (có/không giá ngạch), KDTM, HS, HC, phúc thẩm, lệ phí, tạm ứng, miễn/giảm, hoàn trả | 5.9 KB |
| **thoi-hieu.md** | Thời hiệu TNHS (Đ27 BLHS), dân sự (Đ429 BLDS), thừa kế (Đ623 BLDS), lao động (Đ190 BLLĐ), XPHC (Đ6 XLVPHC), GD vô hiệu (Đ132), THA, khiếu nại | 8.0 KB |
| **tham-quyen-toa.md** | Hệ thống TAND 4 cấp, thẩm quyền sơ thẩm/phúc thẩm/GĐT/TT, theo lãnh thổ, VKS các cấp, quyền kháng nghị | 7.2 KB |
| **trinh-tu-to-tung.md** | Tố tụng DS (7 giai đoạn + thời hạn), HS (7 giai đoạn + thời hạn), HC (đặc thù), thời hạn kháng cáo | 8.8 KB |

### Điều luật được trích dẫn cụ thể

Tổng cộng **40+ điều luật** được trích dẫn trực tiếp từ:
- Bộ luật Hình sự 2015 (sửa đổi 2017): Điều 27, 28, 50, 52, 60, 123, 125, 134, 168, 173, 244, 353, 354...
- Bộ luật Dân sự 2015: Điều 129, 132, 133, 155, 156, 219, 220, 317, 318, 328, 429, 588, 611, 623...
- BLTTDS 2015: Điều 35, 37, 39, 40, 189-213, 222-315...
- BLTTHS 2015: Điều 145-183, 236-323, 330-362, 268-269...
- Luật TTHC 2015: Điều 31, 32...
- BLLĐ 2019: Điều 188, 190...
- Nghị quyết 326/2016/UBTVQH14: Điều 12-14, 24...
- Luật XLVPHC 2012 (sđ 2020): Điều 6, 74...

---

## Hạn Chế & Ghi Chú

1. **Án lệ chi tiết:** Chỉ soạn 13/82 file chi tiết do ưu tiên chất lượng > số lượng. Danh mục tổng hợp đủ 82 án lệ.
2. **Nguồn fetch bị hạn chế:** DuckDuckGo bị captcha sau vài query, thuvienphapluat.vn bị Cloudflare, anle.toaan.gov.vn dùng WebCenter khó fetch. Nội dung án lệ 2025 lấy đầy đủ từ luatsubaochua.vn.
3. **Án phí:** Mức theo NQ 326/2016. Cần kiểm tra nếu có văn bản sửa đổi mới.
4. **Thư mục nghi-dinh** đã tạo, chưa có nội dung (dành cho phase sau).

---

## Đề Xuất Phase 2

1. Bổ sung chi tiết 69 án lệ còn lại (ưu tiên: 02, 03, 06-16, 19-24, 30-35, 40-52)
2. Tải Nghị định quan trọng (NĐ 100/2019 xử phạt giao thông, NĐ 15/2020 xử phạt CNTT...)
3. Tạo bảng tra cứu hình phạt theo tội danh (BLHS 2015)
4. Tạo bảng tra cứu quyền của bị can/bị cáo trong tố tụng hình sự
