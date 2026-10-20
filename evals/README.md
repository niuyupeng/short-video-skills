# Evals · 技能测试

**中文** · [English](#english)

每个技能对应一个 `evals/<skill>.json`，格式兼容 [anthropics/skills](https://github.com/anthropics/skills) 中 skill-creator 的 `evals.json`，另加两个字段：

| 字段 | 含义 |
|---|---|
| `trigger_prompt` | 用户会怎么说（测触发） |
| `should_trigger` | 这句话是否应该触发本技能；`false` 为反例，用于测误触发 |
| `input` | 给 agent 的材料 |
| `expected_output` | 期望产出的一句话描述 |
| `expectations` | 逐条可判定的标准，评分时逐条判 通过 / 不通过 |

> 我们自己跑过一次的结果见 [RESULTS.md](./RESULTS.md)（单模型、样本小，只看方向）。欢迎你用自己的模型再跑，并附上模型名、日期和原始输出。

## 怎么跑

1. **装技能**：把 `skills/<skill>/` 复制到你的 agent 技能目录（如 `~/.claude/skills/`）。
2. **逐条运行**：每条用例开一个新会话，发送 `trigger_prompt`，并附上 `input`。需要文件的用例由评测者自备材料，合成材料要在结果里注明“合成”。
3. **记录**：本次是否触发了技能，以及完整输出。
4. **判分**：对 `expectations` 逐条判 通过/不通过，可以人工判，也可以让另一个模型当裁判（裁判只看输出和标准，不看是否装了技能）。
5. **汇总**：`通过条数 / 总条数`；反例（`should_trigger: false`）单独统计误触发率。

## 和不装技能对比（基线）

同一模型、同一 `trigger_prompt` 和 `input`，分两组跑：

| 组 | 设置 |
|---|---|
| with_skill | 安装该技能 |
| baseline | 不装任何本仓库技能 |

两组用同一份 `expectations` 盲评（打乱顺序，隐去组别）。建议每条至少跑 3 次，报告平均值与波动，不要只挑最好的一次。

结果建议存成 `evals/results/<skill>_<模型>_<日期>.json`，至少包含：`eval_id`、`group`、`triggered`、`passed_expectations`、`raw_output`。提交 PR 时请附原始输出，便于复核。

---

<a id="english"></a>
## English

Each skill has `evals/<skill>.json`, compatible with the skill-creator `evals.json` format from anthropics/skills, plus `trigger_prompt` and `should_trigger` (negative cases test false triggering).

Our own run (single model, small sample): [RESULTS.md](./RESULTS.md). Please re-run with your model and publish model, date and raw outputs.

**Run:** install the skill → new session per case → send `trigger_prompt` with `input` → record whether the skill triggered and the full output → grade each expectation pass/fail (human or blind LLM judge) → report pass rate; report false-trigger rate on negatives separately.

**Baseline:** same model and inputs, with vs. without the skill, graded blind against the same expectations, ≥3 runs each, report mean and spread. Save to `evals/results/<skill>_<model>_<date>.json`.
