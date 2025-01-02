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
    #State of the program after the if block has been executed: *`n` is the first element of `vals`, `k` is the second element of `vals`, `a` is the third element of `vals`, `b` is the fourth element of `vals`, `c` is 0, `d` is `False`. If `b` is greater than `a`, then `d` is set to `False`. There is no change in the values of `n`, `k`, `a`, `b`, and `c`.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is either 0 or the second element of `vals`, `a` and `b` are non-negative integers, `c` is 0, `d` is `False`, and `s` is a string consisting of only 'G' and 'B' characters, where the number of 'G' characters is equal to the number of 'B' characters. If `a < 0` or `b < 0` at any point during the loop execution, the program prints 'NO' and quits.
    print(s)
#Overall this is what the function does:The function processes two integers `a` and `b` under the constraints 1 ≤ k ≤ n ≤ 10^5, 0 ≤ a, b ≤ n, and a + b = n. It constructs a string `s` consisting of 'G' and 'B' characters based on the following rules: the string length is `n`, every `k`-th character is toggled between 'G' and 'B', and the toggle continues until `a` and `b` become unequal, at which point the toggle direction is reversed. The function ensures that `a` and `b` remain non-negative throughout the process. If `a` or `b` becomes negative at any point, the function prints 'NO' and terminates. If the process completes without violating the constraints, the function prints the constructed string `s`.

