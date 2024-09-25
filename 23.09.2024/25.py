lst = [67, -45, 34, 1, -23, 989, -456, 234, -101]

print("/".join(map(str,[i for i in lst if i>=0 ])))
print("/".join([str(x) for x in lst if x > 0]))