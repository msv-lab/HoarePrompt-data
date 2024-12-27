# BTVN_Buoi03_Bai01
# http://codeforces.com/problemset/problem/439/B
# Name: Hoa Hoang
# Email: nobi.hoa@gmail.com

# line_1 = "2 3"
# line_2 = "4 1"
#
# line_1 = "4 2"
# line_2 = "5 1 2 1"

# n, x = map(int, line_1.split())
# C = list(map(int, line_2.split()))

n, x = map(int, raw_input().split())
C = list(map(int, raw_input().split()))


C.sort(reverse=False)
sum = 0
for i in range(0, n):
    sum += C[i] * x
    if x > 1:
        x -= 1

print(sum)