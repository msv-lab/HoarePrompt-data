t = int(input())
results = []
for i in range(t):
    n = int(input())
    arr = input()
    if n % 2 == 0:
        results.append('no')
    elif arr.count('U') > arr.count('D'):
        results.append('yes')
    else:
        results.append('no')
for i in results:
    print(i)