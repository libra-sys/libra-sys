# 我的 GitHub 项目推广计划

调研日期：2026-11-02。形式以 README 和图文为主，不再制作宣传视频。本页是执行建议，不表示已经在外部平台发布或产生曝光。

## 当前先推什么

第一轮只推 **asset-slicer 的透明素材切图**：对象是需要整理图片素材的开发者和创作者，入口是项目 README，动作是下载脚本并成功运行一次。不要把整个账号的 42 个仓库放进同一篇宣传稿。

后续顺序：题目 JSON 转 Excel、图片转 Excel 像素画。截图分析和 PPT 制作先补完整案例；模型档位规则适合开发者经验分享，暂不投入大量推广。校园百事通用于校内，FridgeChef 留作业，未完成的系统项目不按完整产品宣传。

这是结合现有实现和受众的判断，不是流量或 Star 增长承诺。GitHub 的维护者建议也强调：先讲清解决的问题，再完善文档并回应用户。[GitHub 维护者推广建议](https://github.blog/open-source/maintainers/5-tips-for-promoting-your-open-source-project/)

## 第一步：让 README 能承接访问

访客打开后的顺序：

1. **一句话用途**：例如“把一张透明素材图按分离区域拆成切片，并保留位置”。
2. **真实结果图**：输入、输出和限制在同一个案例里。
3. **最短安装与命令**：给出环境要求与真实路径，不让人猜参数。
4. **可下载的自制样例**：方便没有现成素材的人复现。
5. **适用与不适用**：例如透明区域切图不能理解按钮与人物语义。
6. **求助入口**：描述问题时附输入、命令、期望和实际结果，敏感素材不要公开。

前三个重点仓库已补图文样例，统一入口见 [图文演示](SHOWCASE.md)。GitHub 官方说明 README 应交代项目用途和开始方式：[README 文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)。

## 第二步：先选两个渠道

| 渠道 | 本轮怎么发 | 希望得到什么 |
|---|---|---|
| 掘金或知乎，先选一个 | 一篇能复现的图文教程，写输入条件、命令、输出、失败边界 | 有相同问题的人尝试使用 |
| V2EX | 独立作品介绍与反馈征集，讲清作者身份、用途与当前限制 | 第一批技术用户的问题和建议 |
| 小红书，作为下一轮 | 输入/输出对比图与简短说明，先判断读者是否愿意安装 Python | 创作者关注和具体使用需求 |
| 相关 awesome 清单，后续 | 先阅读维护者的收录规则，确实相关且满足许可和质量条件才提 PR | 长期可发现性 |

V2EX 官方欢迎独立开发者在“分享创造”介绍新作；厂商营销内容应放“推广”，不能把商业营销伪装成技术求助。[节点说明](https://www.v2ex.com/help/node)

海外渠道先缓一缓。Show HN 官方要求别人能实际试用，单纯文章、列表或注册页不适用；简单快速生成的一次性作品也未必合适。先补英文快速开始与可复现样例，再判断具体项目是否符合。[Show HN 规则](https://news.ycombinator.com/showhn.html)

## 第一篇可以这样写

标题：**把透明 PNG 拆成独立素材：一个本地切图脚本和它的边界**

做界面和演示稿时，有时会拿到一张包含多个独立元素的透明 PNG。我把裁透明边、按网格切图和按透明连通区域拆图整理成了 asset-slicer。

这次用一张包含三个分离元素的自制测试图运行脚本，实际生成三张切片和坐标清单。README 放了输入与输出，基础切图在本机完成。

最短例子：

```bash
python -m pip install Pillow
python scripts/slice.py detect input.png --min-size 8 -o slices
```

运行前需下载仓库，并在仓库目录准备自己的 input.png。可选依赖和其他子命令见 README。

它依据透明区域分离素材，元素粘在一起时不能自动理解和拆开。希望找几位平时需要处理图片素材的人试试，反馈最卡的那一步。

项目：https://github.com/libra-sys/asset-slicer

配图用项目 README 中的真实样例，不增加未经测试的复杂素材效果，不写虚构节省时间。

## 一轮两周，按反馈推进

| 阶段 | 动作 | 完成标准 |
|---|---|---|
| 第 1–2 天 | README 与样例收尾，自己按公开命令复现 | 别人能找到输入、命令、输出和限制 |
| 第 3–4 天 | 找少量愿意试用的目标用户，或在允许的社区公开征集 | 收到明确的成功反馈或可复现问题；不把人数当保证 |
| 第 5–7 天 | 发一篇图文，集中回答问题 | 留下发布链接、问题与修正记录 |
| 第 8–10 天 | 根据反馈修最影响使用的问题，更新文档或真实版本 | 改动有记录，实际验收后再宣传 |
| 第 11–14 天 | 比较来源、克隆和使用反馈 | 决定继续同一项目，还是开始题库转换这一轮 |

日程是建议，不是必须卡某一天。没有证据证明某个固定星期或时刻一定适合你的账号；也不照搬通用 Skill 里的高频发帖次数。

## 怎么知道推广有用

去仓库 **Insights → Traffic** 看访问、独立访客、完整克隆和来源；GitHub 保留最近 14 天的访客与克隆数据，流量图采用 UTC 时间。建议每周留一份记录，不能只在一个月后回头看。[官方流量说明](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)

| 日期 | 项目 | 发布平台与链接 | 独立访客 | 完整克隆 | 成功使用反馈 | 主要问题 | Star/Fork 变化 |
|---|---|---|---|---|---|---|---|
| 待发布 | asset-slicer | 待填写 | 发布前记基线 | 发布前记基线 | 尚无外部记录 | 待收集 | 不承诺增长 |

访客、克隆、Star 都不等于成功使用。最先值得追的结果是：目标用户是否顺利跑通，哪里让他们放弃。优先回应这些反馈，再把解决过程写成下一篇图文。[为项目寻找合适的用户](https://opensource.guide/zh-hans/finding-users/)

## GitHub 内部还能做什么

- About 描述和 Topics 与实际用途一致；标签按用途、领域和语言选，不堆不相关热词。[Topics 官方文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- 准备分享卡片图。它与 README 插图是两项设置；GitHub 推荐 1280×640，图片小于 1 MB。没有把 README 图片当作已设置 Social preview。[社交预览文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- 只有确实可复现的版本才做 Release，不把文档更新包装成新功能。
- 补适用的许可证和贡献说明；源码与素材来源需核对，不能为追热度随意添加授权。
- 从真实 Issue 中挑适合新人的任务并写清验收方法，再加 good first issue；不制造空任务。

## 已筛选的运营 Skill 与资料

以下元信息于 2026-11-02 实时核对，推送日期是仓库层面，不能代表每个 Skill 都在当天改过。未安装、未运行第三方脚本。

| 候选 | 许可与最近仓库推送 | 适配判断 |
|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT；2026-10-31；未归档 | 优先参考 launch 和 social 的分阶段发布、内容改写与复盘方法；不照搬 SaaS 收款、候补名单和高频发帖 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | MIT；2026-11-02；未归档 | 有 launch-strategy、social-content 等；范围很大，当前不整包装载，也不执行其多 Agent 流程 |
| [T-shirt0523/promo-kit](https://github.com/T-shirt0523/promo-kit) | MIT；2026-09-24；未归档 | 中文素材包流程可参考，但定价、海报、视频范围超出本次图文开源推广；脚本未审计运行，暂不采用 |
| [Zenika 推广备忘单](https://github.com/zenika-open-source/promote-open-source-project/blob/main/README-zh-cn.md) | MIT；2026-09-07；未归档 | 是清单而非 Agent Skill。采用 README、示例、低门槛使用、反馈等检查项；不把其固定发帖时间和 Star 建议当普适规则 |

本次实际参考的 Skill 原文：[launch](https://github.com/coreyhaines31/marketingskills/blob/main/skills/launch/SKILL.md)、[social](https://github.com/coreyhaines31/marketingskills/blob/main/skills/social/SKILL.md)。Skill 帮助组织工作，不等于自动获得曝光，也不是刷 Star 工具。
