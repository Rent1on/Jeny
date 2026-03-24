from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import document_list, document_send, hello, save_document, info_send

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main():
    print("🚀Запуск")
    bot = Bot(token=TOKEN)
    
    dp.include_router(hello.router)
    dp.include_router(save_document.router)
    dp.include_router(document_send.router)
    dp.include_router(document_list.router)
    dp.include_router(info_send.router)
   

    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())

except KeyboardInterrupt:
        print("❌Бот выключен")