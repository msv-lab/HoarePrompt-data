def generate_string(n, k):
    base = ''.join(chr(ord('a') + i) for i in range(k))
   
    result = (base * (n // k + 1))[:k + (n - 1)]
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(generate_string(n, k))
