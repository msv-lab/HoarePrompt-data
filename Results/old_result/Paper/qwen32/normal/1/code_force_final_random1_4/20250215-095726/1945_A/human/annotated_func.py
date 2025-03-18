#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The loop has processed all `t` test cases, where for each test case defined by the triple (a, b, c), it calculates `b` as `b + c` and then prints either `(a + (b // 3))` if `c` is not less than `b % 3`, or `-1` if `c` is less than `b % 3`. The state of `t` remains unchanged, and no further processing occurs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates `b + c` and then prints either `(a + (b // 3))` if `c` is not less than `b % 3`, or `-1` if `c` is less than `b % 3`.

