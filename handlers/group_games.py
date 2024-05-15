from aiogram import Router, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods import delete_message
import logging

from filters.chat_type import ChatTypeFilter

router = Router()

prohibited = [
    "да",
    "пизда",
    "бля",
]



@router.message(
    ChatTypeFilter(["supergroup", "group"]),
    F.text,
)
async def check_text(message: Message):
    message.delete() 
    
    # t = message.text.lower()
    # for word in prohibited:
    #     res = t.find(word)
    #     print(res)
    #     if res >= 0:
    #         r = message.delete()
    #         print(r)
    #         print("deleting meesage")
        
    
