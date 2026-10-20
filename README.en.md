<p align="center"><img src="./assets/banner.png" alt="short-video-skills" width="100%"></p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-black" alt="MIT"></a>
  <a href="https://github.com/niuyupeng/short-video-skills/releases"><img src="https://img.shields.io/github/v/release/niuyupeng/short-video-skills?include_prereleases&label=version&color=d4af37" alt="version"></a>
  <img src="https://img.shields.io/badge/skills-9-d4af37" alt="9 skills">
  <img src="https://img.shields.io/badge/format-SKILL.md-555" alt="SKILL.md">
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-444" alt="agents">
  <a href="https://github.com/niuyupeng/short-video-skills/stargazers"><img src="https://img.shields.io/github/stars/niuyupeng/short-video-skills?style=social" alt="stars"></a>
</p>

<p align="center"><a href="./README.md">中文</a> · <b>English</b></p>

# short-video-skills
**A skill library for knowledge-style short videos, used every day by an AI content team.** From topic picking, fact-checking and cover A/B tests to cross-platform repurposing, every rule here was forced out by a rejected draft.

- ✅ **Zero invented facts**: every claim needs a primary source (DOI / original text), with a PASS / FIX / VETO verdict
- 🎯 **Cover and hook A/B**: landscape 4:3 first, portrait 3:4 alongside, plus a win log
- 📊 **Data reviews that never make up numbers**: no data means writing "no data"
- 🔁 **One video, many platforms**: rewrite one finished video into Bilibili / Xiaohongshu / WeChat Channels titles, copy and tags
- 🧭 Native to Chinese platforms: Douyin, Bilibili and Xiaohongshu rules and health-claim risks

## Install in 30 seconds
```bash
npx skills add niuyupeng/short-video-skills
```
Or install manually:
```bash
git clone https://github.com/niuyupeng/short-video-skills.git
cp -R short-video-skills/skills/* ~/.claude/skills/      # Claude Code
# Codex: ~/.codex/skills/    project level: <project>/.agents/skills/
```
> Install only what you need. Minimal set: `content-fact-compliance` + `content-packaging-ab`.

## Skills
| Skill | In one line | Say to your agent |
|---|---|---|
| content-fact-compliance | Before filming / publishing, check every claim against a primary source and platform rules | "Fact-check this voiceover script" |
| content-data-review | Per-video and weekly performance reviews, no invented numbers | "Review this video's numbers" |
| content-packaging-ab | 2–3 versions each of title, cover and first-3-second hook, with a win log | "Give me three title/cover options for this video" |
| cover-top-tier | Hard standards for knowledge covers (landscape 4:3 + portrait 3:4) | "Make a cover to top-tier standard" |
| content-growth-ops | Repurpose a published video for other platforms, plus comment-reply drafts | "Turn this into Bilibili and Xiaohongshu versions" |
| life-tip-producer | A 35–55 s "try it tonight" life tip, from topic to delivery | "Make a life-tip video" |
| reference-first-script | Break down a reference video's hook, gags and pacing, then write the voiceover and score it line by line (the 40/50 pass mark is a default — adjust it for your team) | "Write one with the feel of this reference video" |
| landscape-first-reframe | Derive 4:3 / 3:4 / 9:16 / 1:1 from a 16:9 master; an FFmpeg script checks per ratio whether subtitles, title cards and corner tags survive the crop | "This landscape cut needs a vertical version — will the subtitles get cut off?" |
| rule-ledger | A dated rule ledger: newer rules supersede older ones, same-day contradictions go to a human, and stale values left in skill files are reported as a patch draft | "The rules changed — which skills need updating?" |

**Tests**: every skill has test cases under [evals/](./evals/) (including cases that should *not* trigger it). Measured with-skill vs. without-skill results for the 7 v0.2.0 skills: [evals/RESULTS.md](./evals/RESULTS.md) (the 2 skills added in v0.3.0 have test cases only, no results yet).

**How this differs from popular repos**: most replicate/storyboard skills assume 9:16 vertical; landscape-first-reframe treats 16:9 as the master and computes the common text-safe area for every derived ratio. skill-creator and superpowers' writing-skills teach you to write *one* good skill; rule-ledger manages how *a set* of skills drifts and contradicts itself over time.

## Results
All three images come from the team's real work records (anonymised, no performance data attached). Full input → output examples for each skill: [examples/](./examples/).

| Fact-check: line by line against the source | Packaging A/B: one lever per version | Data review: no data, no conclusion |
|---|---|---|
| <img src="./assets/demo_factcheck.png" alt="fact-check demo"> | <img src="./assets/demo_packaging_ab.png" alt="packaging A/B demo"> | <img src="./assets/demo_data_review.png" alt="data review demo"> |

## Design principles
1. The description only says when to trigger; the body stays under 500 lines
2. Study the reference before writing
3. Facts need primary sources; AI generation is disclosed honestly
4. When rules conflict, the newest wins, with its effective date written down

## Credits
Writing style learned from [anthropics/skills](https://github.com/anthropics/skills), [obra/superpowers](https://github.com/obra/superpowers) and [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) (ideas only, no content copied).
Sister project: 🧪 [CNS-Skills](https://github.com/niuyupeng/CNS-Skills), skills for writing top-journal papers.

---
⭐ **If it saved you a rewrite, a star helps other creators find it.** Issues and PRs welcome — tell us your pain points.
