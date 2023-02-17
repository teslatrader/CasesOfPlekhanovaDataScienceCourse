# Абонент хочет оптимизировать свои затраты на связь, сменив текущий тарифный план.
#
# Три оператора сотовой связи прислали свои предложения: описание всех тарифных планов
# агрегированы в единый документ. Имеется также выгрузка исходящих вызовов абонента за последние 6 месяцев.
#
# Необходимо исследовать характер исходящих звонков абонента и предложить оптимальный тариф,
# обосновав свои рекомендации аналитическими расчетами.

#                                   План действий:
# - загрузить историю звонков
# - подготовить загруженные данные для последующей обработки и анализа
# - скалькулировать стоимость сделанных звонков в разрере предложенной тарификации
# - сравнить полученные значения и выбрать оптимальный тариф

# Калькуляция стоимости звонка в завиимости от плана:
#  Билайн - Монстр общения (поминутный):                                     <= 1 по 1.5    2 <= 9 по 0.5  10 <= 1.0
#  Билайн - Хочу сказать (поминутный, минут в день):                         <= 5 по 3.95   6 <= 0.4       sms 1.5
#  Билайн - Больше слов (абонентская плата):                                 <= 555 за 555  556 <= 1.95
#  Мегафон - 33 копейки (поминутная):                                        <= 1 по 1      2 <= по 0.33
#  МТС - Много звонков (поминутная, на сторонних операторов, минут в день):  0 <= 5 по 0.9  6 <= 30 0.05   31 <= по 0.9

import pandas as pd
import math

def print_stars_sep():
    """Вспомогательная функция для красивого принта отступов"""
    print_stars_shift = 90
    print(f'\n{"*" * print_stars_shift}\n')

# Загрузка данных
calls = pd.read_excel('calls.xlsx')
print(f'\nДатафрейм загружен\n')
print(calls.tail())
print(calls.dtypes)
print_stars_sep()

#
# ПОДГОТОВКА ДАННЫХ К РАБОТЕ
#
# Переименовываем столбцы для удобства и очищаем датафрейм, проверяем итоговые типы данных
calls.columns = ['Call datetime', 'Duration', 'Operator']
calls.drop_duplicates(inplace=True)

# Форматируем дату и время звонка и получаем длительность звонка в округленных минутах
calls['Call datetime'] = pd.to_datetime(calls['Call datetime'], dayfirst=True)
calls.sort_values(by='Call datetime')
calls.reset_index(drop=True, inplace=True)
calls['Seconds'] = pd.to_timedelta(calls['Duration']).dt.total_seconds().astype(int)
calls['Minutes'] = (calls['Seconds'] / 60).apply(lambda x: math.ceil(x))
print(f'\nБазовый датафрейм\n')
print(calls.tail())
print(calls.dtypes)
print_stars_sep()

# Создаем датафрейм с агрегацией минут по звонкам
min_per_call = pd.DataFrame()
min_per_call = calls.copy()
min_per_call.drop(columns=['Duration', 'Seconds'], inplace=True)
print(f'\nДатафрейм с агрегацией минут по звонкам\n')
print(min_per_call.tail())

# Создаем датафрейм с агрегацией минут по дням
min_per_day = pd.DataFrame()
min_per_day['Duration'] = calls.groupby(calls['Call datetime'].dt.date)['Minutes'].sum()
min_per_day.reset_index(inplace=True)
min_per_day.columns = ['Date', 'Duration']
print(f'\nДатафрейм с агрегацией минут по дням\n')
print(min_per_day.tail())
print_stars_sep()

# Создаем датафрейм с агрегацией минут по месяцам
min_per_month = pd.DataFrame()
min_per_month['Duration'] = calls.groupby(calls['Call datetime'].dt.month)['Minutes'].sum()
min_per_month.reset_index(inplace=True)
min_per_month.columns = ['Month', 'Duration']
print(f'\nДатафрейм с агрегацией минут по месяцам\n')
print(min_per_month)
print_stars_sep()

# Создаем датафрейм с агрегацией минут по звонкам кроме звонков на МТС (кейс МТС)
min_per_call_mts = min_per_call.copy()
min_per_call_mts.columns = ['Call datetime', 'Operator', 'Duration']
min_per_call_mts['Duration'] = min_per_call_mts.apply(lambda x: 0 if x['Operator'] == 'мтс' else x['Duration'], axis=1)
min_per_call_mts = min_per_call_mts[min_per_call_mts['Duration'] > 0]
min_per_call_mts.reset_index(inplace=True, drop=True)
print(f'\nДатафрейм с агрегацией минут по звонкам кроме звонков на МТС\n')
print(min_per_call_mts.tail())





