# # Кейс
# Директор цеха официального дилера автомобилей дорогой немецкой марки просит вас разработать программу,
# которая выводила бы на экран калькуляцию по осмотру автомобиля и объему планируемых работ.
# Калькуляция должна выводиться в следующем виде:
# **Расчет работ по представленному автомобилю:**
# **Замена масла (работы)………….Значение переменной Oil_work_cost руб.**
# **Масло Castrol…………………………. Значение переменной Oil_price руб.**
# **Замена воздушного фильтра…. Значение переменной Filtr_work руб.**
# **Воздушный фильтр………………… Значение переменной Filtr_price руб.**
# **Итого………………………………………..Значение переменной Cost_sum руб.**
# **Персональная скидка……………………..……….3%**
# **Итого с учетом скидки…………….Net_sum_cost**
# **Спасибо, что выбираете Нас!**
# Для выполнения задания необходимо:
# Создать переменную **Oil_work_price**, равную стоимости единицы времени (заработок сотрудника в час).
# В данном случае, необходимо установить ее равной **500 руб**.#
# Создать переменную **Oil_work_time**, которая будет равна трудозатратам сотрудника на замену масла.
# Присвоить ей значение **0,7**#
# Для расчета переменной **Oil_work_cost** необходимо выполнить умножение **Oil_work_price** и **Oil_work_time**.#
# Переменная **Oil_price** должна содержать цену на масло. Закупочная цена равна **700 рублей**.
# Однако, нам необходимо включить в ее стоимость наценку, включив в нее затраты на хранение и транспортировку.
# Для расчета **Oil_price** предположим, что наценка составляет **5 процентов** от стоимости масла.
# Аналогично с переменной **Oil_work_cost** рассчитать переменную **Filtr_work**, с учетом того,
# что стоимость единицы времени **450 руб**, трудозатраты составят **0,5**.
# Аналогично переменной **Oil_price** рассчитать переменную **Filtr_price** при учете,
# что закупочная стоимость фильтра составляет 300 руб, наценка 5 процентов.
# Рассчитать значение переменной **Cost_sum**, как сумму всех проведенных работ.
# Значение **Net_sum_cost** рассчитать, как **Cost_sum** за вычетом скидки.

oil_work_price = 500
oil_work_time = 0.7
oil_price = 700
oil_nacenka = 5

filtr_work_price = 450
filtr_work_time = 0.5
filtr_price = 300
filtr_nacenka = 5

discount = 3

oil_price_total = oil_price * (1 + oil_nacenka / 100)
oil_work_cost = oil_work_price * oil_work_time

filtr_work_cost = filtr_work_price * filtr_work_time
filtr_price_total = filtr_price * (1 + filtr_nacenka / 100)

cost_sum = oil_price_total + oil_work_cost + filtr_work_cost + filtr_price_total
net_sum_cost = cost_sum * (1 - discount / 100)

calculation_output = f'==================================================\n'
calculation_output += 'РАСЧЕТ ПО ПРЕДСТАВЛЕННОМУ АВТОМОБИЛЮ:\n'
calculation_output += f'==================================================\n'
calculation_output += f'Замена масла (работы)          = {oil_work_cost} руб.\n'
calculation_output += f'Масло Castrol                  = {oil_price_total} руб.\n'
calculation_output += f'--------------------------------------------------\n'
calculation_output += f'Замена воздушного фильтра      = {filtr_work_cost} руб.\n'
calculation_output += f'Воздушный фильтр               = {filtr_price_total} руб.\n'
calculation_output += f'==================================================\n'
calculation_output += f'Итого                          = {cost_sum} руб.\n'
calculation_output += f'==================================================\n'
calculation_output += f'Персональная скидка            = {discount}%\n'
calculation_output += f'==================================================\n\n'
calculation_output += f'ИТОГО С УЧЕТОМ СКИДКИ          = {round(net_sum_cost,2)}\n\n'
calculation_output += f'**************************************************\n\n\n'
calculation_output += f'          СПАСИБО, ЧТО ВЫБИРАЕТЕ НАС\n\n'
calculation_output += f'                     **   **\n'
calculation_output += f'                    *  * *  *\n'
calculation_output += f'                    *   *   *\n'
calculation_output += f'                     *     *\n'
calculation_output += f'                      *   *\n'
calculation_output += f'                       * *\n'
calculation_output += f'                        *\n'
print(calculation_output)