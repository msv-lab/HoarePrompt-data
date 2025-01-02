f = None
try:
    f = open('q1.input', 'r')
except IOError:
    f = sys.stdin
if 'xrange' in dir(__builtins__):
    range = xrange

def func_1(case_num, iterable):
    print('Case #{}: {}'.format(case_num, ' '.join(map(str, iterable))))

def func_2(case_num, iterable):
    print('Case #{}: {}'.format(case_num, iterable))

def func_3(A):
    print(' '.join(A))

def func_4():
    return int(f.readline().strip())

def func_5():
    return [int(x) for x in f.readline().strip().split(' ')]

def func_6():
    a = [x for x in f.readline().split(' ')]
    return (int(a[0]), a[1].strip())

def func_7():
    return list(f.readline().strip())

def func_8(x):
    return bin(x)[2:]

def func_9(s, n, p, m):
    s = [0] + s
    dp = [[0 for _ in range(26)] for _ in range(n + 1)]
    p.sort()
    for i in range(1, n + 1):
        for j in range(26):
            dp[i][j] = dp[i - 1][j] + int(j == ord(s[i]) - ord('a'))
    res = [x for x in dp[n]]
    for i in range(m):
        x = p[i]
        for j in range(26):
            res[j] += dp[x][j]
    return ' '.join(map(str, res))

def func_10():
    T = func_4()
    for i in range(T):
        (n, m) = func_5()
        s = func_7()
        p = func_5()
        x = func_9(s, n, p, m)
        if 'xrange' not in dir(__builtins__):
            print(x)
        else:
            (print >> output, str(x))
    if 'xrange' in dir(__builtins__):
        print(output.getvalue())
        output.close()
if 'xrange' in dir(__builtins__):
    import cStringIO
    output = cStringIO.StringIO()
if __name__ == '__main__':
    func_10()
"stuff you should look for\n\t* int overflow, array bounds\n\t* special cases (n=1?)\n\t* do smth instead of nothing and stay organized\n\t* WRITE STUFF DOWN\n\t* BITS - THINK HOW TO MASK PROPERLY\n\t* PERMUTATIONS - PARITY AND CYCLES\n\t* Think simple, if it becomes over complicated, try to look at it from a different perspective.\n\t* Have fun!!!\n\t* TRY FIXING SOMETHING, and then maybe binary search around it.\n\t* Remember heaps. \n\t* Remember how to add a value to a segment when using prefix sum.\n\t\tsuppose you have an array[1,2,3,4,5] and you want to add 3 to array[1:4]. Then just \n\t\tadd 3 to A[1], and decrease 3 from A[4]. Let's look at what happens:\n\t\toriginal prefixsums is \t\t\t\t\t [1,3,6,10,15]\n\t\tarray -> [1,5,3,4,2] and prefix sums are [1,6,9,13,15] \n\t\tAs you see, exactly +3 in A[1:4]\n\t\t*** The previous method can help checking how many x,y you can choose to get s=x+y from two arrays.\n"
'\nbinary search \n\twhile(r - l > 1) {\n\t\tll mid = l + (r - l) / 2;\n\t\tsolve(mid);\n\t\tll sum = 0;\n\t\tfor (int i = 0; i < n; i++)\n\t\t\tsum += b[i];\n\t\tif (sum <= k)\n\t\t\tr = mid;\n\t\telse\n\t\t\tl = mid;\n\t}\n'