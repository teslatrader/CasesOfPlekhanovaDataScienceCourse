# Задача 2.
# В торговом центре проводится розыгрыш призов. Для получения приза необходимо загадать число.
# Случайным образом администраторы выбирают второе число в интервале от 1 до 9. Те пользовательские номера,
# сумма цифр которого делятся нацело на загаданное администрацией число, считаются выигрышными.
# Компания обратилась к вам, чтобы вы разработали приложение, которое будет осуществлять вывод в консоль
# выигрышных номеров.
# Если выигрышных номеров слишком много, отбираются первые 5, то есть как только в консоль выведено 5 игроков,
# розыгрыш заканчивается.

import numpy as np

users_numbers = (np.random.randint(low=1, high=1000, size=100)).tolist()
print(f'Users numbers:\n{users_numbers}\n')

winners_qty = int(input('Input quantity of winners.\n'))

print('\n')

def GetAdminRandomNumber():
  admin_random_number = np.random.randint(1, 9, 2)
  # print(f'New admin random list is = {admin_random_number}\n')
  print(f'New admin random number is = {admin_random_number[1]}\n')
  return(admin_random_number[1])


def GetNumberSum(_number):
  _sum = 0
  # print(f'User number is {_number}.\n')
  for num in str(_number):
    _sum += int(num)
  # print(f'Sum of users numbers is {_sum}.\n')
  return _sum


def PrintResults(winners, adm_random):
  print(f'\n\nAdmin random number was = {adm_random}\n\n')
  print(f'We are happy to name the WINNERS:\n')
  for idx, winner in enumerate(winners):
    print(f'{idx + 1} place is for {winner}')


def GetWinner():
  global winners_qty, users_numbers
  list_of_winners = []

  adm_random = GetAdminRandomNumber()

  for user in users_numbers:
    sum_of_number = GetNumberSum(user)
    if sum_of_number % adm_random == 0:
      list_of_winners.append(user)
      if len(list_of_winners) == winners_qty:
        break
  PrintResults(list_of_winners, adm_random)

GetWinner()