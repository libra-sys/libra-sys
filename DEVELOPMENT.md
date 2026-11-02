# 研发与验证状态

更新：2026-11-02。以下按本轮代码和文档证据区分“明确待开发”和“需要验证”；没有运行证据不直接等于代码不可用。

## 明确需要完善

| 项目 | 当前证据 | 下一步 |
|---|---|---|
| [MetaFix-Orchestrator](https://github.com/libra-sys/MetaFix-Orchestrator) | README 标有文本模拟、前端待完善和测试缺口 | 验证真实 Issue → 修复 → 回归测试 → PR 闭环，补前端与部署 |
| [MedLoop](https://github.com/libra-sys/MedLoop) | 路线图仍列持久化、LLM、前端等；当前包含关键词匹配和模拟号源 | 统一功能状态，完善真实接入与持久化，不作为医院已部署产品宣传 |
| [smart-escort-dashboard](https://github.com/libra-sys/smart-escort-dashboard) | 前端关键词控制台尚未接后端 AI；有固定指标、演示轨迹与本地提醒 | 补真实接口联调、来源标记、鉴权与请求超时 |

## 需要运行验收或公开案例

| 项目 | 尚缺证据 |
|---|---|
| [InfiniShow](https://github.com/libra-sys/InfiniShow) | 线上登录、数据提交、真实分析到结果的完整验证，以及许可确认 |
| [ai-glasses-platform](https://github.com/libra-sys/ai-glasses-platform) | 当前部署与核心发布/使用流程的实际演示 |
| [smart-glasses-management](https://github.com/libra-sys/smart-glasses-management) | 支持设备与蓝牙、云开发的真实联调 |
| [docx-to-kaoshibao](https://github.com/libra-sys/docx-to-kaoshibao) | JSON 到 XLSX 已有小样例；Word/OCR 和考试宝实际导入需分别验证 |
| [contest-ppt-generator](https://github.com/libra-sys/contest-ppt-generator) | 需要可公开的完整材料、可编辑 PPT 与渲染检查案例 |
| [screenshot-reverse-engineer](https://github.com/libra-sys/screenshot-reverse-engineer) | 需要可公开截图、两份实际输出与实现对照案例 |
| [model-tier-advisor](https://github.com/libra-sys/model-tier-advisor) | 规则本身有文档，真实模型使用效果与节省比例尚无本轮对照验证 |

## 需要文档与评测整理

- `subagent-evaluator`：补根目录入口、样例和许可说明。
- `skillsbench-evaluator`：核实引用归因和评分依据，不能把启发式评分当权威基准。
- `ai-workflow-orchestrator`：补真实任务验收，并区分与 MetaFix 的定位。
- 行业 Skill 系列：先清楚标明依赖、脚本与提示词工作流的边界，再补可复现案例。

## 展示范围

- FridgeChef：按作者确认归入学校作业，仅保留学习记录。
- fjlzy-campus-baishitong：按作者要求归入校内展示，不列通用推广。
- 私有项目的名称与内部进展不在本页公开。

演示视频、脚本小样例、完整产品验收与用户认可分别记录，不能相互替代。
