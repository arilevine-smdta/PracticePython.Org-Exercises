# -*- coding: utf-8 -*-
"""Character_Input.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nkdwET8_9Ka8BHW2aICpStRFK8f4k4OY

Character Input

https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""

# have user enter name and age then return birth year and centenial
def char_input():

  char_input.name = str(input('enter your name: '))

  while True:
    try:
      char_input.age = int(input('enter your age: '))
      break
    except:
      print('enter a whole number')

char_input()

cy = 2025                   # current year
by = cy - char_input.age    # birth year
hy = by + 100               # 100 y/o

print(f'hello {char_input.name}, congratulation on becoming {char_input.age} years old')
print(f'your birth year is: {by}')
print(f'your centenial is: {hy}')

# get user input and print out a statement based on the input value

def repeat_print():
    while True:
      try:
        num = int(input('enter a number: '))
        break
      except:
        print('enter a whole number')

    for i in range(0, num):
      print(f'{i + 1}. enter a number')

repeat_print()

