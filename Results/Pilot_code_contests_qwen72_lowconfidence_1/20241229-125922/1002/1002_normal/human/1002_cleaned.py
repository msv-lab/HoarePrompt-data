def func_1():
    n = map(int, sys.stdin.readline().strip('\n\r ').split())[0]
    s = map(int, list(sys.stdin.readline()[:2 * n]))
    sb = s[:n]
    se = s[n:]
    sb.sort()
    se.sort()
    lucky = 0
    unlucky = 0
    while sb:
        b = sb.pop()
        e = se.pop()
        if b > e:
            lucky += 1
        elif b < e:
            unlucky += 1
    if lucky == n or unlucky == n:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    print(func_1())