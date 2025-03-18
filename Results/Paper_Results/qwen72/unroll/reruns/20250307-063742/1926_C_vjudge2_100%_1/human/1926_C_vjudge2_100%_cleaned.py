def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        num = int(num / 10)
    return a
A = []
sum = 0
for i in range(1, 200001):
    a = func_1(i)
    sum = sum + a
    A.append(sum)
for t in range(int(input())):
    n = int(input())
    print(A[n - 1])