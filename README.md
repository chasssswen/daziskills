# 搭子图文场景工作室

百度搭子（DuMate）小红书文案与成图 Skill，包含双账号 **96 篇原文、451 张原图**、逐页 OCR、追加学习的 **16 篇审核稿 / 72 张配图及完整正文**、审核退回记录、官方品牌物料、**18 项真实界面/成果物料**和离线检索脚本。

## 安装与调用

将 `dazi-note-studio` 复制到 `~/.codex/skills/`，在 Codex 中使用 `$dazi-note-studio`。检索脚本只需 Python 3，无 API Key 或第三方依赖。

```sh
python3 dazi-note-studio/scripts/corpus.py search 简历 面试 PDF
python3 dazi-note-studio/scripts/corpus.py show A023
python3 dazi-note-studio/scripts/corpus.py verify
python3 dazi-note-studio/scripts/ui_materials.py search 简历 PDF
python3 dazi-note-studio/scripts/ui_materials.py verify
```

默认工作流：采集界面物料 → 检索96篇的场景与构图 → 用生图构建使用场景 → 等比嵌入真实界面、成果和精确文字 → 图文交付。预采集与内容生产分开；新场景优先用已有界面组件创作AI使用演示，不自动开启真实任务。每次创作看选中案例全部原图，结合具体功能设计画面；品牌、控件与功能逻辑保持准确，任务输入与成果可按场景共同创作；合成稿属于情景演示，不能伪称本次实测。

`assets/ui-library/manifest.json` 记录素材状态、可复用范围和校验值。2026-09-12批次覆盖首页、附件、技能/套件、自动化空白表单、虚构简历任务的输入/执行/交付和实际PDF；入口图不能冒充功能执行成功。

## 内容范围

2026-09-02 采集：A 账号 46 篇 / 223 图，B 账号 50 篇 / 228 图。manifest 保存原笔记 ID、链接、正文、OCR、尺寸与 SHA256；路径可随 Skill 迁移。

参考资料用于用户指定的学习与创作。原作者图文和官方品牌素材的版权仍属各自权利人，本仓库不授予第三方素材的再许可；新笔记应保留来源记录并避免整篇照搬。样本内容不自动证明当前产品能力，功能底稿版本为 2026-09-11。


## 2026-09-15 更新：真人网感与审核学习

优先呈现值得晒的成果、个人动机和取舍，再在动作中自然提到百度搭子。允许纯成果封面、短正文和后置教程；不要求每页都塞Logo、电脑与功能卡。整篇必须能看见品牌、准确界面、可读提示词和对应成果，同批构图须有区别；可保持相近视觉风格，用上下、斜向、上大下三等排法区分。

- [主技能](dazi-note-studio/SKILL.md)
- [真人口吻与画面](dazi-note-studio/references/copy-and-visual.md)
- [16篇逐图学习](dazi-note-studio/references/review-corpus-20260915.md)
- [审核退回原因与修法](dazi-note-studio/references/review-lessons.md)
- [16篇正文与原图索引](dazi-note-studio/assets/review-notes-20260915/manifest.json)
- [工作流方向](dazi-note-studio/references/workflow-directions.md)

追加资料按01—16序号保存在 `dazi-note-studio/assets/review-notes-20260915/`，各目录内有 `note.md` 与有序原图。索引记录页序依据、来源、SHA256和审核阶段，可直接离线读取；此前6篇网页下载稿的观察编号不强行视为原网页页序。

截至2026-09-15，审核表16篇最新状态均通过，其中7篇曾初审退回。保留10条审核反馈与3条修改回复；当前稿件并不等于完整保存了所有退回旧版本。此资料库独立于原96篇库，不把两者混为同一批采集。

安装只需复制整个 `dazi-note-studio` 目录；本地历史来源路径仅供追溯，实际调用使用技能内相对路径，不依赖原电脑目录。

## 2026-09-17 更新：烘焙上新写法与逐图提示词

新增用户原稿正文与4张原图，以及3篇烘焙笔记的9张最终图、3张AI产品原料、2张修正前画面。每张最终图都有对应的完整生图提示词、按顺序的参考路径；另保存发布文案、给搭子的指令和最终局部编辑记录。资源使用Skill内相对路径。

- [文案、逐图提示词与原始搭子UI编辑方法](dazi-note-studio/references/bakery-writing-and-image-prompts.md)
- [原稿学习与用户排版要求](dazi-note-studio/references/bakery-poster-learning-20260917.md)
- [3篇9图与实际提示词索引](dazi-note-studio/assets/examples/bakery-20260917/manifest.json)
- [用户原稿与4张原图索引](dazi-note-studio/assets/user-notes-20260917/manifest.json)

使用示例：调用 `$dazi-note-studio`，参考烘焙上新写法做3篇新商品笔记。先查看该索引中的成图与提示词，分别采用上下、斜向、上大下三排版；用已有搭子UI作参考，AI编辑本篇附件、派活指令和打开的成果。原生控件保持准确，输入与成品始终对应。

本批是基于既有UI参考制作的AI场景，不是本轮真实运行搭子的截图；原稿、AI商品原料、最终成图和修正前画面分开记录，不混入96篇原图库或真实UI库。
