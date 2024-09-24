password = input("Введите пароль: ") 
 
for i in range(5): 
    print(f"Попытка {i+1} из 5") 
    letter = input("Введите букву: ") 
    if letter in password: 
        for j in range(len(password)): 
            if password[j] == letter: 
                print(f"Буква нашлась на месте {j+1}") 
    else: 
        print("Буква не нашлась") 
 
guess = input("Введите слово: ") 
if guess == password: 
    print("Пароль подошёл!") 
else: 
    print("Пароль не подошёл")