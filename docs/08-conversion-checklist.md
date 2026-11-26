# 成約改善チェックリスト（2026-11-27 実施）

## 完了したこと

### 1. ブログデザイン／UX
- CTAボックスを強化（ティール枠線＋上部グラデーション＋大きな影）
- CTAボタンを大型化（font 1.05rem / padding 18px 40px）
- 本文内のアフィリエイトリンクに下線を追加して clicks を促す
- 各カードに実際のHPスクリーンショットを表示（「実際に使っている感」）
- 記事内に「実際の画面をのぞいてみる」セクション（5ツール）

### 2. 投稿クオリティ／記事数
日本語記事を 2 → 7 本に拡充：
1. AIツールの選び方（既存）
2. MiriCanvas（既存）
3. **Value AI Writerの料金と使い方**（新規・成約直結）
4. **ConoHa AI Canvasの料金と使い方**（新規）
5. **AIプレゼン比較 MiriCanvas vs Gamma vs ChatGPT**（新規）
6. **AIライティング比較 Value AI Writer vs Writesonic vs Surfer**（新規・成約直結）
7. **AI音声生成比較 ElevenLabs vs Murf**（新規）

各記事に確認日・公式出典・アフィリエイト開示・CTAを記載。
トップページの「新着記事」に6カード追加。ガイド記事から各比較記事へ内部リンク。

### 3. SEO（サブエージェントが実施・コミット 17c702c）
- canonical/hreflang（x-default含む）を全13ページで修正
- title 30-60字 / description 80-160字に統一
- OGP/Twitterカードを全ページ完成
- JSON-LD：WebSite+SearchAction、Article、BreadcrumbList（全11内部ページ）、FAQPageは該当2ページのみ
- 旧ドメイン（burattom.github.io）文字列ゼロ
- sitemap：JA 9URL / EN 4URL、全ページを収録
- robots.txt：両sitemapを参照

### 4. 被リンク獲得の仕組み
- `docs/07-backlink-plan.md`：アウトリーチ先と依頼文テンプレート
- `sns/note-article.md`：note投稿用原稿（サイトURL張り付け用）
- `sns/post-ideas-conversion.md`：成約記事への導線つきX/Instagram投稿案

## 未完了（ユーザー／人の作業が必要）

| 項目 | 詳細 |
|---|---|
| GSCサイトマップ再送信 | ブラウザのペアリングが切れたため未実施。https://search.google.com/search-console/sitemaps で `sitemap.xml` と `en/sitemap.xml` を再送信 |
| Bing Webmaster Tools | 新サイト追加が未完了。Site Explorer で URL 追加→メタタグ確認→sitemap送信 |
| note / はてな / X / Instagram 投稿 | 原稿は用意済み。実際に投稿して被リンクを獲得 |
| X の graduated access 解除 | 継続的な投稿・エンゲージメントが必要 |
| Instagram のサイトURL設定 | アプリからプロフィールリンクに設定 |
| PartnerStack ネットワーク申請 | 実情報（LinkedIn等）が必要 |

## 公開確認
- 全7記事＋トップ＋sitemap＋画像が HTTP 200 を確認済み（2026-11-27）
- sitemap.xml: 9 URL / en/sitemap.xml: 4 URL
