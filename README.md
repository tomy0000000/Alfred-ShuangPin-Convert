<div align="center">
    <img src="./src/icon.png" width="200" height="200">
</div>

# Alfred ShuangPin Convert

This is an alfred workflow build to help memorizing the mapping between pinyin typing sequence and shuangpin sequence.

![screenshot](assets/screenshot.png)

## Usage

Type the Input query `cv  [pinyin_sequence_space_seperated_ot_not]` in alfred to convert to shuangpin, conversion layout can be set by following the [config](#config) section

## Prerequisite

- Any macOS which has built-in Python 2.7
- Alfred 4+ with Powerpack (v3 should also works, but not tested)

## Installation

- Head over to [Releases](releases), download the latest version
- Double-click on `Shuangpin Convert.alfredworkflow` to install
- Auto-Update of workflow is enabled by default, but can be toggle by sending query
  - `cv workflow:autoupdate` for enabling Auto-Update
  - `cv workflow:noautoupdate` for disabling Auto-Update

## Config

* Config can be set in [workflow environment variables sheet](https://www.alfredapp.com/help/workflows/advanced/variables/#environment), by pressing `[x]` icon in Alfred Preferences

| Name               | Description                               | Default  |
| ------------------ | ----------------------------------------- | -------- |
| `MAIN_LAYOUT`      | Layout to convert shown in title          | `xiaohe` |
| `SECONDARY_LAYOUT` | Layout to convert shown in secondary text | `zhuyin` |

