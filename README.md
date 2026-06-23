# vn-legal-db — Vietnamese law database, 5 codes, offline lookup

> Search and cite Vietnamese law articles offline — Criminal Code, IP Law, Civil Code, Labor Code, Criminal Procedure Code. 4.4MB, 72K+ lines from vi.wikisource.org.

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blueviolet)](https://github.com/NachaFromMars)

## Overview
vn-legal-db provides offline article lookup and keyword search across 5 major Vietnamese legal codes. Python CLI script — article lookup by number and keyword search across one or all codes.

## Features
| Code | Content | Size |
|---|---|---|
| BLHS 2015/2017 | Criminal Code — 26 chapters | 852KB |
| SHTT 2005/2022 | IP Law (2022 amendments) | 1.4MB |
| BLDS 2015 | Civil Code — 6 parts | 503KB |
| BLLĐ 2019 | Labor Code — 17 chapters | 259KB |
| BLTTHS 2015/2021 | Criminal Procedure Code | 1.4MB |

## Usage / Quick Start
```bash
python3 scripts/lookup.py article 226 BLHS
python3 scripts/lookup.py search "sở hữu công nghiệp"
python3 scripts/lookup.py search "lạm dụng tín nhiệm" BLHS
```

## Trigger Keywords (OpenClaw)
luật VN, điều luật, BLHS, BLDS, SHTT, lao động, tố tụng, pháp lý, legal Vietnam, Vietnamese law

## Related Skills
- [your-next-lawyer](https://github.com/NachaFromMars/your-next-lawyer) — AI legal advisor

---
Part of the [NachaFromMars](https://github.com/NachaFromMars) OpenClaw skill ecosystem.
