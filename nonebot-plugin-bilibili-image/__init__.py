from . import matchers
from nonebot.plugin import PluginMetadata

__version__ = "0.0.2"
__plugin_meta__ = PluginMetadata(
    name="b站图片下载",
    description="b站封面提取，动态图片/专栏图片下载",
    usage="b站封面 + bvid/url\n动态图片/动态下载/动态获取 + 动态id/url\n专栏图片/专栏下载/专栏获取 + cvid/url",
    extra={
        "version": __version__,
        "license": "AGPL",
        "author": "jcjrobert <jcjrobbie@gmail.com>",
    },
)