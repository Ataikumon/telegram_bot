
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import URLInputFile
from aiogram.filters.command import Command


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота. Вставьте сюда свой токен
bot = Bot(token="7189654687:AAHMr7zxnY_hXVlHiIH6Ew3YT0gMNOdoIDU")

# Диспетчер
dp = Dispatcher()

next_id = 0

keyboard_next = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text="next")]
    ])


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    global next_id
    next_id = 0
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
    await message.reply("Тебе повезло ты выжил!", reply_markup=keyboard_next)

@dp.message(F.text.lower() == "второя дверь")
async def without_puree(message: types.Message):
    await message.reply("Ты сдох хахаххаахха", reply_markup=keyboard_next)
   
@dp.message(F.text.lower() == "next")
async def cmd_start(message: types.Message):
    global next_id
    if next_id == 0:
        kb = [
            [types.KeyboardButton(text="Да!")],
            [types.KeyboardButton(text="Нет!")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        image_from_url = URLInputFile("https://magiavody.ru/upload/shop_3/4/0/0/item_400/small_shop_property_file_400_254.jpg")
        result = await message.answer_photo(    image_from_url,
            caption="Искупался бы в этом бассейне?", reply_markup=keyboard
        )
        next_id = 1
    elif next_id == 1:
        kb = [
            [types.KeyboardButton(text="last")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Следующее задание", reply_markup=keyboard)


@dp.message(F.text.lower() == "да!")
async def reply_yes(message: types.Message):
    await message.reply("Ты сдох из за горячей воды хахахаахах", reply_markup=keyboard_next)

@dp.message(F.text.lower() == "нет!")
async def reply_no(message: types.Message):
    await message.reply("Тебе повезло ты выжил!", reply_markup=keyboard_next)


@dp.message(F.text.lower() == "last")
async def cmd_last(message: types.Message):
    kb = [
        [types.KeyboardButton(text="1")],
        [types.KeyboardButton(text="2")],
        [types.KeyboardButton(text="3")],
        [types.KeyboardButton(text="4")],
        [types.KeyboardButton(text="5")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выбери цифру от 1 до 5 ты проиграешь если выберешь неправильный номер", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "1")
async def reply_yes(message: types.Message):
    await message.reply("Ты проиграл", reply_markup=keyboard_next)

@dp.message(F.text.lower() == "2")
async def reply_yes(message: types.Message):
    await message.reply("Ты проиграл", reply_markup=keyboard_next)

@dp.message(F.text.lower() == "3")
async def reply_yes(message: types.Message):
    await message.reply("Ты проиграл", reply_markup=keyboard_next)


@dp.message(F.text.lower() == "4")
async def reply_yes(message: types.Message):
    await message.reply("Ты выиграл", reply_markup=keyboard_next)

@dp.message(F.text.lower() == "5")
async def reply_yes(message: types.Message):
    await message.reply("Ты проиграл", reply_markup=keyboard_next)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())