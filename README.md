<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-bilibili-image

_✨ 一键下载b站专栏全部图片 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/jcjrobert/nonebot-plugin-bilibili-image.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-bilibili-image">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-bilibili-image.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

一键下载b站专栏全部图片，后续会增加提取动态图片和封面图片的功能

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

    nonebot.load_plugin('nonebot_plugin_bilibili_image')

</details>

<details>
<summary>从 github 安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库

    git clone https://github.com/jcjrobert/nonebot-plugin-bilibili-image.git

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('src.plugins.nonebot_plugin_bilibili_image')

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| max_forward_msg_num | 否 | 99 | 合并转发消息条数上限 |

## 🎉 使用

### 指令表

| 指令 | 说明 |
|:-----:|:----:|
| 专栏下载/专栏图片下载 + cv号/url/短链接 | 可以直接附上cv号，也可以直接用分享链接，会先提取链接然后处理 |
