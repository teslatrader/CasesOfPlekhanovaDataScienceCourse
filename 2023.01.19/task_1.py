# Задача1:
# Имеется строка:
# "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Необходимо разработать приложение, рассчитывающее количество уникальных символов
# (заглавные и строчные буквы – это разные символы).
# Результаты записать в переменную res и вывести в консоль.

string_to_check = input('Input string.\n')

def CountSymbolsQty(string_to_count):
  qty = len(set(list(string_to_count)))
  return qty

res = CountSymbolsQty(string_to_check)
print(res)