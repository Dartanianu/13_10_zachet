"""Каталог товаров."""
import tkinter as tk
from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, font
)
from resources import get_product_image


def create_product_card(parent, product, refresh=None):
    """
    Создаёт карточку товара.
    """
    # TODO: количество (индекс 6)
    qty = product[6]
    # TODO: цвет фона
    bg_color = _get_card_color(qty)
    # TODO: Frame с рамкой    card = tk.Frame(parent, bg=???, bd=1, relief="solid")
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)
    # TODO: изображение и текст
    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)
    # TODO: привязать клик
    card.bind("<Button-1>", lambda e: _open_view(parent, product, refresh))
    for child in card.winfo_children():
        child.bind("<Button-1>", lambda e: _open_view(parent, product, refresh))
    return card


def _get_card_color(qty):
    """Возвращает цвет фона карточки."""
    # TODO: тернарный оператор
    return COLOR_MAIN_BG if qty > 3 else COLOR_HIGHLIGHT


def _add_image(card, product, bg_color):
    """Добавляет изображение товара (или заглушку)."""
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)
    # TODO: индекс 7
    photo = get_product_image(product[7], size=(100, 100))
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        # TODO: сохранить ссылку
        img_label.image = photo
        img_label.pack()
    else:
        tk.Label(img_frame, text="[ФОТО НЕТ]", bg=bg_color,
                 width=10, height=5).pack()


def _add_text_info(card, product, bg_color, qty):
    """Добавляет текстовую информацию о товаре."""
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True,
                    padx=10, pady=10)
    name = product[1] if product[1] else "???"
    production = product[3] if product[3] else "[Без производителя]"
    category = product[2] if product[2] else "[Без категории]"
    characteristics = product[4] if product[4] else "[Не указаны]"
    price = product[5] if product[5] is not None else 0
    _add_label(text_frame, f"{name} | {production}",
               bg_color, bold=True, size=FONT_SIZE_HEADER)
    _add_label(text_frame, f"Категория: {category}", bg_color)
    _add_label(text_frame, f"Количество: {_indicator(qty)} ({qty})", bg_color)
    _add_label(text_frame, f"Характеристики: {characteristics}", bg_color)
    _add_label(text_frame, f"{price} руб.",
               bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")


def _add_label(parent, text, bg_color, bold=False,
               size=FONT_SIZE_NORMAL, align="w"):
    """Добавляет метку с текстом."""
    tk.Label(parent, text=text, font=font(size, bold=bold),
             bg=bg_color, anchor=align).pack(fill="x")


def _indicator(qty):
    """Индикатор «много/мало» (порог 5)."""
    return "много" if qty > 5 else "мало"


def _open_view(parent, product, refresh=None):
    """Открывает форму просмотра товара."""
    from view_form import ViewForm
    ViewForm(parent, product, on_add_to_order=refresh)