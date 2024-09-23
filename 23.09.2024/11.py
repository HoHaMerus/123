n = int (input('Число: '))
i = 1
sum = 0
while i <= n:
    print(i)
    sum = sum + i
    i = i + 1
answer = 'Суммачиселот 1 до ' + str(n) + ' равна ' + str(sum)
print(answer)
