from . import matchers
from nonebot.plugin import PluginMetadata

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="b站专栏图片下载",
    description="一键下载b站专栏全部图片",
    usage="专栏图片下载 + cvid/url",
    extra={
        "version": __version__,
        "license": "AGPL",
        "author": "jcjrobert <jcjrobbie@gmail.com>",
    },
)