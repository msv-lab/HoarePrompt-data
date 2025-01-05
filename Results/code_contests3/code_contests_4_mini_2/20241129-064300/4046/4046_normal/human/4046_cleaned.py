n = int(input())
(l, ans) = (len(str(n)), 4444477777)
if l & 1:
    l += 1
for i in range(l, 10, 2):
    for x in product('74', repeat=i):
        if x.count('7') == x.count('4'):
            tem = int(''.join(x))
            if tem >= n:
                ans = min(ans, tem)
print(ans)