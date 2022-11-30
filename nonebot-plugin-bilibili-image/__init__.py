from . import matchers
from nonebot.plugin import PluginMetadata

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="b站图片下载",
    description="b站封面提取，专栏图片下载",
    usage="b站封面 + bvid/url\n专栏图片下载 + cvid/url",
    extra={
        "version": __version__,
        "license": "AGPL",
        "author": "jcjrobert <jcjrobbie@gmail.com>",
    },
)