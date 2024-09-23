n = int(input('Введите число '))
sum = 0
mult = 1
while n>0:
    sum += n%10
    mult *= n%10
    n = n//10
print("Сумма:", sum)
print("Произведение:", mult)