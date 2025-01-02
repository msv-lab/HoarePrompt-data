#State of the program right berfore the function call: a, b, and mod are integers such that 0 ≤ a, b ≤ 10^9 and 1 ≤ mod ≤ 10^7.
def func():
    a, b, m = map(int, raw_input().split())
    for i in range(1, min(a + 1, m + 1)):
        if (m - i * 10 ** 9 % m) % m > b:
            print(1, '%(x)09d' % {'x': i})
            sys.exit()
        
    #State of the program after the  for loop has been executed: `a`, `b`, and `m` are input integers, `mod` is an integer such that 1 ≤ `mod` ≤ 10^7. If the loop exits early, the condition `(m - i * 10
    print(2)
#Overall this is what the function does:The function reads three integers `a`, `b`, and `m` from the standard input. It then iterates over a range from 1 to the minimum of `a + 1` and `m + 1`. For each value `i` in this range, it checks if `(m - i * 10

