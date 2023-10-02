import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import keyboard
import var

bot = Bot('6682215796:AAEall5HxrX3328CmjhcO0I7iRgNvWBs9nk')
dp = Dispatcher()


@dp.message(Command("start")) #Ответ на команду /start
async def start(message: Message):
    await message.answer('Добро пожаловать в VandalBot', reply_markup=keyboard.main_kb)



@dp.message(Command("area")) #Ответ на команду /area
async def area(message: Message):
    await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb)


@dp.message(Command("menu"))#Ответ на команду /menu
async def menu_func (message: Message):
    await message.answer('Выберите действие из меню', reply_markup=keyboard.menu_kb)


@dp.message()


@dp.message() #Принимаем сообщение от пользователя 
async def echo(message: Message):
    msg = message.text.lower() #Переводим весь текст сообщения в нижний регистр
    
    if msg == 'районы': #Если пользователь нажал на кнопку "Районы", то
        await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb) #Выводим новую клавиатуру с районами
    elif msg == 'показать адреса':#Если пользовател нажал на кнопку "Показать адреса, то"
        await message.answer(f'Выберите доступные адреса по району {var.start_area}') #Показываем адреса по выбранному району (Стандартно стоит Ворошиловский)"
    elif msg == 'удалить объект':
        await message.answer('Вы можете отправить фотоотчёт о том, что объект облагородили и мы удалим его из базы данных', reply_markup=keyboard.add_delete_kb)
    elif msg == 'добавить объект':
        await message.answer('Вы можете добавить новый объект, подвергшийся действиям вандализма через администратора бота', reply_markup=keyboard.add_delete_kb)


@dp.message()
async def area_and_street(message: Message):
    area = var.start_area
    msg = message.text.lower()

    if msg == 'ворошиловский':
        await message.answer(f'Вы видите все адреса объектов района {area}', reply_markup=keyboard.area_kb_vor())
    elif msg == 'центральный':
        area = 'Центральный'
        await message.answer(f'Вы видите все адреса объектов района {area}', reply_markup=keyboard.area_kb_centr())    
    elif msg == 'краснооктябрьский':
        area = 'Краснооктябрьский'
        await message.answer(f'Вы видите все адреса объектов района {area}', reply_markup=keyboard.area_kb_ko())
    elif msg == 'советсткий':
        area = 'Советский'
        await message.answer(f'Вы видите все адреса объектов района {area}', reply_markup=keyboard.area_kb_sov())
    elif msg == 'кировский':
        area = 'Кировский'
        await message.answer(f'Вы видите все адреса объектов района {area}', reply_markup=keyboard.area_kb_kir())


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())