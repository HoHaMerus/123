def calculate_F(n):
    if n 1:
        return 1
    else:
        return calculate_F(n-1) * calculate_F(n-1) (n-1)

n=int(input('Введите значение n⁚ '))
result calculate_F(n)
print('Значение F({}) {}'․format(n, result))