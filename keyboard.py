from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
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


#Начинается полная путаница, пригтовьтесь, 5 районов = 5 кнопок, нажимая на которые, будут выходить инлайн кнопки с адресами

def area_kb_vor():
    items = [
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
    ]
    builder = InlineKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Назад")
    builder.adjust(*[4]*4)

    return builder.as_markup(resize_keyboard=True)

def area_kb_ko():
    items = [
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
    ]
    builder = InlineKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Назад")
    builder.adjust(*[4]*4)

    return builder.as_markup(resize_keyboard=True)


def area_kb_kir():
    items = [
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
    ]
    builder = InlineKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Назад")
    builder.adjust(*[4]*4)

    return builder.as_markup(resize_keyboard=True)


def area_kb_sov():
    items = [
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
    ]
    builder = InlineKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Назад")
    builder.adjust(*[4]*4)

    return builder.as_markup(resize_keyboard=True)


def area_kb_centr():
    items = [
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
        "Мира 10","Мира 10","Мира 10","Мира 10",
    ]
    builder = InlineKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Назад")
    builder.adjust(*[4]*4)

    return builder.as_markup(resize_keyboard=True)



