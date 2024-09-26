def a(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ynikalnie_elementi = set1 - set2
    return len(ynikalnie_elementi)

str1 = "хочу играть"
str2 = "программировать"

result = a(str1, str2)
print(result)