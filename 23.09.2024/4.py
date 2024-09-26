lst = ([12, 45], [5, 78], [1, 87])
lst2=[]
def sum_lst():
    for i in range(len(lst)):
        lst2.append(lst[i][0] + lst[i][1])
print(sorted(lst2,key=sum_lst(), reverse=True))