import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import keyboard
import var

bot = Bot('6682215796:AAEall5HxrX3328CmjhcO0I7iRgNvWBs9nk', parse_mode="HTML")
dp = Dispatcher()
area = var.start_area
mass = ['Ворошиловский']


@dp.message(Command("start")) #Ответ на команду /start
async def start(message: Message):
    await message.answer('Добро пожаловать в VandalBot', reply_markup=keyboard.main_kb)
    await message.delete()



@dp.message(Command("area")) #Ответ на команду /area
async def area(message: Message):
    await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb)
    await message.delete()

@dp.message(Command("menu"))#Ответ на команду /menu
async def menu_func (message: Message):
    await message.answer('Выберите действие из меню', reply_markup=keyboard.menu_kb)
    await message.delete()

@dp.message(Command("info")) #Информация о боте 
async def information(message: Message):
    await message.answer('<b>Добро пожаловать в VandalVlgBot!</b>\n Данный бот служт для того, чтобы предать огласке проблему вандализма\n Разработчики не пропагандируют данное движение, но просят не портить окр.среду\n\n Вандализм уголовно наказуемое преступление, творите добро и приятного пользования ботом!')
    await message.delete()

@dp.message(Command('street')) #Поиск по выбранному району, если район не выбранн по-муолчанию стоит Ворошиловский
async def street(message: Message):
    street_area = mass.pop(0)
    if street_area == 'Центральный':
        await message.answer('Все доступные объекты по улицам Центрального района', reply_markup=keyboard.area_centr())
    elif street_area == 'Ворошиловский':
        await message.answer('Все доступные объекты по улицам Ворошиловского района', reply_markup=keyboard.area_vor())
    elif street_area == 'Краснооктябрьский':
        await message.answer('Вы видите все адреса объектов Краснооктябрьского района ', reply_markup=keyboard.area_ko())
    elif street_area == 'Советский':
        await message.answer('Вы видите все адреса объектов Советского района ', reply_markup=keyboard.area_sov())
    elif street_area == 'Кировский':
        await message.answer('Вы видите все адреса объектов Кировского  района ', reply_markup=keyboard.area_kir())
    await message.delete()


# @dp.message()
# async def send_photo_file_id(message: Message):
#     await message.reply(message.photo[-1].file_id)

@dp.message() #Принимаем сообщение от пользователя 
async def echo(message: Message):
    msg = message.text.lower() #Переводим весь текст сообщения в нижний регистр
    area_vibor = area
    if msg == 'районы': #Если пользователь нажал на кнопку "Районы", то
        await message.answer('Вы видите все доступные на данный момент районы города Волгоград', reply_markup=keyboard.area_kb) #Выводим новую клавиатуру с районами
    elif msg == 'удалить объект':
        await message.answer('Вы можете отправить фотоотчёт о том, что объект облагородили и мы удалим его из базы данных', reply_markup=keyboard.add_delete_kb)
    elif msg == 'добавить объект':
        await message.answer('Вы можете добавить новый объект, подвергшийся действиям вандализма через администратора бота', reply_markup=keyboard.add_delete_kb)
    elif msg == 'ворошиловский':
        area_vibor = 'Ворошиловский'
        mass.insert(0, area_vibor)
        await message.answer(f'Вы видите все адреса объектов района {area_vibor}', reply_markup=keyboard.area_vor())
    elif msg == 'центральный':
        area_vibor = 'Центральный'
        mass.insert(0, area_vibor)
        await message.answer(f'Вы видите все адреса объектов района {area_vibor}', reply_markup=keyboard.area_centr()) 
    elif msg == 'краснооктябрьский':
        area_vibor = 'Краснооктябрьский'
        mass.insert(0, area_vibor)
        await message.answer(f'Вы видите все адреса объектов района {area_vibor}', reply_markup=keyboard.area_ko())
    elif msg == 'советский':
        area_vibor = 'Советский'
        mass.insert(0, area_vibor)
        await message.answer(f'Вы видите все адреса объектов района {area_vibor}', reply_markup=keyboard.area_sov())
    elif msg == 'кировский':
        area_vibor = 'Кировский'
        mass.insert(0, area_vibor)
        await message.answer(f'Вы видите все адреса объектов района {area_vibor}', reply_markup=keyboard.area_kir())
    elif msg == 'назад':
        await message.answer('Выберите район', reply_markup=keyboard.area_kb)
    elif msg == 'благотворительность':
        await message.answer('Дабы поднять мотивацию для благодеятелей, наша команда решила ввести рекламу в боте.\nЧтобы попасть к нам в избранные закрашивай графити на отмеченных объектах\nи присылай в телеграмм или вк админу фото и видео подтверждение.', reply_markup=keyboard.add_delete_kb)
    elif msg == 'мира 30':
        await message.answer_photo(photo="AgACAgIAAxkBAAICM2UaRU_SoH3vUeHvF5pFlkotXXNeAAKBzjEbcNrRSJH0D5zhkuJFAQADAgADeQADMAQ", caption='Стена')
        await message.answer_photo(photo="AgACAgIAAxkBAAICMWUaRToU5QQMrU3mCCShVXteN8ZYAAJ_zjEbcNrRSDIO5-ntIiDVAQADAgADeQADMAQ", caption='Вход')
    elif msg == 'комсомольская 6': 
        await message.answer_photo(photo="AgACAgIAAxkBAAIDZWUk9r94wwbVPNLANubAqpldVZwTAAJ_zTEbwMgpSQx5IVZrlwrPAQADAgADeAADMAQ", caption='Дом')
    
    else:
        await message.answer('Вы ввели не корректный запрос')




        
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())