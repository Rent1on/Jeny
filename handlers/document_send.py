import os
import json
import asyncio
from os import getenv
from aiogram import Router
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram.types import  Message, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

load_dotenv()
CHEF_ID = int(getenv("CHEF_ID"))
DEVELOPER_ID = int(getenv("DEVELOPER_ID"))

router = Router()

@router.message(Command("отчёт"))
async def send_document(message: Message):
    parts = message.text.strip().split()

    if message.from_user.id != CHEF_ID and message.from_user.id != DEVELOPER_ID:
        await message.answer("❌<b>Вам отказано в получении документа!</b>\n<i>Причина:</i><b>Вы не являетесь членом руководства!</b>", parse_mode='html')
        return

    if len(parts) != 2:
        await message.answer("❌Не коректный ввод команды!\nПример команды <code>/отчёт 1</code>", parse_mode="html")
        return
    
    report_id = parts[1]

    json_path = 'data_base/doc_base.json'
    if not os.path.exists(json_path):
        await message.answer("⚠️ В базе данных нет такого отчёта, проверьте позже")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            await message.answer("❗️ Ошибка чтения базы данных")
            return
        
    report_data = None
    for item in data.get("Отчёт", []):
        if str(item.get("ID")) == report_id:
            report_data = item
            break

    if not report_data:
        await message.answer(f"❌ <b>Отчёт с ID {report_id} ещё не готов, запросите позже</b>", parse_mode='html')
        return
    
    file_name = report_data.get("Name")
    file_path = f'files/{file_name}'

    if not os.path.exists(file_path):
        await message.answer(f"❌ Файл <code>{file_name}</code> отсутствует в камере хранения!", parse_mode='html')
        return      

    image_search = FSInputFile("pictures/search_document.jpg")
    text_search = (
        f"🔎Ищу отчёт с ID: {report_id}"
        )
    await message.answer_photo(photo=image_search, caption=text_search)
    await asyncio.sleep(1)

    user = message.from_user.full_name

    text = (
        f'👩🏻‍💼<b>Приветсвую {user}</b>\n\n'
        f'📑<b>Вот ваш отчёт:  {file_name}</b>\n'
        f'🙋🏻‍♀️Хорошего вам времяпровождения! {user}'
    )

    image = FSInputFile("pictures/send_document.jpg")
    await message.answer_photo(photo=image)

    doc_file = FSInputFile(file_path)
    await message.answer_document(document=doc_file, caption=text, parse_mode='html')

    
