import pandas as pd
from django.shortcuts import render

def index(request):
    file_path = '/home/muhammadjon/5_кл_математика_1_четверть_@e_baza_ishreja.ods'
    data = pd.read_excel(file_path)

    # Oxirgi ustunni olib, progress bar uchun qiymatlarni normallashtirish
    last_column = data.iloc[:, -1]  # DataFrame'dagi oxirgi ustunni olish
    max_value = last_column.max()    # Maksimal qiymatni topish
    min_value = last_column.min()    # Minimal qiymatni topish

    # Progress bar uchun normallashtirilgan qiymatlarni yangi ustunga qo‘shish
    data['progress'] = ((last_column - min_value) / (max_value - min_value) * 100).fillna(0)

    return render(request, 'index.html', {'data': data})
