# Azure Functions 活用事例集

> Microsoft の公式 Customer Success ページ（[www.microsoft.com/en/customers](https://www.microsoft.com/en/customers/)）から抽出した、Azure Functions が非常に効果的に活用されている事例をご紹介します。

---

## 事例 1: Coca-Cola — 60日間でグローバルAIキャンペーンを展開

**URL:** [https://www.microsoft.com/en/customers/story/22668-coca-cola-company-azure-ai-and-machine-learning](https://www.microsoft.com/en/customers/story/22668-coca-cola-company-azure-ai-and-machine-learning)

**業種:** 消費財・飲料  
**国/地域:** グローバル

### 概要

Coca-Cola は、AI を活用したホリデーキャンペーン「Create Real Magic」を世界43市場・26言語で展開しました。カスタム Santa モデルが 100 万人以上の消費者とリアルタイムで会話し、個別の「スノーグローブ」を共同作成するというものでした。この野心的なキャンペーンを、わずか 60 日間で立ち上げることに成功しました。

### Azure Functions の活用方法

Azure Functions は、AI・データ・イベントソース間のサーバーレスなワークフローオーケストレーションを簡素化するために活用されました。具体的には、Azure Functions のトリガーとバインディング機能を使用して、Azure Cosmos DB、Azure Service Bus、Azure Blob Storage 間でのイベントとデータ処理をシームレスに行いました。これにより、開発者はコード量を減らしつつ生産性を高め、インフラ管理ではなくイノベーションに集中できるようになりました。

> *"Azure gave us the tools to build, test, and deploy quickly. Everything was automated. That let us focus on solving real problems, not managing infrastructure."*

### 主な成果

- 26言語で対応（サブミリ秒のパフォーマンス）
- 100万人以上の消費者エンゲージメント
- 43市場・4リージョンで展開
- 15のサービスをわずか60日間で統合

---

## 事例 2: Art Basel — AI搭載のアートフェアコンパニオンアプリ

**URL:** [https://www.microsoft.com/en/customers/story/24324-art-basel-azure-ai-foundry](https://www.microsoft.com/en/customers/story/24324-art-basel-azure-ai-foundry)

**業種:** メディア・エンターテインメント  
**国/地域:** グローバル（スイス拠点）

### 概要

世界最高峰のアートフェアを主催する Art Basel は、訪問者がフェアをより楽しめるよう「Art Basel Companion」アプリを開発しました。このアプリには、会話型 AI コンパニオンと、スマートフォンカメラでアートを撮影するとアーティストやギャラリー情報を即座に返す「Art Basel Lens」機能が含まれています。

### Azure Functions の活用方法

Azure Container Apps と Azure Functions がサーバーレスバックエンドを担い、**Art Basel Lens** のリアルタイム画像認識ワークフローのオーケストレーションを Azure Functions が実行しています。ユーザーが写真を撮ると、画像のクロッピング、エンベディング生成、ベクターインデックスでの類似検索が約 2 秒以内に完了します。このサーバーレスアーキテクチャにより、年間を通じて変動するフェア来場者数に合わせて自動的にスケールが可能です。

> *"The scalability and flexibility of Azure provided exactly what we needed."*  
> — Sean Smith, Practice Lead, Data and AI, Valorem Reply

### 主な成果

- エンゲージメントの大幅な向上
- リピート訪問数の増加
- アプリ内滞在時間の延長
- GDPR など厳格なプライバシー規制への対応

---

## 事例 3: Chipotle — 統合された新しいカスタマーウェブサイトの構築

**URL:** [https://www.microsoft.com/en/customers/story/787157-chipotle-retailers-azure](https://www.microsoft.com/en/customers/story/787157-chipotle-retailers-azure)

**業種:** 小売・飲食  
**国/地域:** 米国

### 概要

Chipotle Mexican Grill は、既存の 3 つの異なるウェブサイト（メインサイト、オンライン注文サイト、ケータリングサイト）を統合した新しいカスタマー向けウェブプレゼンスを、小さなチームが 8 ヶ月以内に構築しました。新システムにより、メニューや価格の変更をコード変更なしに分単位で反映できるようになりました。

### Azure Functions の活用方法

Azure Functions は、フルホストのサービスが不要な場面でのイベント駆動型コード実行に活用されました。具体的には、**各店舗がメニューアイテムを在庫切れ時にリアルタイムで調整できる API**をサーバーレス関数として実装しました。これにより、小さなイベント処理に対して常時稼働のサーバーを維持するコストを削減しつつ、必要な機能を迅速に提供できるようになりました。

> *"In less than 20 minutes, I had a working prototype in .NET Core, deployed to Azure, with permissions properly set up…. Instead of spending a lot of time debating theories and approaches with no prior experience to rely on, we had a working demo ready to drive decision making in minutes."*  
> — Mike Smith, Lead Software Developer, Chipotle Mexican Grill

### 主な成果

- 8 ヶ月以内に新ウェブサイトをリリース
- メニュー変更を数分以内に反映可能（以前は開発・テスト・デプロイが必要）
- 2,500 以上の店舗に対応
- 内部 IT インフラの管理負荷を削減

---

## 事例 4: SPAR NL — 将来の小売業に向けたAzure Integration Servicesの活用

**URL:** [https://www.microsoft.com/en/customers/story/1607488243744944969-spar-nl-readies-future-retail-with-azure-integration-services](https://www.microsoft.com/en/customers/story/1607488243744944969-spar-nl-readies-future-retail-with-azure-integration-services)

**業種:** 小売  
**国/地域:** オランダ

### 概要

約 450 店舗を抱えるオランダの SPAR NL は、独立した各店舗オペレーターを連携する複雑なシステム統合の課題を抱えていました。レガシーな「ブラックボックス」システムを刷新し、クラウドファーストな統合プラットフォームを構築することで、注文・在庫・物流の透明性を確保しました。

### Azure Functions の活用方法

SPAR NL は、Microsoft および技術パートナーの HSO Global Services と協力し、**Azure Logic Apps と Azure Functions** を中核とした**イベント駆動型サーバーレス統合プラットフォーム**を構築しました。このプラットフォームにより、既存のオンプレミスサービスとスケーラブルなクラウドアプリを接続し、信頼性の高いセキュアなワークフローをオーケストレーションしています。以前は不透明だったデータの流れが可視化され、問題発生時に迅速に診断・対応できるようになりました。

> *"This Azure integration solution makes it possible to get an order right, get the scalability right, and get an order directly to the right systems."*  
> — Joran van den Brink, IT Integration Manager, SPAR NL

### 主な成果

- エンドツーエンドの監視が可能になり、問題の迅速な診断を実現
- 市場の変化への対応速度が大幅に向上
- 各店舗への注文・価格情報の配信が正確かつリアルタイムに
- レガシーの「ブラックボックス」システムを廃止し、透明性を確保

---

## 事例 5: SparePartsNow GmbH — 製造業向けB2Bスペアパーツマーケットプレイス

**URL:** [https://www.microsoft.com/en/customers/story/1620881869789987855-sparepartsnow-manufacturing-azure-services](https://www.microsoft.com/en/customers/story/1620881869789987855-sparepartsnow-manufacturing-azure-services)

**業種:** 製造業  
**国/地域:** ドイツ

### 概要

ドイツ・アーヘンのスタートアップ SparePartsNow GmbH は、製造業のスペアパーツ市場を変革しようとしています。工場の機械が故障した際に、複数の販売代理店を探し回ることなく、ワンクリックで必要なパーツを注文・配送できるプラットフォームを構築しました。わずか 3 名のエンジニアからスタートし、2022 年 10 月のローンチ以来、40 社以上のサプライヤーから約 20,000 種類のパーツを提供しています。

### Azure Functions の活用方法

少人数のエンジニアチームが、**イベント駆動型のサーバーレス Azure Functions コード**を活用してプラットフォームの中核を構築しました。注文処理ワークフローでは、Azure Functions がワークフローのオーケストレーション、請求処理、決済、配送物流を自動化しています。さらに、長時間実行される非同期プロセスには **Durable Functions**（Azure Functions の拡張機能）を採用し、ワークフローエンジンをゼロから構築する手間を省きつつ柔軟性を確保しました。

> *"The Durable Functions service was especially noteworthy, because it provided us with a lightweight and flexible way to orchestrate our long-running, asynchronous processes with as much code and skill reuse as possible."*  
> — Sebastian Kleinschmager, Co-Founder and CTO, SparePartsNow GmbH

### 主な成果

- 数週間以内に最初のプロトタイプを完成
- 同種の B2B プラットフォームとして市場で唯一の存在に
- 40 社以上のサプライヤー、約 20,000 種類のパーツを提供
- 小さなチームで大規模なオペレーションを実現

---

## まとめ

上記 5 件の事例はいずれも Microsoft の公式 Customer Success ページ（[https://www.microsoft.com/en/customers/](https://www.microsoft.com/en/customers/)）に掲載された実際の事例であり、Azure Functions が以下のシナリオで特に効果的に活用されていることがわかります：

| ユースケース | 事例 |
|:---|:---|
| サーバーレス ワークフロー オーケストレーション | Coca-Cola, SparePartsNow |
| イベント駆動型 API | Chipotle |
| リアルタイム画像処理パイプライン | Art Basel |
| エンタープライズ システム統合 | SPAR NL |
| 長時間実行プロセス （Durable Functions） | SparePartsNow |

Azure Functions のサーバーレスモデルにより、インフラ管理のオーバーヘッドなしに、スケーラブルで費用対効果の高いアプリケーションを迅速に構築・展開できることが、これらの事例から明確に示されています。
