import asyncio
import sys
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

api = '7736647536:AAFLHlsiHX7CmNJrBMnks83AplXK4ejoNfs'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
router = Router()
dp.include_router(router)


userdata = {
    'fullName': 'John Doe'
}

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Kompyuterlar')],
        [KeyboardButton(text='Komponentlar')],
        [KeyboardButton(text='Aksessuarlar')],

    ],
    resize_keyboard= True
)

keyboard1 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Gaming PC')],[KeyboardButton(text='Ofis PC')],
        [KeyboardButton(text='Custom PC')],
    ],
    resize_keyboard= True
)

keyboard2 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Videokartalar')],[KeyboardButton(text='Protsessorlar')],
        [KeyboardButton(text='Operativ xotira (RAM)')],[KeyboardButton(text='SSD/HDD ')],
        [KeyboardButton(text='Quvvat manbalari va sovutish tizimlari')],
    ],
    resize_keyboard= True
)

keyboard3 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Klaviaturalar')],[KeyboardButton(text='Sichqonchalar')],
        [KeyboardButton(text='Quloqchinlar')],[KeyboardButton(text='Monitorlar')],
        [KeyboardButton(text='Mikrofon va veb-kameralar')],
    ],
    resize_keyboard= True
)

keyboard4 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='NVIDIA RTX 4090')],[KeyboardButton(text='NVIDIA RTX 4070 Ti')],
        [KeyboardButton(text='AMD Radeon RX 7900 XTX')],[KeyboardButton(text='RTX 3060 / RX 6600 XT')],
    ],
    resize_keyboard= True
)

keyboard5 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Intel Core i9-13900K')],[KeyboardButton(text='AMD Ryzen 9 7950X')],
        [KeyboardButton(text='Intel Core i5-13600K')],[KeyboardButton(text='AMD Ryzen 5 7600X')],
    ],
    resize_keyboard= True
)

keyboard6 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Corsair Vengeance 32GB DDR5 6000MHz')],[KeyboardButton(text='Kingston Fury Beast 16GB DDR4 3600MHz')],
        [KeyboardButton(text='G.Skill Trident Z RGB 64GB DDR5')],[KeyboardButton(text='Crucial 8GB DDR4 3200MHz')],
    ],
    resize_keyboard= True
)

keyboard7 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Samsung 990 PRO 2TB NVMe SSD')],[KeyboardButton(text='WD Black SN850X 1TB NVMe SSD')],
        [KeyboardButton(text='Crucial MX500 1TB SATA SSD')],[KeyboardButton(text='Seagate Barracuda 4TB HDD')],
    ],
    resize_keyboard= True
)

keyboard8 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Corsair RM1000x 1000W 80+ Gold')],[KeyboardButton(text='MSI MPG A850G 850W 80+ Gold')],
        [KeyboardButton(text='Noctua NH-D15 havo sovutgichi')],[KeyboardButton(text='NZXT Kraken X73 360mm AIO')],
    ],
    resize_keyboard= True
)

keyboard9 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='SteelSeries Apex Pro')],[KeyboardButton(text='Logitech G Pro X')],
        [KeyboardButton(text='Razer Huntsman Mini')],[KeyboardButton(text='Redragon K552 Kumara')],
    ],
    resize_keyboard= True
)

keyboard10 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Logitech G Pro X Superlight')],[KeyboardButton(text='Razer DeathAdder V3 Pro')],
        [KeyboardButton(text='Glorious Model O Wireless')],[KeyboardButton(text='Logitech G305 Lightspeed')],
    ],
    resize_keyboard= True
)

keyboard11 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='LG UltraGear 27GP850-B 165Hz 1440p')],[KeyboardButton(text='Gigabyte M32U 32" 4K 144Hz')],
        [KeyboardButton(text='ASUS ROG Swift PG259QN 360Hz')],[KeyboardButton(text='Dell S2721DGF 165Hz 1440p')],
    ],
    resize_keyboard= True
)

keyboard12 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Shure SM7B')],[KeyboardButton(text='Elgato Wave 3')],
        [KeyboardButton(text='Logitech C920 HD Pro')],[KeyboardButton(text='Razer Kiyo Pro')],
    ],
    resize_keyboard= True
)

