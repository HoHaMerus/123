fn = input("Введите фамилию, имя и отчество: ") 
n = fn.split() 
fa = n[0] 
i = f"{n[1][0]}.{n[2][0]}." 
print(f"{n} {i}")