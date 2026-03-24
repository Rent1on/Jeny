import os
import json
from os import getenv
from aiogram import Router
from dotenv import load_dotenv
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

load_dotenv()
CHEF_ID = int(getenv("CHEF_ID"))
DEVELOPER_ID = int(getenv("DEVELOPER_ID"))

router = Router()

@router.message(Command('list'))
async def send_list(message: Message):
    if message.from_user.id != CHEF_ID and message.from_user.id != DEVELOPER_ID:
        await message.answer("❌<b>Отказанно в получении списка</b>\nПричина: Вы не являетесь членом руководства!", parse_mode='html')
        return
    
    json_path = 'data_base/doc_base.json'

    if not os.path.exists(json_path):
        await message.answer("📂 <b>База данных отчётов пуста.</b>", parse_mode='html')
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            await message.answer("❗️ Ошибка: отчёт поврежден")

    reports = data.get("Отчёт", [])

    if not reports:
        await message.answer("📂 <b>Список отчётов пока пуст.</b>", parse_mode='html')
        return
    
    text_list = "📝 <b>Список доступных отчётов:</b>\n\n"

    for item in reports:
        r_id = item.get("ID")
        r_name = item.get("Name")
        text_list += f"🆔 <code>{r_id}</code> - {r_name}\n"

    text_list += "\n<i>Чтобы получить файл, введите:</i>\n<code>/отчёт [ID]</code>"

    image = FSInputFile("pictures/list_document.jpg")
    await message.answer_photo(photo=image, caption=text_list, parse_mode='html')

    
