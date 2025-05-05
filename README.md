# CyberProbe AI

AI エージェントによる自動ペネトレーションテストシステム

## Overview

本システムは、[PTES](http://www.pentest-standard.org) に準拠し以下の機能を提供する。

- 自動脆弱性スキャンと分析
- インテリジェントな侵入テスト
- レポート生成

## Prerequisites

* [mise](https://github.com/jdx/mise)

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

### 3. アプリケーションを起動する

```shell
mise run-webui
```
