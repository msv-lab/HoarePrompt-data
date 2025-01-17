n, s = input()
n = int(n)
pos = 'abcdef'.index(s) + 1

t = (n - 1) // 2
t *= 6
t += (n - 1) % 2
t += 3 - pos

print(t + 1)
