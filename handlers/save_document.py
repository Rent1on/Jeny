import os
import json
from os import getenv
from aiogram import Bot
from aiogram import Router, F
from dotenv import load_dotenv
from aiogram.types import  Message, FSInputFile

load_dotenv()
ADMIN_ID = int(getenv("ADMIN_ID"))

router = Router()

@router.message(F.document)
async def proccess_document(message: Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌<b>Отказано в приятии файла!</b>\nПричина: вы не является сотрудником!", parse_mode='html')
        return

    document = message.document
    file_id = document.file_id
    file_name = document.file_name
    local_path = f'files/{document.file_name}'
    
    file = await bot.get_file(file_id)
    await bot.download_file(file.file_path, destination=local_path)

    json_file = 'data_base/doc_base.json'
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"Отчёт": []}

    else:
        data = {"Отчёт": []}

    new_id = str(len(data['Отчёт']) + 1)
    new_report = {
        "ID": new_id,
        "Name": file_name,
    }

    data["Отчёт"].append(new_report)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump (data, f, ensure_ascii=False, indent=4)

    user = message.from_user.full_name
    image = FSInputFile("pictures/save_document.jpg")
    text = (
        f'✅ Файл сохранен как <code>{local_path}</code>\n'
        f'📝 В базу добален отчёт с <b>ID: {new_id}</b>\n'
        f'👩🏻‍🔬 Спасибо за работу! {user}\n'
        f'🙋🏻‍♀️ Хорошего времяпровождения! {user}'
    )

    await message.answer_photo(photo=image, caption=text, parse_mode='html')