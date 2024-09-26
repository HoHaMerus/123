lst=list(map(int,input().split()))
print(lst)
print(sorted(lst,key=lambda x:x%10))