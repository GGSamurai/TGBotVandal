import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import keyboard

bot = Bot('6682215796:AAEall5HxrX3328CmjhcO0I7iRgNvWBs9nk')
dp = Dispatcher()


@dp.message(Command("start")) #Ответ на команду /start
async def start(message: Message):
    await message.answer('Добро пожаловать в VandalBot', reply_markup=keyboard.main_kb)



@dp.message(Command("area")) #Ответ на команду /area
async def area(message: Message):
    await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb)



@dp.message() #Принимаем сообщение от пользователя 
async def echo(message: Message):
    msg = message.text.lower() #Переводим весь текст сообщения в нижний регистр
    
    if msg == 'районы': #Если пользователь нажал на кнопку "Районы", то
        await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb) #Выводим новую клавиатуру с районами
    elif msg == 'показать адреса':#Если пользовател нажал на кнопку "Показать адреса, то"
        await message.answer(f'Выберите доступные адреса по району') #Показываем адреса по выбранному району (Стандартно стоит Ворошиловский)"



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())