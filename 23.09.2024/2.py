p = "23"
 
for i in range(3): 
    print(f"Попытка {i+1} из 3") 
    c = input("Попробуй угадай: ")             
    if  c in p: 
        print("Да ты счастливчик") 
        break
    else: 
        print("Мимо")