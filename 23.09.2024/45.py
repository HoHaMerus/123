def a(imena):
    p = imena.split()
    dict = {i + 1: x for i, x in enumerate(p)}
       
    dlinnoe_imya = max(p, key=len)
    ego_index = p.index(dlinnoe_imya) + 1

    del dict[ego_index]
    
    return dict

r = a(input("Введите имена питомцев: "))

print(r)