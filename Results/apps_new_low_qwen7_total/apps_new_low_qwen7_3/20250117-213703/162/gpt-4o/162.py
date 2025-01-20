def is_perfect_longcat(x):
    # Check if x is of the form 2^m - 1
    return (x & (x + 1)) == 0

def find_transform(x):
    operations = []
    count = 0
    while not is_perfect_longcat(x) and count < 40:
        if count % 2 == 0:
            # Operation A
            n = 0
            while (1 << n) - 1 <= x:
                n += 1
            # Find the highest bit position with 0
            while n > 0 and ((x >> (n - 1)) & 1) == 1:
                n -= 1
            if n == 0:
                break
            operations.append(n)
            x ^= (1 << n) - 1
        else:
            # Operation B
            x += 1
        count += 1
    
    return count, operations

# Read input
x = int(input())

t, ops = find_transform(x)

print(t)
for i in range(0, len(ops), 2):
    print(ops[i], end=' ')
