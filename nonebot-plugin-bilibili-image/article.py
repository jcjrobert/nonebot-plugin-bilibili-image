from bs4 import BeautifulSoup
import httpx
import re
import traceback
from typing import List

from .utils import *

"""
提取cv号

支持：
①直接的cv号
②带有cv号专栏网址
③短链接跳转
"""
async def get_cvid(args: str) -> str:
    """提取https网址"""
    url_pattern = re.compile(r"[a-zA-z]+://[^\s]*")
    url = url_pattern.search(args)
    if url:
        url = url.group(0)
    else:
        url = ""
    cvid = args
    if "b23.tv" in url:
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                url = str((await get(client, url)).url)
        except:
            traceback.print_exc()
    pattern = re.compile(r"(cv|id=)[0-9]+", re.I)
    res = pattern.search(url)
    if res:
        cvid = re.sub(r"cv|id=","",res.group(0))
    return cvid


"""
验证专栏号是否有效
并且获取专栏头图（如果有）
"""
async def get_bilibili_article_viewinfo(cvid: str):
    url = f"https://api.bilibili.com/x/article/viewinfo?id={cvid}"
    valid = False
    banner_url = ""
    title = ""
    try:
        async with httpx.AsyncClient() as client:
            resp = (await get(client, url)).json()
            if resp.get("code") == 0:
                valid = True
                banner_url = resp.get("data").get("banner_url")
                title = resp.get("data").get("title")
    except:
        traceback.print_exc()
    return valid, banner_url, title


"""
直接读取专栏获取图片
"""
async def get_bilibili_article_images(valid: bool, banner_url: str, cvid: str):
    img_urls: List[str] = []
    images = []
    if banner_url:
        img_urls.append(banner_url)
    if valid:
        url = f'https://www.bilibili.com/read/cv{cvid}'
        try:
            async with httpx.AsyncClient() as client:
                resp = await get(client, url)
                dom = BeautifulSoup(resp.text, 'lxml')
                content = dom.find(id="article-content")
                imgs = content.find_all("img")
                img_urls += [f"https:{i['data-src']}" for i in imgs]
                images = [BytesIO((await get(client, i)).content) for i in img_urls]
        except:
            traceback.print_exc()
    return images