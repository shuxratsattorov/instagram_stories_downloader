import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand

from src.config import BOT_TOKEN
from src.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
from src.handlers.handlers import dp
from src.login_instagram import login_to_instagram
from src.scheduler import start_scheduler


bot = Bot(token=BOT_TOKEN)


async def main():
    logging.info("🚀  Bot ishga tushmoqda...")

    login_result = login_to_instagram(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    logging.info(login_result)

    # dp.startup.register(startup_answer)
    # dp.shutdown.register(shutdown_answer)

    start_scheduler(bot)

    await dp.start_polling(bot)

    await bot.set_my_commands([
        BotCommand(command="/start", description="Qayta ishga tushirish")
    ])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())