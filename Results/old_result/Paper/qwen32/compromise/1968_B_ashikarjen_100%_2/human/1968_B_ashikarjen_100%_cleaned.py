def func_1():
    (n, m) = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        if j < m:
            k += 1
            j += 1
        else:
            break
    print(k)
    return
if __name__ == '__main__':
    for _ in range(int(input())):
        func_1()