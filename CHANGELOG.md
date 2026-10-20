# 更新日志 / Changelog

本项目所有值得注意的改动都记在这里。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。
All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-10-20

### 新增 / Added
- 新技能 `landscape-first-reframe` — 以 16:9 横版为母版派生 4:3 / 3:4 / 9:16 / 1:1，脚本逐比例检查文字安全区并给出 FFmpeg 命令 / new skill: derive other ratios from a 16:9 master and check text safe areas per ratio
- 新技能 `rule-ledger` — 带生效日期的规则账本，扫描技能文件中的旧值残留并输出补丁草稿 / new skill: dated rule ledger that finds stale values in skill files and drafts patches
- 每个技能新增 `references/`、`scripts/`（Python 标准库小工具）和 `tests/`（自编测试材料）/ every skill gains references/, stdlib scripts/ and synthetic tests/
- `evals/` 新增 2 个技能的测试用例（尚未跑结果）/ test cases for the 2 new skills (no results yet)
- `examples/` 新增 2 个样例；完整英文 README（README.en.md）/ 2 new examples; full English README

### 变更 / Changed
- 原有 6 个技能的 SKILL.md 重写：拆出参考资料，新增「常见错误」「输出模板」「工具」三节 / the 6 original SKILL.md files restructured with common mistakes, output templates and tools sections
- README：技能数 7 → 9，新增「和热门仓库有什么不一样」，English 链接指向 README.en.md / README: 9 skills, comparison section, English link to README.en.md
- `evals/RESULTS.md` 保持 v0.2.0 原样 / v0.2.0 results kept unchanged

## [0.2.0] - 2026-10-20

### 新增 / Added
- 新技能 `reference-first-script` — 先拆参考片（钩子、笑点密度、节奏、反转位置、时长），再写口播稿，再逐句五项对标打分；及格线 40/50 为默认值，可按团队调整 / new skill: break down a reference video first, then write the voiceover script, then score it line by line on five axes (40/50 pass mark is a default you can adjust)
- `evals/`：7 个技能共 29 条测试用例（含反例）与运行说明 / 29 test cases (incl. negative cases) for all 7 skills, with run instructions
- `evals/RESULTS.md`：装技能 vs 不装技能的实测结果（同一模型、每条 3 次）/ measured with-skill vs. baseline results (same model, 3 runs per case)
- `examples/reference-first-script/`：自编中性题目的示意样例 / illustrative example on a self-made neutral topic

### 变更 / Changed
- README：技能数 6 → 7，技能表加入 reference-first-script，补充 evals 说明 / README: 7 skills, new table row, evals section

## [0.1.0] - 2026-10-20

### 新增 / Added
- 6 个技能 / 6 skills:
  - `content-fact-compliance` — 逐条核一手来源与平台违规风险，给出 PASS / FIX / VETO / primary-source fact-check and platform compliance with a PASS / FIX / VETO verdict
  - `content-data-review` — 单条与周度数据复盘，不编数字 / per-post and weekly performance review, never invents numbers
  - `content-packaging-ab` — 标题、封面、前 3 秒钩子 A/B + 赢家日志 / title, cover and first-3s hook A/B with a win log
  - `cover-top-tier` — 知识类封面硬标准（横 4:3 为主 + 竖 3:4）/ hard rules for knowledge-video covers (4:3 primary + 3:4)
  - `content-growth-ops` — 一稿多投与评论运营草稿 / cross-platform repurposing and comment drafts
  - `life-tip-producer` — 35–55 秒生活小招全流程 / end-to-end 35–55s life-tip videos
- README（中英）、CONTRIBUTING、MIT LICENSE、横幅图 / README (zh/en), CONTRIBUTING, MIT LICENSE, banner
- 6 个脱敏样例（examples/）与 3 张效果图 / 6 sanitized examples and 3 demo images
- Issue 模板（问题反馈 / 新技能建议）、PR 模板、行为准则（Contributor Covenant 2.1）、本更新日志 / issue templates (bug / skill request), PR template, Code of Conduct (Contributor Covenant 2.1), this changelog

[0.2.0]: https://github.com/niuyupeng/short-video-skills/releases/tag/v0.2.0
[0.1.0]: https://github.com/niuyupeng/short-video-skills/releases/tag/v0.1.0
