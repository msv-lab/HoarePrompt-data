import sys
from collections import defaultdict
strInp = lambda : raw_input().strip().split()
intInp = lambda : list(map(int,strInp()))

n , m, k = intInp()
arr = intInp()
school = intInp()
index = intInp()
values = []
for i in index:
    values.append(arr[i-1]) 

s_in_s = defaultdict(list)

for i in range(n):
    s_in_s[school[i]].append(arr[i])
ans = 0
for j in values:
    for i in range(1,m+1):
        if j != max(s_in_s[i]) and j in s_in_s[i]:
            ans += 1
            break
print(ans)            

