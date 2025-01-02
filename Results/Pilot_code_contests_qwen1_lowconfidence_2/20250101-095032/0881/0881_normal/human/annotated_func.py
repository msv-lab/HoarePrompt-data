#State of the program right berfore the function call: n, k, a, and b are integers such that 1 ≤ k ≤ n ≤ 10^5, 0 ≤ a, b ≤ n, and a + b = n.
def func():
    vals = [int(x) for x in raw_input().split()]
    n = vals[0]
    k = vals[1]
    a = vals[2]
    b = vals[3]
    c = 0
    d = True
    if (b > a) :
        d = False
    #State of the program after the if block has been executed: *`n` is `vals[0]`, `k` is `vals[1]`, `a` is `vals[2]`, `b` is `vals[3]`, `c` is 0, and `d` is `False`, provided that `b` is greater than `a`. There is no alternative outcome since there is no else part in the code.
    s = ''
    for i in range(n):
        if c == k:
            d = not d
            c = 0
        
        if d:
            s += 'G'
            a -= 1
            c += 1
            if a < b:
                d = not d
                c = 0
        else:
            s += 'B'
            b -= 1
            c += 1
            if b < a:
                d = not d
                c = 0
        
        if a < 0 or b < 0:
            print('NO')
            quit()
        
    #State of the program after the  for loop has been executed: - `n` is `vals[0]`.
    #- `k` is `vals[1]`.
    #- `a` is the final value of `a` after `n` iterations, which could be any non-negative integer depending on the decrement logic.
    #- `b` is the final value of `b` after `n` iterations, which could be any non-negative integer depending on the decrement logic.
    #- `c` is `n`.
    #- `d` is `True` if `b >= a` and `a` is even, `False` otherwise.
    #- `s` is a string consisting of 'G' and 'B' characters, with the exact sequence determined by the loop logic.
    #- The program prints 'NO' and exits if `a < 0` or `b < 0` during any iteration, otherwise it does not print anything.
    #
    #Thus, the output state is:
    print(s)
#Overall this is what the function does:The function `func()` accepts four integers `n`, `k`, `a`, and `b` (with constraints 1 ≤ k ≤ n ≤ 10^5, 0 ≤ a, b ≤ n, and a + b = n) and generates a string `s` consisting of 'G' and 'B' characters. It alternates between appending 'G' and 'B' based on the values of `a` and `b` and a toggle flag `d`. The function ensures that `a` and `b` do not become negative during the process. If either `a` or `b` becomes negative at any point, the function prints 'NO' and exits. After completing the loop, the function prints the generated string `s`.

Potential edge cases and missing functionality:
- The function correctly handles the case where `b` is initially greater than `a`, setting `d` to `False` and `c` to `0`.
- The function correctly toggles `d` and resets `c` when either `a` or `b` becomes less than the other.
- If `a` and `b` are both zero initially, the function will still work correctly, as it will simply print an empty string `s`.
- The function does not handle the case where `a` or `b` is zero and `k` is not zero; in such a scenario, the function will print 'NO' and exit because `c` will never reach `k`.
- The function does not account for the possibility that `k` might be larger than `a` or `b`, which would also result in `a` or `b` becoming negative before `c` reaches `k`, leading to the printing of 'NO' and exit.

