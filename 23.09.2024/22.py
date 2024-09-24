lst_str=["Камила", "Владимир", "Роман","Ли", "Мия"]
a = []
for name in lst_str:
    a.append(len(name))
new_list = str(a).replace(",", "")
print(new_list)