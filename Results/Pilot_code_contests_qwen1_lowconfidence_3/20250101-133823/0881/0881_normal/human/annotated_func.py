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
    #State of the program after the if block has been executed: *`n` is an integer such that \(1 \leq k \leq n \leq 10^5\); `k` is the second element of `vals`; `a` is equal to `vals[2]`; `b` is the fourth element of `vals`; `vals` is a list of integers equal to the input split and converted to integers; `c` is 0; `d` is `False` if `b > a`, otherwise `d` remains `True`.
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
        
    #State of the program after the  for loop has been executed: `k` is the second element of `vals`, `n` is greater than or equal to `k`, `c` is 0, `d` retains its final value after all iterations, `s` is the sequence of 'G' and 'B' characters resulting from the loop's conditions, and `a` and `b` are both 0. If `a < 0` or `b < 0` at any point during the loop, the console prints 'NO' and the loop terminates early.
    print(s)
#Overall this is what the function does:The function processes the values of `n`, `k`, `a`, and `b` according to specific constraints and generates a string `s` consisting of 'G' and 'B' characters. The string `s` is constructed based on the values of `a` and `b` within a loop that runs `n` times. If at any point during the loop, `a` or `b` becomes negative, the function immediately prints 'NO' and exits. After completing the loop, the function prints the generated string `s`. If no negative values occur, `s` will consist of exactly `k` 'G' characters and the rest will be 'B' characters, with the pattern alternating between 'G' and 'B' based on the values of `a` and `b`. The function handles the case where `b > a` by setting `d` to `False` initially, ensuring the pattern alternates correctly.

