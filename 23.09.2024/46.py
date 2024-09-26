dict1 = {'id324': 167, 'id95': 204, 'id326': 45, 'id327': 90, 'id328': 3, 'id329': 43, 'id405': 27, 'id567': 10}
dict2 = dict1.copy()
for key in list(dict2.keys()):
    if dict2[key] % 2 == 0:
        del dict2[key]
print(list(dict2.keys()))
