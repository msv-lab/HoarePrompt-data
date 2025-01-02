#State of the program right berfore the function call: n, k, a, and b are integers such that 1 ≤ k ≤ n ≤ 105, 0 ≤ a, b ≤ n, and a + b = n.
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
    #State of the program after the if block has been executed: *`n` is `vals[0]`, 1 ≤ k ≤ `vals[0]` ≤ 105, `a` is `vals[2]`, 0 ≤ `b` ≤ `vals[0]`, `k` is `vals[1]`, `b` is `vals[3]`, `c` is 0. If `b` > `a`, then `d` is `False`. Otherwise, `d` remains `True`.
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
        
    #State of the program after the  for loop has been executed: `n` is `vals[0]`, `k` is `vals[1]`, `a` is `vals[2] - (number of 'G' in s)`, `b` is `vals[3] - (number of 'B' in s)`, `c` is between 0 and `k-1`, `s` is a string of length `n` consisting of 'G' and 'B', `d` is the final state of the toggle, and if `a < 0 or b < 0`, the program has terminated with 'NO'.
    print(s)
#Overall this is what the function does:The function reads four integers `n`, `k`, `a`, and `b` from user input, where `1 ≤ k ≤ n ≤ 105`, `0 ≤ a, b ≤ n`, and `a + b = n`. It then constructs a string `s` of length `n` consisting of characters 'G' and 'B'. The function ensures that no more than `k` consecutive 'G' or 'B' characters appear in `s`. If at any point the construction of the string fails (i.e., `a` or `b` becomes negative), the function prints 'NO' and terminates. If the string is successfully constructed, it prints the string `s`. After the function concludes, the state is as follows: `n` is the original value read from input, `k` is the original value read from input, `a` is the original value minus the number of 'G' characters in `s`, `b` is the original value minus the number of 'B' characters in `s`, `c` is between 0 and `k-1`, and `s` is a string of length `n` consisting of 'G' and 'B' characters. If the function prints 'NO', it terminates early without further processing.

