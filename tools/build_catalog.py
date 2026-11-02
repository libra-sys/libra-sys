"""Rebuild editable project cards and README without changing approved identity art."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
projects=[
    ('asset-slicer','本地素材切图','透明裁边 · 网格与连通区域切图'),
    ('docx-to-kaoshibao','题库转换助手','题目整理工作流 · JSON 转 Excel'),
    ('model-tier-advisor','模型档位提示','轻量 Agent 规则 · 提醒后继续工作'),
    ('contest-ppt-generator','可编辑演示稿流程','材料核对 · 视觉确认 · 编辑与检查'),
]
for i,(slug,title,desc) in enumerate(projects,1):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="780" height="236" viewBox="0 0 780 236"><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#151722"/><stop offset="1" stop-color="#292339"/></linearGradient><radialGradient id="shine"><stop stop-color="#9784d4" stop-opacity=".22"/><stop offset="1" stop-color="#9784d4" stop-opacity="0"/></radialGradient></defs><rect x="1" y="1" width="778" height="234" rx="24" fill="url(#bg)" stroke="#514761"/><ellipse cx="690" cy="205" rx="220" ry="150" fill="url(#shine)"/><g font-family="Segoe UI,Microsoft YaHei,Arial,sans-serif"><text x="32" y="43" fill="#b8a7de" font-size="16">0{i} / PROJECT</text><text x="32" y="89" fill="#f2eefa" font-size="28" font-weight="600">{escape(title)}</text><text x="32" y="131" fill="#c1b8d4" font-size="19">{escape(desc)}</text><text x="32" y="194" fill="#b1a7c5" font-size="17">{slug}</text><text x="715" y="195" fill="#d0bfff" font-size="28">↗</text></g></svg>'''
    (ROOT/'assets'/f'project-{i}.svg').write_text(svg,encoding='utf-8')
text='''<p align="center">
  <img src="assets/hero.png" width="100%" alt="Hi, I’m why. 把想法，做成作品。黑紫液态玻璃背景与白发 Q 版龙娘。" />
</p>

我在整理能实际复用的小工具与 Agent 工作流：素材处理、题库转换、模型使用和演示稿制作。

## 精选工具与工作流

'''
for i,(slug,title,desc) in enumerate(projects,1):
    text+=f'<a href="https://github.com/libra-sys/{slug}"><img src="assets/project-{i}.svg" width="49%" alt="{title}：{desc}。打开 {slug}" /></a>\n'
text+='''
- [asset-slicer](https://github.com/libra-sys/asset-slicer)：本地素材处理。
- [docx-to-kaoshibao](https://github.com/libra-sys/docx-to-kaoshibao)：题目整理与 Excel 输出。
- [model-tier-advisor](https://github.com/libra-sys/model-tier-advisor)：模型档位提醒规则。
- [contest-ppt-generator](https://github.com/libra-sys/contest-ppt-generator)：可编辑演示稿制作流程。

> 切图工具按透明区域或已知网格处理素材，不做语义识别；题库脚本接收 JSON，Word/OCR 提取和校对属于前置流程。模型规则只作提醒，演示稿项目提供制作流程。具体依赖、限制与用法请看各仓库说明。

另外可以看看：[截图逆向工程](https://github.com/libra-sys/screenshot-reverse-engineer)。校园类作品放在下方校内栏目。

## 按方向浏览

| 方向 | 入口 |
|---|---|
| 实用工具与制作流程 | [切图、题库、PPT 与更多工具](PROJECTS.md#实用工具与制作流程) |
| 校园与参赛作品 | [校园百事通与创作系列](PROJECTS.md#校园与参赛系列) |
| 校内展示 | [福建林职校园百事通](PROJECTS.md#校内展示) |
| 行业 Skill | [客服、会议、内容与行业辅助流程](PROJECTS.md#行业-skill-系列) |
| 应用与系统探索 | [智能眼镜、经营分析与研发项目](PROJECTS.md#应用与系统研发) |
| 学习与数据探索 | [网络知识库与电影数据分析](PROJECTS.md#学习与数据探索) |
| 学校作业 | [课程作品与学习记录](PROJECTS.md#学校作业) |
| Agent 研发与评估 | [工作流编排与评估探索](PROJECTS.md#agent-研发与评估) |

[查看全部 42 个公开仓库分类 →](PROJECTS.md)

[查看真实图文演示 →](SHOWCASE.md) · [图文推广计划与调研 →](PROMOTION.md)

[查看待开发、待验证与案例补充清单 →](DEVELOPMENT.md)

这些项目处于不同阶段；目录与精选入口不代表全部功能均已完成或通过完整运行验收。

<p align="center"><sub>探索 · 构建 · 迭代</sub></p>

<!-- Visual source and maintenance notes: docs/DESIGN.md -->
'''
(ROOT/'README.md').write_text(text,encoding='utf-8')
print('Built four cards and public profile README; identity artwork unchanged.')
