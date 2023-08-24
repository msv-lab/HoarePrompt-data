n, k = map(int, input().split())

count = 0
for i in range(n):
    num = input()
    
    if set(num) - set(str(k+1)) == set():
        count += 1

print(count)