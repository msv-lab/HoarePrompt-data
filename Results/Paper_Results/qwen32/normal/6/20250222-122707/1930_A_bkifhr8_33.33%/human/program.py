t = int(input())
ans_f = []
 
for i in range(t):
    ans = 0
    n = int(input())
    l = input()
    lst = l.split(" ")
    for i in range(n * 2):
        if(len(lst) != 2):
            ans += min(int(lst[0]), int(lst[1]))
            lst.remove(lst[0*2])
            lst.remove(lst[1*2])
        else:
            ans += min(int(lst[0]), int(lst[1]))
            break
 
 
    ans_f.append(ans)
 
for i in ans_f:
    print(i)