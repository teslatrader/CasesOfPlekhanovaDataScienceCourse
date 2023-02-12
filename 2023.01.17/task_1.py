# Задача 1.
# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.

test_string = "some text"
print(f'original text is \"{test_string}\"')

txt_split = test_string.split(' ')

result = txt_split[1] + " " + txt_split[0]

print(f'final text is \"{result}\"')