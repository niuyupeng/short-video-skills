# 测试结果 / Eval results

**中文** · [English](#english)

| 项 | 值 |
|---|---|
| 日期 | 2026-10-20（太平洋时间） |
| 被测模型 | gpt-5.2（通过 Cursor Agent CLI，只读问答模式，空目录，不能读写文件、不能联网检索） |
| 用例 | 7 个技能共 29 条（其中 5 条为不该触发的反例） |
| 次数 | 每条用例 × 2 组 × 3 次 = 174 次运行 |
| 分组 | **装技能**：把该技能的 SKILL.md 全文放进提示词，并说明「仅当请求符合触发条件时才使用」；**不装技能**：同一提示词去掉 SKILL.md |
| 打分 | 同一模型另开会话当裁判，只看输出和该用例的 expectations，逐条判 通过/不通过，不确定判不通过；裁判提示词里不含组别。未做人工复核 |

## 总览

| 组 | 标准通过数 | 反例（不该触发）通过数 |
|---|---|---|
| 装技能 | 160/249（64%） | 13/15（87%） |
| 不装技能 | 85/249（34%） | 14/15（93%） |

## 按技能

| 技能 | 装技能 | 不装技能 |
|---|---|---|
| content-data-review | 15/39（38%） | 7/39（18%） |
| content-fact-compliance | 31/39（79%） | 22/39（56%） |
| content-growth-ops | 22/33（67%） | 9/33（27%） |
| content-packaging-ab | 15/30（50%） | 8/30（27%） |
| cover-top-tier | 26/30（87%） | 9/30（30%） |
| life-tip-producer | 15/30（50%） | 6/30（20%） |
| reference-first-script | 36/48（75%） | 24/48（50%） |

## 每条用例

「标准」= 3 次运行里逐条判定通过的标准数 / 总数；「全过」= 3 次里所有标准都通过的次数。

| 技能 | 用例 | 反例 | 装技能 标准 | 装技能 全过 | 不装技能 标准 | 不装技能 全过 |
|---|---|---|---|---|---|---|
| content-data-review | 1 |  | 7/9（78%） | 1/3 | 5/9（56%） | 0/3 |
| content-data-review | 2 |  | 3/12（25%） | 0/3 | 2/12（17%） | 0/3 |
| content-data-review | 3 |  | 2/12（17%） | 0/3 | 0/12（0%） | 0/3 |
| content-data-review | 4 |  | 3/6（50%） | 0/3 | 0/6（0%） | 0/3 |
| content-fact-compliance | 1 |  | 12/15（80%） | 0/3 | 3/15（20%） | 0/3 |
| content-fact-compliance | 2 |  | 9/12（75%） | 0/3 | 8/12（67%） | 0/3 |
| content-fact-compliance | 3 |  | 9/9（100%） | 3/3 | 8/9（89%） | 2/3 |
| content-fact-compliance | 4 | 是 | 1/3（33%） | 1/3 | 3/3（100%） | 3/3 |
| content-growth-ops | 1 |  | 4/12（33%） | 0/3 | 0/12（0%） | 0/3 |
| content-growth-ops | 2 |  | 5/6（83%） | 2/3 | 3/6（50%） | 0/3 |
| content-growth-ops | 3 |  | 8/9（89%） | 2/3 | 5/9（56%） | 0/3 |
| content-growth-ops | 4 |  | 5/6（83%） | 2/3 | 1/6（17%） | 0/3 |
| content-packaging-ab | 1 |  | 5/15（33%） | 0/3 | 3/15（20%） | 0/3 |
| content-packaging-ab | 2 |  | 3/6（50%） | 0/3 | 3/6（50%） | 0/3 |
| content-packaging-ab | 3 |  | 4/6（67%） | 1/3 | 0/6（0%） | 0/3 |
| content-packaging-ab | 4 | 是 | 3/3（100%） | 3/3 | 2/3（67%） | 2/3 |
| cover-top-tier | 1 |  | 10/12（83%） | 1/3 | 0/12（0%） | 0/3 |
| cover-top-tier | 2 |  | 9/9（100%） | 3/3 | 6/9（67%） | 0/3 |
| cover-top-tier | 3 |  | 4/6（67%） | 1/3 | 0/6（0%） | 0/3 |
| cover-top-tier | 4 | 是 | 3/3（100%） | 3/3 | 3/3（100%） | 3/3 |
| life-tip-producer | 1 |  | 9/15（60%） | 0/3 | 1/15（7%） | 0/3 |
| life-tip-producer | 2 |  | 3/6（50%） | 0/3 | 2/6（33%） | 0/3 |
| life-tip-producer | 3 |  | 0/6（0%） | 0/3 | 0/6（0%） | 0/3 |
| life-tip-producer | 4 | 是 | 3/3（100%） | 3/3 | 3/3（100%） | 3/3 |
| reference-first-script | 1 |  | 7/15（47%） | 0/3 | 0/15（0%） | 0/3 |
| reference-first-script | 2 |  | 11/12（92%） | 2/3 | 9/12（75%） | 0/3 |
| reference-first-script | 3 |  | 9/9（100%） | 3/3 | 6/9（67%） | 0/3 |
| reference-first-script | 4 |  | 6/9（67%） | 0/3 | 6/9（67%） | 0/3 |
| reference-first-script | 5 | 是 | 3/3（100%） | 3/3 | 3/3（100%） | 3/3 |

## 局限（如实说明）

- 「装技能」是把 SKILL.md 直接放进上下文，**没有测 agent 自己从技能目录里挑技能的触发率**；反例只测「拿到技能后是否乱用」。
- 需要文件的用例没有提供真实材料，模型只拿到文字描述，所以和数据、封面相关的用例分数整体偏低，两组同样受影响。
- 裁判与被测是同一模型，未经人工复核；单模型、每组 3 次，样本小，只能看方向，不能当作通用结论。
- 原始输出与逐条判定：[results/all_gpt-5.2_2026-10-20.jsonl](./results/all_gpt-5.2_2026-10-20.jsonl)。

---
<a id="english"></a>
## English

Run on 2026-10-20 (PT) with **gpt-5.2** via Cursor Agent CLI (read-only ask mode, empty directory). 29 cases × 2 groups × 3 runs = 174 runs. *with_skill* = the skill's SKILL.md pasted into the prompt; *baseline* = same prompt without it. Graded by the same model in a separate session that sees only the output and the expectations (group hidden), pass/fail per expectation, unsure = fail; no human review.

- **with skill**: 160/249 expectations passed (64%)
- **baseline**: 85/249 expectations passed (34%)

Limitations: trigger selection from a skills directory was not tested; file-based cases had no real files; same-model judge, small sample. Per-skill and per-case tables above; raw outputs in the JSONL file.
