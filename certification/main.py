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
import plotly.express as px

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
min_per_call.columns = ['Call datetime', 'Operator', 'Duration']
print(f'\nДатафрейм с агрегацией минут по звонкам\n')
print(min_per_call.tail())

# Создаем датафрейм с агрегацией минут по дням
min_per_day = pd.DataFrame()
min_per_day['Duration'] = calls.groupby(calls['Call datetime'].dt.date)['Minutes'].sum()
min_per_day.reset_index(inplace=True)
min_per_day.columns = ['Call datetime', 'Duration']
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

# Создаем датафрейм с агрегацией минут по звонкам кроме звонков на МТС
temp = min_per_call_mts = pd.DataFrame()
temp = min_per_call.copy()
temp.columns = ['Call datetime', 'Operator', 'Duration']
temp['Duration'] = temp.apply(lambda x: 0 if x['Operator'] == 'мтс' else x['Duration'], axis=1)
temp = temp[temp['Duration'] > 0]
temp.drop(columns=['Operator'], inplace=True)
min_per_call_mts['Duration'] = temp.groupby(temp['Call datetime'].dt.date)['Duration'].sum()
min_per_call_mts.reset_index(inplace=True)

print(f'\nДатафрейм с агрегацией минут по звонкам кроме звонков на МТС\n')
print(min_per_call_mts)
print_stars_sep()

def GetMonstrOfTalk(data: list) -> float:
    cost_0_1_min = 1.5
    cost_2_9_min = 0.5
    cost_10_plus_min = 1.0
    result = 0.0

    def GetCostFirstMinute():
        return cost_0_1_min

    def GetCostTwoNineMinutes(minutes_total=9):
        minutes_total -= 1
        return GetCostFirstMinute() + minutes_total * cost_2_9_min

    def GetCostTenPlusMinutes(minutes_total):
        minutes_total -= 9
        return GetCostTwoNineMinutes() + minutes_total * cost_10_plus_min

    for value in data:
        if value <= 1:
            result += GetCostFirstMinute()
        elif 2 <= value <= 9:
            result += GetCostTwoNineMinutes(value)
        elif 10 <= value:
            result += GetCostTenPlusMinutes(value)
    return round(result, 2)

def GetWantToTell(data: list) -> float:
    cost_0_5_min = 3.95
    cost_6_plus_min = 0.4
    result = 0.0

    def GetCostFiveMinutes(minutes_total=5):
        return minutes_total * cost_0_5_min

    def GetCostSixPlusMinutes(minutes_total):
        minutes_total -= 5
        return GetCostFiveMinutes() + minutes_total * cost_6_plus_min

    for value in data:
        if value <= 5:
            result += GetCostFiveMinutes(value)
        else:
            result += GetCostSixPlusMinutes(value)

    return round(result, 2)

def GetMoreWords(data: list) -> float:
    cost_monthly_fee = 555              # абонентская плата
    cost_exceeded_min = 1.95            # стоимость минуты превышающей лимит на месяц в 555 минут включительно
    result = 0.0

    for value in data:
        result += 555 + (0 if value <= 555 else ((value - 555) * cost_exceeded_min))

    return round(result, 2)

def GetMegafon(data: list) -> float:
    cost_0_1_min = 1
    cost_2_plus_min = 0.33
    result = 0.0

    def GetCostFirstMinute():
        return cost_0_1_min

    def GetCostTwoPlusMinutes(minutes_total):
        minutes_total -= 1
        return round(GetCostFirstMinute() + minutes_total * cost_2_plus_min, 2)

    for value in data:
        if value <= 1:
            result += GetCostFirstMinute()
        else:
            result += GetCostTwoPlusMinutes(value)

    return round(result, 2)

def GetMTS(data: list) -> float:
    cost_0_5_min = 0.9
    cost_6_30_min = 0.05
    cost_30_plus = 0.9
    result = 0.0

    def GetCostFirstFiveMinutes(minutes_total=5):
        return minutes_total * cost_0_5_min

    def GetCostSixThirtyMinutes(minutes_total=30):
        minutes_total -= 5
        return GetCostFirstFiveMinutes() + minutes_total * cost_6_30_min

    def GetCostThirtyPlusMinutes(minutes_total):
        minutes_total -= 30
        return GetCostSixThirtyMinutes() + minutes_total * cost_30_plus

    for value in data:
        if value <= 5:
            result += GetCostFirstFiveMinutes(value)
        elif 6 <= value <= 30:
            result += GetCostSixThirtyMinutes(value)
        elif 31 <= value:
            result += GetCostThirtyPlusMinutes(value)

    return round(result, 2)

# Считаем затраты по тарифам и агрегируем в датафрейм
results = {
    'Билайн - Монстр общения': [GetMonstrOfTalk(min_per_call['Duration'].to_list())],
    'Билайн - Хочу сказать': [GetWantToTell(min_per_day['Duration'].to_list())],
    'Билайн - Больше слов': [GetMoreWords(min_per_month['Duration'].to_list())],
    'Мегафон - 33 копейки': [GetMegafon(min_per_call['Duration'].to_list())],
    'МТС - Много звонков': [GetMTS(min_per_call_mts['Duration'].to_list())]
}

result_df = pd.DataFrame(data=results)
result_df.sort_values(by=0, axis=1, inplace=True)
print(result_df)
print_stars_sep()

# Рисуем графики
fig = px.bar(x=result_df.columns, y=result_df.values[-1], title='Сравнение расходов на мобильную связь по возможным тарифам')
fig.update_xaxes(title='Тарифы')
fig.update_yaxes(title='Расходы, руб.')
fig.show()