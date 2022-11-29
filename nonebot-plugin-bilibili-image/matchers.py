import math
import tempfile
import traceback
from itertools import chain

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import (
    Message,
    MessageSegment,
    Bot,
    MessageEvent,
    GroupMessageEvent,
)
from nonebot.log import logger

from .config import config
from .article import *
from .utils import *

"""
专栏
"""
article = on_command("专栏图片下载", aliases={"专栏下载"}, block=True, priority=12)
@article.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    await bot.send(event=event,message="正在读取专栏图片中，请耐心等待",at_sender=True)
    url = args.extract_plain_text()
    cvid = await get_cvid(url)
    valid, banner_url, title = await get_bilibili_article_viewinfo(cvid)
    res = await get_bilibili_article_images(valid, banner_url, cvid)
    if res:
        """
        上传文件
        """
        zip_file = zip_images(res)
        filename = f"{title} - cv{cvid}.zip"
        try:
            await upload_file(bot, event, zip_file, filename)
        except:
            traceback.print_exc()
            logger.warning("上传文件失败")
        """
        发送转发信息
        """
        max_forward_msg_num = config.max_forward_msg_num
        msgs: List[Message] = [
            Message(MessageSegment.image(msg)) for msg in res
        ]
        if len(msgs) > max_forward_msg_num:
            step = math.ceil(len(msgs) / max_forward_msg_num)
            msgs = [
                Message(chain.from_iterable(msgs[i : i + step]))
                for i in range(0, len(msgs) - 1, step)
            ]
        await send_forward_msg(bot, event, config.nickname[0], bot.self_id, msgs)
    else:
        await bot.send(event=event,message="没有读取到该专栏的任何图片信息，请确认输入的网址/cvid是否正确",at_sender=True)


"""
发送接口
"""
async def send_forward_msg(
    bot: Bot,
    event: MessageEvent,
    name: str,
    uin: str,
    msgs: List[Message],
):
    def to_json(msg):
        return {"type": "node", "data": {"name": name, "uin": uin, "content": msg}}

    messages = [to_json(msg) for msg in msgs]
    if isinstance(event, GroupMessageEvent):
        await bot.call_api(
            "send_group_forward_msg", group_id=event.group_id, messages=messages
        )
    else:
        await bot.call_api(
            "send_private_forward_msg", user_id=event.user_id, messages=messages
        )


async def upload_file(
    bot: Bot,
    event: MessageEvent,
    file: BytesIO,
    filename: str,
):
    with tempfile.NamedTemporaryFile("wb+") as f:
        f.write(file.getbuffer())
        if isinstance(event, GroupMessageEvent):
            await bot.call_api(
                "upload_group_file", group_id=event.group_id, file=f.name, name=filename
            )
        else:
            await bot.call_api(
                "upload_private_file", user_id=event.user_id, file=f.name, name=filename
            )