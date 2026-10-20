---
name: rule-ledger
description: Use when a team's rules or skill files change over time and may contradict each other — a new instruction overrides an old one, two skills give different values for the same setting, or before editing several skills after a policy change.
license: MIT
---
# Rule ledger · 带生效日期的规则账本 + 冲突扫描

> 管的不是「怎么写好一个技能」，而是**一组技能随时间演化时的冲突**：新规则推翻旧规则，旧值却还留在别的文件里。

## Overview
所有规则写进一张带生效日期的表。脚本按「同一个键，最新日期为准」自动判出已废止的规则，找出同一天互相矛盾的规则，再去技能目录里搜旧值残留，生成补丁草稿。脚本只读，不改任何技能文件。

## When to use
- 刚收到一条推翻旧做法的新规则（比如画幅从竖版改成横版）。
- 两个技能对同一个参数给了不同的数。
- 改一批技能之前，想先知道要改哪几行。
- 每周例行体检。

## 步骤
1. **记账**：每条规则一行，写进 `RULES.md`。列：`id | 生效日期 | 键 | 值 | 来源 | 旧值写法`。规则写法见 [references/ledger-format.md](references/ledger-format.md)。
   - 「键」是被约束的那件事（如「片尾时长上限」），同一件事必须用同一个键。
   - 「旧值写法」列出旧规则在文字里常见的说法，方便搜残留（如 `9:16,竖版视频`）。
2. **扫描**：
   ```bash
   python3 scripts/scan_conflicts.py RULES.md skills/ --patch PATCH_DRAFT.md
   ```
3. **读结果**：
   - `CONFLICT`：同一键同一天两个值，没有赢家，必须找定规则的人裁定。脚本不会替你选。
   - `SUPERSEDED`：旧规则被新规则取代。
   - `STALE`：技能文件里还写着旧值的行（已经用 `~~删除线~~` 标掉的不算）。
4. **出补丁草稿**：`PATCH_DRAFT.md` 列出每处残留和建议改法。按 [references/patch-policy.md](references/patch-policy.md) 改：先备份，旧写法用删除线保留，注明新规则 id 和日期。
5. **重扫**：改完再跑一次，直到 `CONFLICT 0` 且 `残留旧值 0`。

## 硬规则
- 新日期胜旧日期；同一天冲突不自动裁决。
- 不删旧规则，只标「已废止」，留痕可查。
- 脚本只出草稿，改技能文件是人的决定。
- 每条规则要有来源（谁、什么时候、在哪说的）。

## 常见错误
- 同一件事用了两个键（「片尾时长」「结尾卡时长」），扫描就发现不了冲突。
- 「旧值写法」只填一个数字，结果搜出一堆无关行；要写成带上下文的短语。
- 把补丁草稿当成已改完。
- 改了技能却没回账本补一条新规则，下次又被旧值覆盖。
- 规则没有生效日期，只能靠记忆判断谁新。

## 输出模板
```
规则 N 条，键 M 个
CONFLICT  键: 日期 同一天有 k 个值 [...] → 必须人工裁定
SUPERSEDED Rx 键=旧值（日期）→ 以 Ry 新值（日期）为准
STALE 文件:行 [键] 「原文」 应为 新值（Ry）
冲突 a，已废止 b，残留旧值 c
```

## 工具
- `scripts/scan_conflicts.py`：纯 Python 标准库，只读。
- `tests/demo_rules.md` + `tests/demo_skills/`：自编示例规则和两个演示技能文件，用来自测。
