# -*- coding: utf-8 -*-
"""Divisors.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JNIjKIBMQXm71mPewslJdUUqvok4j4Ug

Divisors

https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""

# obtain user input and print ou list of all divisors

usr_inpt = int(input('enter a divisor: '))

x = list(range(usr_inpt))

divisors = []

for i in x:
  if i == 0:
    continue
  elif usr_inpt % x[i] == 0:
    divisors.append(x[i])

print(divisors)