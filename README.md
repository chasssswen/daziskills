# 搭子图文场景工作室

百度搭子（DuMate）小红书文案与成图 Skill，包含双账号 **96 篇原文、451 张原图**、逐页 OCR、官方品牌物料和离线检索脚本。

## 安装与调用

将 `dazi-note-studio` 复制到 `~/.codex/skills/`，在 Codex 中使用 `$dazi-note-studio`。检索脚本只需 Python 3，无 API Key 或第三方依赖。

```sh
python3 dazi-note-studio/scripts/corpus.py search 简历 面试 PDF
python3 dazi-note-studio/scripts/corpus.py show A023
python3 dazi-note-studio/scripts/corpus.py verify
```

每次创作先检索、看选定案例全部原图，再结合具体功能设计文案与画面。真实产品界面不得重绘或改写成虚假实测；新任务示例与参考操作须区分。

## 内容范围

2026-09-02 采集：A 账号 46 篇 / 223 图，B 账号 50 篇 / 228 图。manifest 保存原笔记 ID、链接、正文、OCR、尺寸与 SHA256；路径可随 Skill 迁移。

参考资料用于用户指定的学习与创作。原作者图文和官方品牌素材的版权仍属各自权利人，本仓库不授予第三方素材的再许可；新笔记应保留来源记录并避免整篇照搬。样本内容不自动证明当前产品能力，功能底稿版本为 2026-09-11。
