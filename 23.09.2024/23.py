# s1 = list(input('Введите строку: ').lower())
#
# s2=[]
# for i in s1:
#     if i!=' ':
#         s2.append(i)
# print(s2)

s2=list(input().lower())
print([i for i in s2 if i!=' '])