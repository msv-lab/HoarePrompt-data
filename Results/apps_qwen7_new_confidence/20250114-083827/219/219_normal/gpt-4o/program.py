n, p, q = map(int, input().split())
s = input()

def split_string(n, p, q, s):
    for i in range(n // p + 1):
        if (n - i * p) % q == 0:
            k = i + (n - i * p) // q
            print(k)
            for j in range(i):
                print(s[j * p: (j + 1) * p])
            for j in range((n - i * p) // q):
                print(s[i * p + j * q: i * p + (j + 1) * q])
            return
    print(-1)

split_string(n, p, q, s)
