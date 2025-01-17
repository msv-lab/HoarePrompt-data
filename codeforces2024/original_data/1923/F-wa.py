# for _ in range(int(input())):
#     n, q = list(map(int, input().split()))
#     c = list(map(int, input().split()))
#     for i in range(q):
#         l, r = list(map(int, input().split()))

n, k = list(map(int, input().split()))
s = list(input())
ones = s.count('1')
left = 0
right = n-1
while s[left] == "0":
    left += 1
while s[right] == '0':
    right -= 1
while k > 0 and (right - left + 1) != ones:
    mid = (right + left) // 2
    if s[left:mid+1].count('0') < s[mid+1:right].count('0'):
        s = s[left:]
        s = s[::-1]
        # print('type 1')
    else:
        ind = right - 1
        # print('type 2')
        while s[ind] == '1':
            ind -= 1
        if k == 1 and s[-1] == '0':
            ind = -1
        s[left], s[ind] = s[ind], s[left]
    left = 0
    right = len(s)-1
    while s[left] == "0":
        left += 1
    while s[right] == '0':
        right -= 1
    k -= 1
    # print(left, right, k, s)
res = 0
for i in range(left, len(s)):
    if s[i] == '1':
        res += 1
    res <<= 1
    # print('res', res)
res >>= 1
print(res % 1000000007)