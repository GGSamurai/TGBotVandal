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
            KeyboardButton(text = "Инфо о командах")
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
