import re
import httpx
import traceback

from .utils import *


async def get_bvid(args: str) -> str:
    url_pattern = re.compile(r"[a-zA-z]+://[^\s]*")
    url = url_pattern.search(args)
    if url:
        url = url.group(0)
    else:
        url = args
    bvid = args
    if "b23.tv" in url:
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                url = str((await get(client, url)).url)
        except:
            traceback.print_exc()
    pattern = re.compile(r"(av|BV)[0-9a-zA-Z]+", re.I)
    res = pattern.search(url)
    if res:
        bvid = re.sub(r"av|BV","",res.group(0))
    return bvid


async def get_bilibili_video_viewinfo(bvid: str):
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    valid = False
    data = None
    try:
        async with httpx.AsyncClient() as client:
            resp = (await get(client, url)).json()
            if resp.get("code") == 0:
                valid = True
                data = resp.get("data")
    except:
        traceback.print_exc()
    return valid, data