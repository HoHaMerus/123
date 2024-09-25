def F(n):
    if n == 1:
        return 3
    else:
        n > 2
        return F(n-1)*(n-1)
n = int(input("Enter n: "))
print(f"F({n}) = {F(n)}")