keyboard13 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='SteelSeries Arctis Pro Wireless')],[KeyboardButton(text='HyperX Cloud II')],
        [KeyboardButton(text='Razer BlackShark V2 Pro')],[KeyboardButton(text='Logitech G733 Lightspeed')],
    ],
    resize_keyboard= True
)


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('🔥 Xush kelibsiz, ByteBazaar!\nSizning eng zor kompyuter dokoningiz! 🛒💻\n⚡ Mahsulotlarni korib chiqing⚡ \nNarxlar va chegirmalarni tekshiring⚡\n Mutaxassislar yordamidan foydalaning\nBoshlash uchun /shop yozing yoki har qanday savolingizga javob oling! 🚀')

@router.message(Command(commands=['shop']))
async def start_shopping(message: Message):
    await message.answer(
        'Kerakli bolimni tanlang:\n 💻 Kompyuterlar – Tayyor tizimlar va gaming PClar\n🛠 Komponentlar – Videokartalar, protsessorlar, RAM va boshqalar\n🎧 Aksessuarlar – Klaviatura, sichqoncha, quloqchin va boshqa jihozlar', reply_markup=keyboard
    )


@router.message(F.text == "Kompyuterlar")
async def back_to_main(message: Message):
    await message.answer(
        "💻 Kompyuterlar bo‘limi!\n"
        "🖥 Gaming PC – O‘yin uchun kuchli kompyuterlar\n"
        "💼 Ofis PC – Ish va o‘qish uchun qulay variantlar\n"
        "🔧 Custom PC – O‘z konfiguratsiyangizni tanlang", reply_markup=keyboard1)



@router.message(F.text == 'Komponentlar')
async def shopping2(message: Message):
    await message.answer(
        '🛠 Komponentlar bo‘limi!\n🎮 Videokartalar – Eng so‘nggi va kuchli GPU’lar\n⚡ Protsessorlar – Intel va AMD chiplar\n🧠 Operativ xotira (RAM) – Tezkor ishlash uchun\n💾 SSD/HDD – Katta hajmli saqlash qurilmalari\n🔌 Quvvat manbalari va sovutish tizimlari', reply_markup=keyboard2
    )

@router.message(F.text == 'Aksessuarlar')
async def shopping3(message: Message):
    await message.answer(
        '🎧 Aksessuarlar bo‘limi!\n⌨ Klaviaturalar – Mexanik va membranali modellari\n🖱 Sichqonchalar – O‘yin va ofis uchun qulay variantlar\n🎧 Quloqchinlar – Gaming va musiqaga mos model tanlang\n🖥 Monitorlar – Yuqori sifatli ekranlar\n🎤 Mikrofon va veb-kameralar – Striming va ish uchun ideal', reply_markup=keyboard3
    )


@router.message(F.text == 'Videokartalar')
async def shopping4(message: Message):
    await message.answer('Videokartalardan birini tanlang: ', reply_markup=keyboard4 )

@router.message(F.text == 'Protsessorlar')
async def shopping5(message: Message):
    await message.answer('Protsessorlardan birini tanlang: ', reply_markup=keyboard5 )

@router.message(F.text == 'Operativ xotira')
async def shopping6(message: Message):
    await message.answer('Operativ xotiradan birini tanlang: ', reply_markup=keyboard6 )

@router.message(F.text == 'SSD va HDD')
async def shopping7(message: Message):
    await message.answer('SSD va HDD lardan birini tanlang: ', reply_markup=keyboard7 )

@router.message(F.text == 'Quvvat manbalari va sovutish tizimlari')
async def shopping8(message: Message):
    await message.answer('Quvvat manbalari va sovutish tizimlaridan birini tanlang: ', reply_markup=keyboard8 )

@router.message(F.text == 'Klaviaturalar')
async def shopping9(message: Message):
    await message.answer('Klaviaturalardan birini tanlang: ', reply_markup=keyboard9 )

@router.message(F.text == 'Sichqonchalar')
async def shopping10(message: Message):
    await message.answer('Sichqonchalardan birini tanlang: ', reply_markup=keyboard10 )

@router.message(F.text == 'Monitorlar ')
async def shopping11(message: Message):
    await message.answer('Monitorlardan birini tanlang: ', reply_markup=keyboard11 )

@router.message(F.text == 'Mikrofon va veb-kameralar')
async def shopping12(message: Message):
    await message.answer('Mikrofon va veb-kameralardan birini tanlang: ', reply_markup=keyboard12 )

@router.message(F.text == 'Quloqchinlar')
async def shopping4(message: Message):
    await message.answer('Quloqchinlardan birini tanlang: ', reply_markup=keyboard13 )


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    print('Bot is running....')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
