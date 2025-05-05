# CyberProbe AI

AI エージェントによる自動ペネトレーションテストシステム

## Overview

本システムは、[PTES](http://www.pentest-standard.org) に準拠し以下の機能を提供する。

- 自動脆弱性スキャンと分析
- インテリジェントな侵入テスト
- レポート生成

## Prerequisites

* [mise](https://github.com/jdx/mise)
* Docker

## Quick Start

### 1. Google AI Studio で API Key を発行する

1. [Google AI Studio](https://aistudio.google.com/app/apikey) を開く。
2. **Get API Key** をクリックし、画面の指示に従って API Key を作成する。
3. 作成された API Key をコピーする。

API Key を作成できたら `.env` ファイルに記載すること。

```
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

### 2. Install Dependencies

```shell
mise install
pdm install
npm install
```

### 3. Run Docker

```shell
docker compose up -d
```

### 4. WordPress をセットアップする

事前に、既知の脆弱性が存在するプラグインをダウンロードしておく。

```shell
wget -P ./tmp/wordpress https://downloads.wordpress.org/plugin/woocommerce.9.8.3.zip
wget -P ./tmp/wordpress https://downloads.wordpress.org/plugin/woocommerce-payments.5.6.0.zip
```

続いて [http://localhost](http://localhost) にアクセスし、WordPress をインストールする。

インストールが完了したら、ダウンロードした zip ファイルを [WordPress プラグイン管理画面](http://localhost/wp-admin/plugin-install.php) からアップロードする。

## 5. アプリケーションを起動する

```shell
mise run-webui
```
