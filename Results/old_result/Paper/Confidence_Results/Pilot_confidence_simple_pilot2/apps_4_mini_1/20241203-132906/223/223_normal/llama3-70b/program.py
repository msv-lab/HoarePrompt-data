import math

n = int(input())
orig_n = n
min_ops = float('inf')

for i in range(len(str(n)), -1, -1):
    for j in range(i, len(str(n))+1):
        num_str = str(n)[:i] + str(n)[j:]
        if num_str and num_str[0] != '0':
            num = int(num_str)
            root = math.sqrt(num)
            if root == int(root):
                min_ops = min(min_ops, len(str(orig_n)) - len(num_str))

if min_ops == float('inf'):
    print(-1)
else:
    print(min_ops)
