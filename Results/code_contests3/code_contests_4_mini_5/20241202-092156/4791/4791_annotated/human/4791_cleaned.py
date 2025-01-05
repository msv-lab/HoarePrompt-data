n = input()
while n:
    n -= 1
    for j in range(n):
        print(bin(j + 1)[::-1].find('1') + 1)