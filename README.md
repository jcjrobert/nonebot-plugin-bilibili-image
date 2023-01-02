<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-bilibili-image

_✨ b站图片下载 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/jcjrobert/nonebot-plugin-bilibili-image.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-bilibili-image">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-bilibili-image.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

b站封面提取，动态图片/专栏图片下载

本插件使用了 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 `send_group_forward_msg` 和 `send_private_forward_msg` 接口 来发送合并转发消息，使用了 `upload_group_file` 和 `upload_private_file` 接口 来上传文件

发送私聊合并转发消息需要使用 `v1.0.0-rc2` 版本以上的 go-cqhttp

上传私聊文件需要使用 `v1.0.0-rc3` 版本以上的 go-cqhttp

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-bilibili-image

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-bilibili-image
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-bilibili-image
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-bilibili-image
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-bilibili-image
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot-plugin-bilibili-image')

</details>

<details>
<summary>从 github 安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库

    git clone https://github.com/jcjrobert/nonebot-plugin-bilibili-image.git

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('src.plugins.nonebot-plugin-bilibili-image')

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| max_forward_msg_num | 否 | 99 | 合并转发消息条数上限 |
| bilibili_image_save_local | 否 | false | 是否将下载的压缩包保存在本地 |

如果选择保存在本地，保存的压缩包将会在机器人运行目录下的 `data/download/`下

## 🎉 使用

### 指令表

| 指令 | 说明 |
|:-----:|:----:|
| b站封面/B站封面 + bv号/url/短链接 | 可以直接附上bv号，也可以直接用的分享链接，会先提取链接然后处理，不支持av号（因为基本用不到） |
| 动态图片/动态下载/动态获取 + 动态id/url/短链接 | 同上 |
| 专栏图片/专栏下载/专栏获取 + cv号/url/短链接 | 同上 |

除了b站封面获取，都会在获取后发送文件和转发信息，转发信息用于预览（图片画质会压缩），发送文件用于使用

## 📝 更新日志

<details>
<summary>展开/收起</summary>

### 0.0.2.1

- 依赖修正

### 0.0.2

- 支持将下载的压缩包保存在本地

### 0.0.1

- 插件初次发布

</details>

## 💡 特别感谢

- [noneplugin/nonebot-plugin-imagetools](https://github.com/noneplugin/nonebot-plugin-imagetools) Nonebot2 简单图片操作插件

## 📄 开源许可

本项目使用[AGPL-3.0](./LICENSE)许可证开源
