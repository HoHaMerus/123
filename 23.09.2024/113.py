a = int(input())

ch = 0
nc = 0

while a > 0:
    if a % 2 == 0:
        ch += 1
    else:
        nc += 1
    a = a // 10

print(f'Четных: {ch}, Нечетных: {nc}')