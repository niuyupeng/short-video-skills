# 样例 / Example：rule-ledger

> 规则和技能文件都是自编的演示数据（`tests/demo_rules.md`、`tests/demo_skills/`）。输出是脚本原样输出。
> Rules and skill files are made-up demo data; output is verbatim.

## 输入 / Input
```
| id | 生效日期 | 键 | 值 | 来源 | 旧值写法 |
|---|---|---|---|---|---|
| R1 | 2026-01-05 | 视频画幅 | 9:16 | 示例：负责人口头 | 9:16,竖版视频 |
| R7 | 2026-03-02 | 视频画幅 | 16:9 | 示例：负责人书面 | |
| R2 | 2026-01-05 | 片尾时长上限 | 3s | 示例 | 片尾 3s,片尾不超过 3 |
| R9 | 2026-03-10 | 片尾时长上限 | 1.2s | 示例 | |
| R4 | 2026-02-01 | 人声高于配乐 | 6 LU | 示例 | |
| R5 | 2026-02-01 | 人声高于配乐 | 4 LU | 示例 | |
```
演示技能文件：`cover/rules.md` 写着「视频本体一律 9:16 竖版视频」；`edit/rules.md` 写着「片尾 3s 以内」，另有一行已用删除线标掉的旧写法。

```bash
python3 scripts/scan_conflicts.py tests/demo_rules.md tests/demo_skills --patch PATCH_DRAFT.md
```

## 输出 / Output
```
规则 6 条，键 3 个
CONFLICT 人声高于配乐: 2026-02-01 同一天有 2 个值 ['4 LU', '6 LU'] → 必须人工裁定
SUPERSEDED R1 视频画幅=9:16（2026-01-05）→ 以 R7 16:9（2026-03-02）为准
SUPERSEDED R2 片尾时长上限=3s（2026-01-05）→ 以 R9 1.2s（2026-03-10）为准
STALE cover/rules.md:2 [视频画幅] 「- 视频本体一律 9:16 竖版视频，HARD LOCK。」 应为 16:9（R7）
STALE edit/rules.md:2 [片尾时长上限] 「- 片尾 3s 以内。」 应为 1.2s（R9）
补丁草稿: patch.md
冲突 1，已废止 2，残留旧值 2
[exit 1]
```

生成的 `PATCH_DRAFT.md`：
```
# 规则补丁草稿（未修改任何文件，需人工确认）

- `cover/rules.md` 第 2 行 [视频画幅]
  - 现在: - 视频本体一律 9:16 竖版视频，HARD LOCK。
  - 建议: 改为 16:9，旧写法用删除线保留，注明 R7 2026-03-02
- `edit/rules.md` 第 2 行 [片尾时长上限]
  - 现在: - 片尾 3s 以内。
  - 建议: 改为 1.2s，旧写法用删除线保留，注明 R9 2026-03-10
```

**这个样例展示了什么**：同一天两个值的「人声高于配乐」不被自动裁决；已经用删除线标掉的旧写法不算残留；脚本只出草稿，不改文件。
