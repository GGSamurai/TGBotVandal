from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
    keyboard =[
        [
            KeyboardButton(text = "Районы"),
            KeyboardButton(text = "Показать адреса")
        ],
        [
            KeyboardButton(text = "Удалить объект"),
            KeyboardButton(text = "Инфо о командах")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)


menu_kb = ReplyKeyboardMarkup(
    keyboard =[
        [
            KeyboardButton(text = "Районы"),
            KeyboardButton(text = "Показать адреса")
        ],
        [
            KeyboardButton(text = "Удалить объект"),
            KeyboardButton(text = "Добавить объект")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)


area_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Ворошиловский"),
            KeyboardButton(text = "Центральный")
        ],
        [
            KeyboardButton(text = "Краснооктябрьский")
        ],
        [
            KeyboardButton(text = "Советский"),
            KeyboardButton(text = "Кировский")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите район из меню',
    selective=True
)

add_delete_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='VKontakte', url="https://vk.com/v.fatt"),
            InlineKeyboardButton(text='Telegram', url="t.me//moy_korolb")
        ]
    ],
    resize_keyboard=True
)
