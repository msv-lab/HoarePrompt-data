n, t = map(int, input().split())

def countNumbers(n, t):
    count = 0
    
    for m in range(n):
        row_sum = 0
        for i in range(m+2):
            row_sum ^= i
        if row_sum == t:
            count += 1
    
    return count

result = countNumbers(n, t)
print(result)