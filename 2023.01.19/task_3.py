# Кейс.
# Компания ужесточает требования к паролям.
# Пароль может быть задан пользователем, однако к нему есть требования:
# Не может содержать менее 10 символов
# Обязательно содержит одну заглавную букву
# Все буквы должны быть латинскими
# В пароле должны содержаться символы @,~,*,(,)
# Создайте код с использованием цикла для модернизации проверки паролей

list_of_special = []
list_of_allowed = ['@', '~', '*', ',', '\'']

def CheckLenght(psw):
  if len(psw) < 10:
    print(f'Your psw is shorter than allowed length - 10 symbols.')
    return False
  else:
    print(f'Your psw has enough lenght.')
    return True

def CheckAlpha(psw):
  global list_of_special
  for letter in psw:
    # print(f'\n\nChecking this character = {letter}\n')
    if not letter.isalpha():
      list_of_special.append(letter)
  return True

def CheckSpecialSymbols(psw):
  global list_of_special, list_of_allowed
  for char in list_of_special:
    if char not in list_of_allowed:
      print(f'Your psw has symbol which is not allowed = {char}.')
      return False

  for char in psw:
    if char in list_of_allowed:
      print('Your psw has allowed special symbol.')
      return True

  print(f'Special symbols *{list_of_allowed} were not found!')
  return False


def CheckCapital(psw):
  for letter in psw:
    if letter.upper() == letter and letter not in list_of_special:
      print('Your psw has at least one capital letter.')
      return True
  print('Your psw doesn\'t have at least one capital letter.')
  return False


def DoCheck():
  global list_of_special
  list_of_special = []
  psw_to_check = input('New password for check.\n\n')

  if not CheckLenght(psw_to_check):
    return False
  elif not CheckAlpha(psw_to_check):
    return False
  elif not CheckSpecialSymbols(psw_to_check):
    return False
  elif not CheckCapital(psw_to_check):
    return False
  print('Your password matches our requirements!')
  return True

while True:
  if DoCheck():
    break