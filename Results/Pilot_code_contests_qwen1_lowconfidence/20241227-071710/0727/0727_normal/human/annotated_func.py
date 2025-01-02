#State of the program right berfore the function call: The input is a list of n integer numbers (2 ≤ n ≤ 100) where each number is within the range 1 ≤ a_i ≤ 3 ⋅ 10^{18}. The sequence can be rearranged such that each number is either twice the previous number or one third of the previous number in the sequence.
def func():
    MOD = 10 ** 9 + 7
    INF = float('+inf')
    if (sys.subversion[0] == 'PyPy') :
        sys.stdout = io.BytesIO()
        atexit.register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
        sys.stdin = io.BytesIO(sys.stdin.read())
        raw_input = lambda : sys.stdin.readline().rstrip()
    #State of the program after the if block has been executed: *The input is a list of n integer numbers (2 ≤ n ≤ 100) where each number is within the range 1 ≤ a_i ≤ 3 ⋅ 10^{18}. The sequence can be rearranged such that each number is either twice the previous number or one third of the previous number in the sequence. INF is float('+inf'). The Python implementation is PyPy (indicated by sys.subversion[0] == 'PyPy'); sys.stdout is set to io.BytesIO() for handling output in memory. `raw_input` is now a lambda function that reads from `sys.stdin`. These conditions hold regardless of whether the if condition is true or false.
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
        
    #State of the program after the loop has been executed: `n` is an integer value obtained from user input, `arr` is an empty set, `res` contains the original elements of `arr` plus the last element of `arr` repeated until no further valid operations can be performed according to the rules inside the loop.
    pr(*res)
#Overall this is what the function does:The function `func` accepts a list of `n` integer numbers where `2 ≤ n ≤ 100` and each number is within the range `1 ≤ a_i ≤ 3 ⋅ 10^{18}`. The sequence can be rearranged such that each number is either twice the previous number or one third of the previous number in the sequence. After executing the function, the program state will be as follows:

1. The variable `n` holds the integer value of the length of the input list.
2. The variable `arr` is an empty set.
3. The variable `res` contains the original elements of the input list `arr` plus the last element of `arr` repeated until no further valid operations can be performed according to the rules inside the loop.
4. If no further valid operations can be performed, the program will print the elements in `res` using the `pr` function.
5. The program does not return anything explicitly; instead, it prints the result.

