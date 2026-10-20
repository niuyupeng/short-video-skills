---
name: reference-first-script
description: Use when writing or reviewing a short-video voiceover script that should match a reference video's feel (钩子、笑点、节奏), when the user says "照着这个参考片写/没有参考片那种感觉", or when a knowledge-comedy script needs a line-by-line score against a reference.
license: MIT
---
# Reference-first script · 先拆参考，再写稿，再对标打分

> 中文在前，English summary at the end.
> 本技能迁移的是参考片的**节奏机制**，不复制台词、画面或人设。

## 0. 门禁
- 没有参考拆解（`REF_BREAKDOWN.md`）不准写稿。
- 用户没给参考片：先要一条；实在没有，就用同题材公开爆款做拆解，并写明“非用户指定参考”。
- 事实（年份、引文、出处）交给事实核查技能，本技能只管写得好不好看。

## 1. 拆参考片 → `REF_BREAKDOWN.md`
每个字段标【观察到的】或【推断的】。

| 项 | 记录什么 |
|---|---|
| 钩子 | 第 0–3 秒说了什么、画面是什么；为什么成立（荒诞前提 / 共同认知 / 直接提问） |
| 笑点密度 | 每个笑点的时间码、类型（反差、错位称呼、现代梗、角色反应）；平均几秒一个 |
| 节奏 | 每句字数、停顿、信息量；哪里快、哪里留白 |
| 反转位置 | 第几秒出现第一、第二个反转；谜底在哪 |
| 时长 | 总秒数、总字数、字/秒 |
| 结构表 | 按秒切段：段落功能 + 情绪 |

**降级路径**：参考片没有音轨或逐字稿时，在文件开头写明，节奏和笑点密度只能【推断】，后面的评分标注“非终审”，并向用户要带声音的原片。

## 2. 写稿（硬规则）
1. **第 0 秒直接说问题**。第一句就是那个问题，不铺垫、不自我介绍、不交代背景。
2. **谜底放最后，一句冷收**。能揭穿笑点的那句（例如“其实那个苹果可能根本没砸到他”）放到结尾，一句话收住；不解释笑话，不展开。
3. **不偷换概念，称呼前后一致**。同一个对象从头到尾一个身份：说了是“科学家”，后面就不能叫“果农”；把晚年聊天讲的轶事说成写进了论文，就是偷换概念。
4. **A/B 结尾不自相矛盾**。每个选项的字面意思要和它代表的立场一致（反例：用“躲开苹果”去代表“让它砸下来”）。选项里的对象也要和正文框架一致。
5. **每 5–6 秒至少一个实笑点**。嘴上说“这招我不敢学”不算；要有反差、错位、现代翻译或角色反应。给“我”配一个有反应的固定角色，接住包袱。
6. **删掉复述前文的部分**。观众刚看完的内容不再讲；非要总结，压成一句、3 秒以内。
7. **史料不把后来的事说成当场**。用“后来写下”“几年后”，不写“临走留下”，除非史料能证明是当场。学界有分歧的年份写“前后”。
8. 时长按账号规定；没有规定时以参考片时长为准，留 10% 余量。写“超了就删某段”等于承认那段可有可无，现在就删。

## 3. 逐句对标打分 → `SCORE.md`
五项各 10 分，满分 50，及格线 40 是默认值，可以按自己团队调整：

| 项 | 怎么判 |
|---|---|
| 钩子 | 第 0 秒是否直接是问题；前提是否和参考一样“人人能懂又够荒诞” |
| 笑点密度 | 实笑点个数 ÷ 时长，是否达到每 5–6 秒一个，且不低于参考 |
| 节奏 | 有没有解释笑话、复述、单句信息过载 |
| 反转位置 | 最响的反转是否放大；谜底是否在最后且一句收 |
| 时长 | 是否在规定内并有余量 |

输出格式：
```
总分 x/50  结论: 放行 | 小改 | 退回重写
逐句表: | 时间 | 原句 | 问题(对应规则#) | 改句 |
必须改: …   建议改: …
本次是否终审: 是/否（无音轨参考时为否）
```
低于及格线必须退回，列出具体改句，不写空泛意见。分数只来自实际对比，不编造。

## 4. 自检清单（交稿前）
- [ ] 有 REF_BREAKDOWN，且字段标了观察/推断
- [ ] 第一句是问题
- [ ] 谜底在最后、一句、没解释
- [ ] 全文同一对象称呼一致
- [ ] A/B 字面意思与立场一致
- [ ] 每 5–6 秒有实笑点
- [ ] 无复述段
- [ ] 史料时间不错位，已交事实核查
- [ ] 没有照抄参考片台词

---
## English summary
Gate: no reference breakdown, no script. Break the reference into hook, gag density, pacing, twist positions and length, marking each field observed vs. inferred (silent reference → degraded mode, non-final score). Write with hard rules: open at second 0 with the question; punchline/reveal last in one dry line, never explain the joke; keep one consistent label per entity (no concept swapping); A/B options must not contradict their own meaning; a real laugh every 5–6 s; cut recaps; never present later events as happening on the spot. Then score line by line on five 10-point axes (pass mark 40/50 is a default — adjust it for your team) with concrete rewrites. Transfer mechanics only — never copy the reference's lines.
