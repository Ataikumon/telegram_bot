
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота. Вставьте сюда свой токен
bot = Bot(token="7189654687:AAHMr7zxnY_hXVlHiIH6Ew3YT0gMNOdoIDU")

# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Проверь интуицию")


@dp.message(Command("check"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Первая дверь")],
        [types.KeyboardButton(text="Второя дверь")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выбери дверь что бы выжить", reply_markup=keyboard)
    



@dp.message(F.text.lower() == "первая дверь")
async def with_puree(message: types.Message):
    await message.reply("Тебе повезло ты выжил!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text.lower() == "второя дверь")
async def without_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="next")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Ты сдох хахаххаахха", reply_markup=keyboard)
   
@dp.message(F.text.lower() == "next")
async def cmd_start(message: types.Message):
    await message.answer("Следующее задание", reply_markup=types.ReplyKeyboardRemove())











# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())