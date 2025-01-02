def func_1():
    n = stdin.readline()
    res = ''
    for x in range(int(n)):
        (a, b, n, S) = [int(x) for x in stdin.readline().split()]
        prod = n * a
        if n * a < S:
            if S - prod <= b:
                res += 'YES\n'
            else:
                res += 'NO\n'
        elif S % n <= b:
            res += 'YES\n'
        else:
            res += 'NO\n'
    stdout.write(res)
if __name__ == '__main__':
    func_1()