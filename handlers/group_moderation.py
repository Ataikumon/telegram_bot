from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command, F

from filters.chat_type import ChatTypeFilter

router = Router()

prohibited = [
    "",
    "",
    "",
]

@router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    F.text,
)
async def check_text(message: Message):
    message.text 
    
