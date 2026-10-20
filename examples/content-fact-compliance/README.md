# 样例 / Example：content-fact-compliance

> 改写自团队一次真实的脚本阶段核查（第 1 轮）。人名、账号名已去掉；论文、DOI 与原文数字均为核查时真实读到的内容，未改动。
> Adapted from a real script-stage review by our team. Names and accounts removed; papers, DOIs and quoted numbers are exactly as verified.

## 输入 / Input
对 agent 说：「帮我核一下这篇口播稿」，附上脚本（节选）：

> 有个实验专门测这个：让大学生去校园里找陌生人帮忙，比如填一份问卷、借一下手机……答应的人大约是他们预想的两倍。
> 还有更新的研究：被求助的人帮完之后的心情比求助者想象的好得多，也没觉得被打扰。
> 求人时把事情说具体，说清楚要多久。越具体，别人越好答应。

## 输出 / Output
**审核结论：FIX**（改完即可拍，无需复审全文）

一手来源 / Primary sources
- Flynn FJ, Lake VKB (2008) *JPSP* 95(1):128–143. DOI 10.1037/0022-3514.95.1.128
- Zhao X, Epley N (2022) *Psychological Science* 33(10):1708–1731. DOI 10.1177/09567976221097615

| # | 原句 | 结论 | 原文确切表述 | 建议改法 |
|---|---|---|---|---|
| 1 | 让大学生在校园里找陌生人帮忙（填问卷、借手机） | 通过 | 研究 1：请陌生人填问卷；研究 2：借手机打电话 | 保留 |
| 2 | 答应的人大约是预想的两倍 | **需改** | 研究 1：预测要问 20.5 人，实际 10.5 人；研究 2：预测 10.1 人，实际 6.2 人。摘要：“underestimated by as much as 50%” | 只在研究 1 成立；改成「要问的人数，大家猜的差不多是实际的 2 倍（填问卷实验）」 |
| 3 | 帮完心情比想象的好得多，也没觉得被打扰 | **需改** | “underestimated how positively helpers would feel, and overestimated how inconvenienced helpers would feel” | 改成「比你想的更好」「也没有你想的那么觉得被打扰」 |
| 4 | 说具体、说清要多久，别人更好答应 | **需改（标为建议）** | 两篇论文都没检验这一点 | 口播加「我的建议是」，不算作研究结论 |

```
审核结论: FIX
阻断项: 无
必改: #2 倍数只限研究1；#3 去掉绝对化；#4 标为个人建议
复审条件: 改完对照本表自查即可
```

**这个样例展示了什么 / What it shows**：不是只说「有出处」，而是逐句对到原文数字；论文没测过的东西，即使听起来合理也不能算研究结论。
