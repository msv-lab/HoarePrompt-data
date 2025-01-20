n = int(input())
s = input()

def func_1(n, s):
    min_operations = n
    for i in range(1, n):
        if s[:i] == s[i:2 * i]:
            operations = i + 1 + (n - 2 * i)
            min_operations = min(min_operations, operations)
    return min_operations
result = func_1(n, s)
print(result)