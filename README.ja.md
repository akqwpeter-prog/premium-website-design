# Premium Website Design

[English](README.md) · [中文版](README.zh-CN.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md)

個人サイト、ポートフォリオ、ランディングページを、方向性・デザイントークン・タイポグラフィ・触覚的なインタラクション・生成アート・ライト/ダークテーマ・QA・デプロイまで一貫して設計する Codex スキルです。

**このスキルで作った実例:** https://mengjin-site.pages.dev

## できること

1. **デザインリード** - 対象と目的を読み取り、バリエーション / モーション / 密度のダイヤルを設定
2. **方向性** - 一つの明確な美学に絞り、テンプレ感を排除
3. **トークンと骨格** - OKLCH のダークファーストテーマ + ライトテーマ
4. **インタラクション** - キャラクター演出、スポットライト、3D チルト、マグネットボタン、スクロール連動、マーキー、テーマ切替
5. **アートワーク** - シード付き生成アート（API キー不要）、AI アバター（プライバシー対応）
6. **アイコン** - Iconify / Simple Icons / iconfont から自動検索・取得し、検証チェックリストで確認
7. **検証とデプロイ** - プリフライト、Playwright QA、Cloudflare Pages

## インストール

Codex 内でこのリポジトリからインストールを依頼するか、スキルディレクトリへコピーします。

```bash
cp -r premium-website-design ~/.codex/skills/
```

## 目次

```text
SKILL.md                      コアワークフロー
references/preflight.md       リリースチェックリスト
references/interactions.md    モーション実装
references/art-pipeline.md    生成アート + アバター + プライバシー
references/icons.md           アイコン取得 + 検証
assets/tokens.css             デザイントークン
scripts/qa_site.py            Playwright QA
```

## ライセンス

MIT
