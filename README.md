<p align="center"><img src="./assets/banner.png" alt="short-video-skills" width="100%"></p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-black" alt="MIT"></a>
  <a href="https://github.com/niuyupeng/short-video-skills/releases"><img src="https://img.shields.io/github/v/release/niuyupeng/short-video-skills?include_prereleases&label=version&color=d4af37" alt="version"></a>
  <img src="https://img.shields.io/badge/skills-6-d4af37" alt="6 skills">
  <img src="https://img.shields.io/badge/format-SKILL.md-555" alt="SKILL.md">
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-444" alt="agents">
  <a href="https://github.com/niuyupeng/short-video-skills/stargazers"><img src="https://img.shields.io/github/stars/niuyupeng/short-video-skills?style=social" alt="stars"></a>
</p>

<p align="center"><b>中文</b> · <a href="#english">English</a></p>

# short-video-skills
**一支 AI 内容团队每天都在用的知识短视频技能库。** 从选题、事实核查、封面 A/B 到一稿多投，每一条规则都是被退稿逼出来的。

- ✅ **事实零编造**：每条事实都要附一手来源（DOI / 原文），给出 PASS / FIX / VETO 三档结论
- 🎯 **封面与钩子 A/B**：横版 4:3 为主、竖版 3:4 同时出，留一份赢家日志
- 📊 **数据复盘不编数字**：没有数据就写「无数据」
- 🔁 **一稿多投**：一条成片改写成 B 站 / 小红书 / 视频号各自的标题、文案和标签
- 🧭 中文平台原生：抖音、B 站、小红书的规则与健康类表述风险

## 30 秒安装
```bash
npx skills add niuyupeng/short-video-skills
```
或手动安装：
```bash
git clone https://github.com/niuyupeng/short-video-skills.git
cp -R short-video-skills/skills/* ~/.claude/skills/      # Claude Code
# Codex: ~/.codex/skills/    项目级: <project>/.agents/skills/
```
> 只装你需要的。最小组合：`content-fact-compliance` + `content-packaging-ab`。

## 技能列表
| 技能 | 一句话 | 对 agent 说 |
|---|---|---|
| content-fact-compliance | 拍摄前 / 发布前逐条核一手来源和平台违规风险 | 「帮我核一下这篇口播稿」 |
| content-data-review | 单条和周度数据复盘，不编数字 | 「复盘这条视频的数据」 |
| content-packaging-ab | 标题、封面、前 3 秒钩子各出 2–3 版，记录赢家 | 「给这条片子出三版标题封面」 |
| cover-top-tier | 知识类封面硬性标准（横 4:3 + 竖 3:4） | 「按顶级标准做封面」 |
| content-growth-ops | 已发视频改投其他平台，并出评论运营草稿 | 「把这条改成 B 站和小红书版」 |
| life-tip-producer | 35–55 秒「今晚就能试」的生活小招，从选题到交付 | 「做一条生活小招」 |

## 效果
以下三张图都来自团队真实工作记录（已脱敏，未附任何效果数据）。每个技能的完整「输入 → 输出」样例见 [examples/](./examples/)。

| 事实核查：逐句对原文 | 包装 A/B：一版一个杠杆 | 数据复盘：没有数据不下结论 |
|---|---|---|
| <img src="./assets/demo_factcheck.png" alt="fact-check demo"> | <img src="./assets/demo_packaging_ab.png" alt="packaging A/B demo"> | <img src="./assets/demo_data_review.png" alt="data review demo"> |

## 设计原则
1. description 只写触发条件，正文少于 500 行
2. 先学参考，再动笔
3. 事实要有一手来源，AI 生成如实标注
4. 规则冲突时以最新为准，并写明生效日期

## 致谢
写法参考了 [anthropics/skills](https://github.com/anthropics/skills)、[obra/superpowers](https://github.com/obra/superpowers)、[JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills)（只参考思路，未转载内容）。
姊妹项目：🧪 [CNS-Skills](https://github.com/niuyupeng/CNS-Skills)，顶刊论文写作技能。

---
<a id="english"></a>
## English
**Battle-tested Agent Skills for Chinese knowledge-style short videos** — fact-checking with primary sources, title/cover/hook A/B testing, honest data reviews and cross-platform repurposing (Douyin, Bilibili, Xiaohongshu). Built and used daily by an AI content team.

```bash
npx skills add niuyupeng/short-video-skills
```
Real input→output examples for every skill: [examples/](./examples/).
Works with any agent that reads `SKILL.md` (Claude Code, Codex, Cursor…). MIT licensed.

---
⭐ **If it saved you a rewrite, a star helps other creators find it.** Issues and PRs welcome — tell us your pain points.
