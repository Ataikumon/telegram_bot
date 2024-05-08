import asyncio

from aiogram import Bot, Dispatcher

from handlers import group_games



async def main():
    bot = Bot(token=" 6938317584:AAEDuV_GArP4hd_hg0WINUofffeDHQLTuvY")
    dp = Dispatcher()
    dp.include_router(group_games.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

   

if __name__ == "__main__":
    asyncio.run(main())
