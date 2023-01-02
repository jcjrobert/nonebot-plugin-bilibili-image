from pydantic import BaseModel, Extra, validator
from typing import List

from nonebot import get_driver

class Config(BaseModel, extra=Extra.ignore):
    nickname: List[str] = ["Bot"]
    max_forward_msg_num: int = 99
    bilibili_image_save_local: bool = False

    @validator("nickname")
    @classmethod
    def check_nickname(cls, nickname):
        if not nickname:
            nickname = ["Bot"]
        return nickname

config = Config.parse_obj(get_driver().config.dict())