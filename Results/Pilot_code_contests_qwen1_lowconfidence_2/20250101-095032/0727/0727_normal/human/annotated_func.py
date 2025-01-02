#State of the program right berfore the function call: The input is a list of n integer numbers (2 ≤ n ≤ 100) where each number is in the range 1 to 3 ⋅ 10^{18}, and these numbers can be rearranged such that each number is either exactly two times the previous number or exactly one third of the previous number.
def func():
    MOD = 10 ** 9 + 7
    INF = float('+inf')
    if (sys.subversion[0] == 'PyPy') :
        sys.stdout = io.BytesIO()
        atexit.register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
        sys.stdin = io.BytesIO(sys.stdin.read())
        raw_input = lambda : sys.stdin.readline().rstrip()
    #State of the program after the if block has been executed: *The input is a list of n integer numbers (2 ≤ n ≤ 100) where each number is in the range 1 to 3 ⋅ 10^{18}, and these numbers can be rearranged such that each number is either exactly two times the previous number or exactly one third of the previous number; `MOD` is 10; `INF` is set to positive infinity. Additionally, if `sys.subversion[0]` equals 'PyPy', then `sys.stdin` is an in-memory bytes buffer containing the original input data, `sys.stdout` is set to an in-memory bytes buffer, and `raw_input` is a lambda function that reads a line from `sys.stdin` and strips the trailing newline character. Otherwise, the state of `sys.stdin`, `sys.stdout`, and `raw_input` remains unchanged.
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
        
    #State of the program after the loop has been executed: `arr` is empty, `res` contains the sequence of operations applied to the initial elements of `arr` until no further operations can be performed, `a` is the last element of `res`, `sys.stdout` is an in-memory bytes buffer, `MOD` is 10, `INF` is positive infinity, `read_strs` is a lambda function that takes input using `raw_input()` and splits it into a list of strings, `read_int` is a lambda function that reads an integer from input using `int(raw_input())`, `read_ints` is a lambda function that reads a list of integers from input using `map(int, raw_input().split())`, `read_float` is a lambda function that reads a float from input using `float(raw_input())`, `read_floats` is a lambda function that maps `float` to each element of the list split from the input using `raw_input().split()`
    pr(*res)
#Overall this is what the function does:The function `func` accepts a list of `n` integer numbers where `2 ≤ n ≤ 100` and each number is in the range 1 to \(3 \cdot 10^{18}\). It rearranges the numbers such that each number is either exactly two times the previous number or exactly one third of the previous number. The function constructs a sequence of operations that can transform the initial elements of the list into a valid sequence according to the specified rules. After executing the operations, the function prints the resulting sequence and returns nothing. If no valid sequence can be constructed, the function still prints the initial sequence provided.

