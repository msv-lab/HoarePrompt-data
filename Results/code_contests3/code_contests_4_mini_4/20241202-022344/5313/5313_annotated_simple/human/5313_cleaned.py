n = int(input())
x = int(n ** 0.5)
if x ** 2 == n:
    answr = x * 4
elif x * (x + 1) > n:
    answr = (x + x + 1) * 2
else:
    answr = 4 * (x + 1)
answr = int(answr)
print(answr)