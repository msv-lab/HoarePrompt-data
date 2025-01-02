#State of the program right berfore the function call: The input sequence is a list of n integer numbers where 2 ≤ n ≤ 100 and each number a_i satisfies 1 ≤ a_i ≤ 3 ⋅ 10^{18}.
def func():
    MOD = 10 ** 9 + 7
    INF = float('+inf')
    if (sys.subversion[0] == 'PyPy') :
        sys.stdout = io.BytesIO()
        atexit.register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
        sys.stdin = io.BytesIO(sys.stdin.read())
        raw_input = lambda : sys.stdin.readline().rstrip()
    #State of the program after the if block has been executed: *`n` is a list of integers between 2 and 100 inclusive, each between 1 and \(3 \cdot 10^{18}\) inclusive; `MOD` is 10; `INF` is positive infinity; if the system subversion starts with 'P' followed by 'y', 'p', and 'y', `sys.stdout` is now `io.BytesIO()`, and the standard input is redirected to an in-memory bytes stream initialized with the existing standard input data; `raw_input` is a lambda function that reads a line from `sys.stdin` and strips any trailing whitespace. If the system subversion does not match this pattern, the state remains unchanged.
    pr = lambda *args: sys.stdout.write(' '.join(str(x) for x in args) + '\n')
    epr = lambda *args: sys.stderr.write(' '.join(str(x) for x in args) + '\n')
    die = lambda *args: pr(*args) ^ exit(0)
    read_str = raw_input
    read_strs = lambda : raw_input().split()
    read_int = lambda : int(raw_input())
    read_ints = lambda : map(int, raw_input().split())
    read_float = lambda : float(raw_input())
    read_floats = lambda : map(float, raw_input().split())
    """---------------------------------------------------------------"""
    n = read_int()
    arr = read_ints()
    res = [arr.pop()]
    arr = set(arr)
    while arr:
        a = res[0]
        
        if a % 2 == 0 and a / 2 in arr:
            arr.remove(a / 2)
            res = [a / 2] + res
            continue
        elif a * 3 in arr:
            arr.remove(a * 3)
            res = [a * 3] + res
            continue
        
        a = res[-1]
        
        if a % 3 == 0 and a / 3 in arr:
            arr.remove(a / 3)
            res = res + [a / 3]
            continue
        elif a * 2 in arr:
            arr.remove(a * 2)
            res = res + [a * 2]
            continue
        
    #State of the program after the loop has been executed: `arr` is an empty set, `res` contains the transformation history of the initial elements based on the given operations. Specifically, each element in `res` is either halved (if it is even and its half is in `arr`), tripled (if it is divisible by 3 and its third is in `arr`), or doubled (if its double is in `arr`). If none of these conditions are met, the original value remains in `res`.
    pr(*res)
#Overall this is what the function does:The function `func` accepts a list of integers as input and processes each integer according to specific rules. The function removes elements from the list based on whether they can be halved (if even), tripled (if divisible by 3), or doubled (if present in the list). It maintains a list `res` that records these transformations. After processing all elements, the function prints the contents of `res`. The function does not return any value but modifies and prints a list based on the input list.

