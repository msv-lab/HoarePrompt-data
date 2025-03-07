def kkk(lst):
    sorted_lst = sorted(lst)
    return lst == sorted_lst
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    for p in range(1,len(list1)):
        if not kkk(list1):
            if list1[p-1]>list1[p] and list1[p-1]>10:
                a=list1[p-1]
                list1.pop(p-1)
                list1.insert(p-1,a//10)
                list1.insert(p,a%10)
    if kkk(list1):
        print("Yes")
    else:
        print("No")