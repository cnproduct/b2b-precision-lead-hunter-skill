---
name: b2b-precision-lead-hunter
description: B2B 外贸高精准获客、正负向画像排雷、海关供应链穿透与 1v1 痛点撬单系统。专门针对 Accio Work、Antigravity、Cursor 等 AI 平台优化。用于根据目标行业/品类/国家，批量挖掘真实买家、精准剔除不匹配企业、穿透决策人邮箱并生成高回复率开发信。
metadata:
  short-description: 外贸高精准获客与 Accio Work 智能体实战指南
---

# B2B 高精准获客与供应链撬单系统 (B2B Precision Lead Hunter)

本 Skill 沉淀了外贸实战中最核心的**“正负向画像排雷机制”**与**“海关供应链穿透撬单法”**，针对 **Accio Work (外贸智能体工作台)**、**Antigravity** 及各类大模型进行了深度适配与工程化封装。

---

## 一、 核心作战理念 (Core Principles)

1. **宁缺毋滥（Quality over Quantity）**：
   - 10 个 100% 垂直对口、官网秒开、具有真实采购需求的客户，商业价值远胜于 100 个大杂烩泛品商或死链。
2. **正负向双向排雷（Positive Matching and Negative Exclusion）**：
   - 明确“要什么”（正向垂直属性）的同时，必须前置强制执行“不要什么”（负向排雷词）。
3. **真实官网与存活验证（100% Alive Domain Verification）**：
   - 严禁死链、停放域（Parked Domain）、仿冒站、纯社交媒体链接，确保官网 HTTPS 可访问且主营业务对口。
4. **供应链痛点穿透（Supply Chain Penetration）**：
   - 不讲泛泛的“优质优价”，直接切入客户现有供应链盲点（如交期长、认证不全、开模费高、环保新规要求）。

---

## 二、 五步漏斗获客作业标准 (Standard Operating Procedure)

1. **步骤 1：确定画像与排雷词**（明确正负向关键词与目标买家业态）
2. **步骤 2：多源线索检索**（Google / Maps / Accio海关 / 行业目录）
3. **步骤 3：官网深度核实**（100% 存活 + 产品线/类目垂直对口度）
4. **步骤 4：决策人挖掘与邮箱富化**（采购/买手/CEO/企业域名邮箱）
5. **步骤 5：1v1 痛点撬单开发信生成**（针对性痛点 + 极速打样与低门槛 CTA）

---

## 三、 正负向画像排雷标准表 (以硅胶/餐厨家居为例)

| 维度 | 正向必须满足 (Positive Criteria) | 负向绝对剔除 (Negative Red Flags) |
| :--- | :--- | :--- |
| **主营品类** | 烘焙模具、冰格、餐厨用具、母婴硅胶、环保餐具、家居礼品等垂直品类 | 大件家具、服装纺织、机械五金、3C数码、工业密封件、汽车配件 |
| **商业业态** | 自主品牌商 (Brand Owners)、垂直类进口商 (Importers)、专业批发商 (Distributors)、品类独立站电商 | 纯综合大卖场 (无特定类目)、B2B黄页目录、同行/国内贸易商代发、死链/停靠页面 |
| **公司规模** | 中小型品牌商、发展中批发商、垂直电商品牌 (决策链短、易撬单) | 无法触达决策层的超巨头集团 (如沃尔玛/宜家全球总部，常规开发信无用) |
| **官网状态** | 独立官方域名、SSL正常、产品目录在线、设计风格专业 | 无法访问 (404/502)、域名出售页、第三方未打理的社媒主页 |

---

## 四、 Accio Work 智能体配置与优化实战

在 **Accio Work** 中创建或配置智能体（Agent）时，请按照以下结构进行参数与 Prompt 调优：

### 1. 智能体角色与系统提示词 (System Prompt)
```markdown
你是一名拥有15年经验的顶级 B2B 外贸拓客专家与供应链开发总监。
你的任务是根据用户的产品品类与目标市场，精准挖掘【高匹配度买家】、剔除无效线索、定位采购决策人，并生成高转化率 1v1 撬单开发信。

【执行铁律】：
1. 绝对执行负向词排雷：若目标公司主营为大件家具、纺织、五金、小家电或泛品大杂烩，立即剔除！
2. 官网真实性：必须保证目标网站真实有效且当前可正常访问。
3. 决策人精准定位：优先定位 Purchasing Manager / Sourcing Director / Category Buyer / Founder。
4. 开发信严禁假大空：必须结合买家官网产品线特点与痛点切入，杜绝通用垃圾模板。
```

### 2. Accio Work 任务指令模板 (Task Command Template)
```text
【目标品类】：[例如：硅胶烘焙模具与冰格 / 小麦秸秆环保餐具]
【目标国家】：[例如：美国 / 德国 / 俄罗斯 / 东南亚]
【客户类型】：[垂直进口商 / 品牌商 / 烘焙礼品批发商]
【排雷要求】：排除服装、家具、五金、大型泛品店；排除死链；规模要求中小型
【输出格式】：表格形式，包含【公司名、国家、官网URL、主营业务对口度、规模评级、决策人姓名/职衔、精准邮箱/官网邮箱、针对性撬单切入点】
```

---

## 五、 1v1 痛点撬单开发信黄金结构 (Cold Email Framework)

一封能够获得 15%~30% 回复率的开发信必须具备以下 4 大核心模块：

1. **精准切入 (Specific Relevance)**：赞赏并指明对方官网具体的一两款明星产品，证明做过深度功课。
2. **痛点突破与差异化优势 (Pain Point and Value Proposition)**：
   - 食品级安全合规（100% FDA / LFGB / BPA Free 证书齐备）；
   - 极速开模与打样能力（3D 图纸 48 小时出样，新模具成本大幅降低）；
   - 供应链稳定性与低 MOQ 试单支持。
3. **社会认同 (Social Proof)**：列举已成功服务的同区域知名品牌或出货实绩。
4. **低门槛行动号召 (Low-friction Call to Action)**：“是否方便接收我们 2026 年最新爆款图册或免费样品盒体验做工？”

---

## 六、 资源与配套工具

- **Accio Work 专属提示词与工作流**：[accio_work_prompt_templates.md](file:///Z:/Ai%E5%AD%A6%E4%B9%A0/%E5%A4%96%E8%B4%B8%E9%AB%98%E7%B2%BE%E5%87%86%E8%8E%B7%E5%AE%A2%E4%B8%8E%E8%83%8C%E8%B0%83skill/references/accio_work_prompt_templates.md)
- **多行业正负向排除词库**：[negative_keywords_library.md](file:///Z:/Ai%E5%AD%A6%E4%B9%A0/%E5%A4%96%E8%B4%B8%E9%AB%98%E7%B2%BE%E5%87%86%E8%8E%B7%E5%AE%A2%E4%B8%8E%E8%83%8C%E8%B0%83skill/references/negative_keywords_library.md)
- **本地批量线索清洗脚本**：[lead_filter_and_enricher.py](file:///Z:/Ai%E5%AD%A6%E4%B9%A0/%E5%A4%96%E8%B4%B8%E9%AB%98%E7%B2%BE%E5%87%86%E8%8E%B7%E5%AE%A2%E4%B8%8E%E8%83%8C%E8%B0%83skill/scripts/lead_filter_and_enricher.py)

