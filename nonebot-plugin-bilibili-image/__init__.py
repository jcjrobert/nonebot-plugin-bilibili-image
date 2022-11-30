from . import matchers
from nonebot.plugin import PluginMetadata

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="b站图片下载",
    description="b站专栏图片下载，封面提取",
    usage="专栏图片下载 + cvid/url",
    extra={
        "version": __version__,
        "license": "AGPL",
        "author": "jcjrobert <jcjrobbie@gmail.com>",
    },
)