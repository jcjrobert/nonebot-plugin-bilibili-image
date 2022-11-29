import asyncio
import httpx
import imghdr
import traceback
from io import BytesIO
from typing import List
from zipfile import ZipFile, ZIP_BZIP2


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


def retry(func):
    async def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return await func(*args, **kwargs)
            except:
                traceback.print_exc()
                await asyncio.sleep(3)
                continue
        raise Exception('网络错误')

    return wrapper


@retry
async def get(client: httpx.AsyncClient, url: str, **kwargs):
    return await client.get(url, headers=headers, timeout=10, **kwargs)


"""
将图片打包成zip（图片类型自动判断）
"""
def zip_images(files: List[BytesIO]):
    output = BytesIO()
    with ZipFile(output, "w", ZIP_BZIP2) as zip_file:
        for i, file in enumerate(files):
            file_bytes = file.getvalue()
            ext = imghdr.what(None, h=file_bytes)
            zip_file.writestr(f"{i}.{ext}", file_bytes)
    return output