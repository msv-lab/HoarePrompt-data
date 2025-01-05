lst = raw_input().split()
lst.sort()
lst.reverse()
lst = list(map(int, lst))
ans = 10 * lst[0] + lst[1] + lst[2]
print(ans)