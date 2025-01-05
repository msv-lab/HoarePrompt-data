lst = (raw_input().split())
#print(lst)

lst.sort()
lst.reverse()
lst = list(map(int, lst))
#lst = [int(x) for x in lst]
#print(lst)

ans = 10*lst[0] + lst[1] + lst[2]
print(ans)