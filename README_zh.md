<div align="center">
    <img src="./src/icon.png" width="200" height="200">
</div>

# Alfred ShuangPin Convert

![Test Status](https://github.com/tomy0000000/Alfred-ShuangPin-Convert/workflows/Test/badge.svg)
![GitHub All Releases](https://img.shields.io/github/downloads/tomy0000000/Alfred-ShuangPin-Convert/total?color=blue&label=Downloads&logo=Github)
![GitHub License](https://img.shields.io/github/license/tomy0000000/Alfred-ShuangPin-Convert?label=License)

這是一個設計用來幫助記憶雙拼鍵位的 Alfred workflow。

![screenshot](assets/screenshot.png)

## 使用方式

在 Alfred 的預設輸入框中直接輸入 `cv [漢語拼音鍵位 (可加空白或不加)]` ，鍵位佈局可透過 [Config](#config) 進行設定

## 系統環境

- 任何內建 Python 2.7 的 macOS
- Alfred 4+ 以及 Powerpack (v3應該也可以適用，但並未測試過)

## 安裝

- 前往 [Releases](https://github.com/tomy0000000/Alfred-ShuangPin-Convert/releases) ，下載最新版本
- 雙擊 `Shuangpin Convert.alfredworkflow` 安裝
- 自動更新預設為開啟，但可透過輸入下面的 Alfred 指令更改
  - `cv workflow:autoupdate` 開啟自動更新
  - `cv workflow:noautoupdate` 關閉自動更新

## Config

* Config 可以透過點擊 Alfred 設定中的 `[x]` 開啟 [workflow 環境變數設定頁](https://www.alfredapp.com/help/workflows/advanced/variables/#environment)設定

| 名字               | 用途                               | 預設值  |
| ------------------ | ----------------------------------------- | -------- |
| `MAIN_LAYOUT`      | 標題顯示的鍵位佈局          | `xiaohe` |
| `SECONDARY_LAYOUT` | 副標顯示的鍵位佈局 | `zhuyin` |

目前支援的鍵盤佈局有：

* 小鶴雙拼 (xiaohe)
* 微軟雙拼 (microsoft)
* 拼音加加 (plusplus)
* 搜狗雙拼 (sougou)
* 注音符號 (zhuyin)