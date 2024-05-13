import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import group_games

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token="7115299867:AAEFCkPZRfrLNtc7Amaxz-n_97tlMnIDKy4")
    dp = Dispatcher()
    dp.include_router(group_games.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
