n = int(input())
count = 0

if n == 1:
    print(0)
else:
    for i in range(1, n+1):
        if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 and i % 10 != 0:
            count += 1
            
    print(count)