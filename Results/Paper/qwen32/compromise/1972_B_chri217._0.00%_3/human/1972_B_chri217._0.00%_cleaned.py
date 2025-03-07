def func_1(s):
    num_up = s.count('U')
    if num_up % 2 == 1:
        return 'YES'
    else:
        return 'NO'
input = sys.stdin.read
data = input().split()
t = int(data[0])
for _ in range(t):
    n = int(data[1])
    s = data[2]
    print(func_1(s))