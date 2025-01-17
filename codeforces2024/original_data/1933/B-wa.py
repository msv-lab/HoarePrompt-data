# This is a sample Python script.
a = int(input())
b = int(input())
c = list(map(int, input().split()))
s = 0
y = 0
for i in range(b):
    s += c[i]
    if c[i] % 3 == 1:
        y += 1
if s % 3 == 0:
    print(0)
if s % 3 == 2:
    print(1)
if s % 3 == 1:
    if y > 0:
        print(1)
    else:
        print(2)