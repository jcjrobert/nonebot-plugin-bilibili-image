import re
import httpx
import json
import traceback

from .utils import *


async def get_did(args: str) -> str:
    """提取https网址"""
    url_pattern = re.compile(r"[a-zA-z]+://[^\s]*")
    url = url_pattern.search(args)
    if url:
        url = url.group(0)
    else:
        url = args
    did = re.sub(r"\?.*","",args) 
    if "b23.tv" in url:
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                url = str((await get(client, url)).url)
        except:
            traceback.print_exc()
    pattern = re.compile(r"[0-9]+")
    res = pattern.search(url)
    if res:
        did = res.group(0)
    return did


async def get_bilibili_get_dynamic_detail(did: str):
    url = f"https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id={did}"
    pics = []
    try:
        async with httpx.AsyncClient() as client:
            resp = (await get(client, url)).json()
            if resp.get("code") == 0:
                data = resp["data"]["card"]
                """
                图片动态就正常提取
                """
                if data["desc"]["type"] == 2:
                    pics = [p["img_src"] for p in json.loads(data["card"])["item"]["pictures"]]
                    pics = [BytesIO((await get(client, i)).content) for i in pics]
    except:
        traceback.print_exc()
    return pics