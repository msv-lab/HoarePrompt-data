def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
    return 'NO'

def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = input().strip()
        b = input().strip()
        c = input().strip()
        results.append(func_1(n, a, b, c))
    for result in results:
        print(result)
if __name__ == '__main__':
    func_2()