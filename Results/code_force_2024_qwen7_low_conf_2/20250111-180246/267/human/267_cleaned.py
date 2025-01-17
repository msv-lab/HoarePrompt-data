def func_1(s):
    n = len(s)
    max_length = 0
    for d in range(1, n // 2 + 1):
        count = sum((1 for i in range(d) if func_2(s[i], s[i + d])))
        for l in range(n - 2 * d):
            if l > 0:
                count -= func_2(s[l - 1], s[l - 1 + d])
                count += func_2(s[l + d - 1], s[l + 2 * d - 1])
            if count == d:
                max_length = max(max_length, 2 * d)
    return max_length

def func_2(a, b):
    return a == b or a == '?' or b == '?'
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        result = func_1(s)
        print(result)