# Задача 1
# Используя полное ветвление, упростите следующий фрагмент программы:
#
# if a > b:  c = 1
# # if a > b: d = 2
# # if a <= b: c = 3
# # if a <= b: d = 4

import numpy as np

a = np.random.random()
b = np.random.random()
c = d = 0.0
print(a, b, c, d)
if a > b:
  c = 1
  d = 2
else:
  c = 3
  d = 4
print(a, b, c, d)