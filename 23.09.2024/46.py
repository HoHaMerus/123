dict1={"id324": 167,"id95": 204,"id326": 45,"id327": 90,"id328": 3,"id329": 43,"id405": 27,"id567": 10}
dict2=dict1.copy()
for key, value in dict2.items:
    if value % 2 == 0:
        del dict2[key]
keys=list(dict2.keys)
print(dict2)