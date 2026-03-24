from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile


router = Router()

@router.message(Command("info"))
async def send_info(message: Message):

    user = message.from_user.full_name
    developer = "https://t.me/Ent1onOfficial"
    text = (
        f"🙋🏻‍♀️ Приветсвую {user} как ты мог видить я бот секретарь.\n"
        f"👩🏻‍💻 Мой функционал на данный момент это получения и отправка документов.\n"
        f"🤷🏻‍♀️ На данный момент я поддерживаю только .pdf файлы.\n"
        f"👩🏻‍🔬 В будущем добавятся новые базы по хранению файлов.\n"
        f"🤵🏻‍♀️На данный момент бот ограничен для определенного круга лиц.\n"
        f"💁🏻‍♀️ Заинтересовал моий функционал вот тебе ссылка на разработчика {developer}\n"
        f"👩🏻‍🔧 Он может сделать мой функционал под тебя и под твои нужды, на этом всё.\n"
        f"🙋🏻‍♀️ Хорошего времяпровождения {user} и до скорого!"
    )

    image = FSInputFile("pictures/info_Jeny.jpg")

    await message.answer_photo(photo=image, caption=text, parse_mode='html')

    