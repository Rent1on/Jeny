from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, ReplyKeyboardMarkup, KeyboardButton
    
router = Router()

@router.message(Command('start'))
async def send_first_message(message: Message):
    kb = [
        [KeyboardButton(text="/list")],
        [KeyboardButton(text="/info")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )

    user = message.from_user.first_name
    image = FSInputFile("pictures/hello_Jeny.png")
    text = (
        f"<b>👩🏻‍💼 Приветсвую {user}, я Jeny, ваш личный бот секретарь</b>\n\n"
        f"👩🏻‍💻 Если вы хотите получить отчёт введите команду: <code>/отчёт [номер]</code>\n"
        f"👩🏻‍💻 Советую для начала ознакомиться со списком\n"
        f"👩🏻‍💻 Если хотите ознакомиться со списком отчётов напишите <code>/list</code>"
    )

    await message.answer_photo(
        photo=image, 
        caption=text,
        reply_markup=keyboard, 
        parse_mode='html')