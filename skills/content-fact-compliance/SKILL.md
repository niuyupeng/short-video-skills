---
name: content-fact-compliance
description: >-
  Use before any script is filmed or any video/copy is published — verifies
  every factual claim against a primary source, checks platform 违规 rules and
  health-claim risk, and issues PASS / FIX / VETO.
---
# Fact-check & compliance review — has veto power

Run twice: on the script (before production) and on the final package (video + titles + covers + copy + first comment).

## 1. Claim extraction
| # | 原句 | 类型 | 一手来源(DOI/官方文件/原著卷页) | 来源原话 | 结论 OK/改/删 |
- Primary source required; news/百科/自媒体 only as leads.
- Preprints / opinion pieces / single small studies labeled on screen or cut.
- Quotes checked against the original; use 「前后」 when scholars disagree on dates.
- No source → remove or soften, never kept for flow.

## 2. Health & safety claims (strictest)
健康类最严：不诊断、不承诺疗效、写明不适合人群、效应量照原文、不从动物/细胞外推到人。
详见 [references/health-claims.md](references/health-claims.md)。

## 3. Platform 违规 check
文字、画面音频、AI 标识、标题与内容一致、首评不引流，逐项过。
详见 [references/platform-rules.md](references/platform-rules.md)。

## 4. Verdict
```
审核结论: PASS | FIX | VETO
阻断项: …   必改: …   建议: …
事实表: …
复审条件: …
```
- VETO blocks publishing until fixed and re-reviewed; other roles cannot override. Only the owner can, explicitly.
- Keep a dated review log per video.

## 常见错误
- 拿百科、新闻、自媒体当一手来源，它们只能当线索。
- 只看摘要就判 OK：要摘到来源原话。
- 「为了顺」保留没来源的句子。
- 把相对风险写成绝对风险，或把动物实验外推到人。
- 只审稿子不审成片：标题、封面、字卡、首评也要审。

## 输出模板
```
审核结论: PASS | FIX | VETO
| # | 原句 | 类型 | 一手来源 | 来源原话 | 结论 OK/改/删 |
阻断项: …
必改: 原句 → 改句
建议: …
复审条件: …
```

## 工具
`scripts/check_fact_ledger.py LEDGER.md`：结论只能是 OK/改/删；判 OK 的必须有一手来源和原话；疑似二手来源报错。
