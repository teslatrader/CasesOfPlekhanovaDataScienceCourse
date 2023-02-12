# Задача 2
# Дано трёхзначное число.
# Напишите программу, которая определяет: есть ли среди цифр заданного целого трёхзначного  числа одинаковые.
# Пример входных данных.
# Пример выходных данных
# 123 Нет
# 121 Да
# 222 Да

numbers = list(input('Введите число.\n'))
print(numbers)
is_repeat = False
need_stop = False
for idx, number in enumerate(numbers):
  for i, num in enumerate(numbers):
    if  idx != i and number == num:
      is_repeat = True
      need_stop = True
      break
  if need_stop:
    break

if is_repeat:
  print('У нас дубликат!')
else:
  print('У нас нет дублей!')