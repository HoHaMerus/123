#Имитация броска кубика

import random
import os

#Выбор колличества кубиков

def brosok():
  while True:
      try:
          kol_kubikov = input("Количество кубиков: ")
          otvet = ["1", "2"]
          if kol_kubikov not in otvet:
              raise ValueError("Можно выбрать 1 или 2")
          else:
              return kol_kubikov
      except ValueError as er:
          print(er)

#Бросок кубика

def brosok_kubikov():
   min = 1
   max = 6
   povtor = "y" 

   while povtor.lower() =="y":
       os.system("cls" if os.name == "nt" else "clear")
       amount = brosok()

       if amount == "2":
           
           kubik1 = random.randint(min, max)
           kubik2 = random.randint(min, max)

           
           print("Первый кубик: ", kubik1)
           print("Второй кубик: ", kubik2)
           print("Результат: ", kubik1 + kubik2)

           povtor = input("Бросаем еще: ")
       else:
           kubik1 = random.randint(min, max)
           print(f"Результат: {kubik1}")

           povtor = input("Бросаем еще: ")


if __name__ == '__main__':
   brosok_kubikov()