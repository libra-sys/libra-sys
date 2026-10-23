# 个人主页视觉与维护

版本：1.0.0（2026-10-23）

## 目标

GitHub Profile README：黑紫液态玻璃横幅、已确认的白发 Q 版 GPT 龙娘，以及四个可点击公开项目入口。兼容 GitHub 原生页面，不依赖脚本、外部统计服务或自定义 CSS。

## 素材与实现

- `assets/gpt-dragon.png`：本次对话生成并由用户认可的透明底角色图，属个人使用的非官方 GPT 拟人形象。
- `assets/hero.png`：角色图与本地绘制玻璃背景合成；不是实时背景模糊。
- `assets/project-*.svg`：可编辑的静态项目卡片；文字来自公开仓库 README。未添加能力评级、虚构统计或私有项目信息。
- `tools/build_visuals.py`：使用 Pillow 重建横幅和卡片；首次素材来源路径可替换为 `assets/gpt-dragon.png`。Windows 微软雅黑字体用于中文绘制。
- `README.md`：原生 HTML 图片链接，无第三方依赖。

## 验证与限制

发布后检查 GitHub Profile 实际渲染、五张展示图加载、四个项目链接和窄屏显示。GitHub 外层主题由访问者选择，无法通过 README 更改。图片包含描述性替代文本。角色图保留原始分辨率，展示横幅为 1600×720。

## 更新

- 1.0.0：首次上线龙娘液态玻璃个人主页。
