import tkinter as tk
from tkinter import ttk
import requests


def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def update_cur_options():
    rates_data = get_exchange_rates()
    if rates_data:
        cur_codes = list(rates_data['rates'].keys())
        b_cur1_combobox['values'] = cur_codes
        b_cur2_combobox['values'] = cur_codes
        target_cur_combobox['values'] = cur_codes


def exchange():
    rates_data = get_exchange_rates()
    if rates_data:
        b_cur1 = b_cur1_var.get()
        b_cur2 = b_cur2_var.get()
        target_cur = target_cur_var.get()

        if b_cur1 in rates_data['rates'] and target_cur in rates_data['rates']:
            exchange_rate1 = rates_data['rates'][target_cur] / rates_data['rates'][b_cur1]
            result1_var.set(f'1 {b_cur1} = {exchange_rate1:.2f} {target_cur}')
        else:
            result1_var.set('Неверный выбор "Базовой валюты №1"')

        if b_cur2 in rates_data['rates'] and target_cur in rates_data['rates']:
            exchange_rate2 = rates_data['rates'][target_cur] / rates_data['rates'][b_cur2]
            result2_var.set(f'1 {b_cur2} = {exchange_rate2:.2f} {target_cur}')
        else:
            result2_var.set('Неверный выбор "Базовой валюты №2"')
    else:
        result1_var.set('Ошибка получения данных')
        result2_var.set('Ошибка получения данных')


window = tk.Tk()
window.title("Конвектор курса валют")
window.geometry("165x380")

b_cur1_var = tk.StringVar(value='USD')
b_cur2_var = tk.StringVar(value='EUR')
target_cur_var = tk.StringVar(value='RUB')
result1_var = tk.StringVar()
result2_var = tk.StringVar()

b_cur1_label = ttk.Label(text="Базовая валюта №1:")
b_cur1_label.pack(padx=10, pady=10)

b_cur1_combobox = ttk.Combobox(textvariable=b_cur1_var)
b_cur1_combobox.pack(padx=10, pady=10)

b_cur2_label = ttk.Label(text="Базовая валюта №2:")
b_cur2_label.pack(padx=10, pady=10)

b_cur2_combobox = ttk.Combobox(textvariable=b_cur2_var)
b_cur2_combobox.pack(padx=10, pady=10)

target_cur_label = ttk.Label(text="Целевая валюта:")
target_cur_label.pack(padx=10, pady=10)

target_cur_combobox = ttk.Combobox(textvariable=target_cur_var)
target_cur_combobox.pack(padx=10, pady=10)

exchange_button = ttk.Button(text="Конвертировать", command=exchange)
exchange_button.pack(padx=10, pady=10)

result1_label = ttk.Label(textvariable=result1_var)
result1_label.pack(padx=10, pady=10)

result2_label = ttk.Label(textvariable=result2_var)
result2_label.pack(padx=10, pady=10)

update_cur_options()

window.mainloop()
