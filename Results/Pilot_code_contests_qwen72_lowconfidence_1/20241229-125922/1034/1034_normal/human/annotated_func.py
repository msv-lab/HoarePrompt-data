#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^4, and each of the q test cases contains four integers a, b, n, and S where 1 ≤ a, b, n, S ≤ 10^9.
def func_1():
    n = stdin.readline()
    res = ''
    for x in range(int(n)):
        a, b, n, S = [int(x) for x in stdin.readline().split()]
        
        prod = n * a
        
        if n * a < S:
            if S - prod <= b:
                res += 'YES\n'
            else:
                res += 'NO\n'
        elif S % n <= b:
            res += 'YES\n'
        else:
            res += 'NO\n'
        
    #State of the program after the  for loop has been executed: `q` is a positive integer such that 1 ≤ `q` ≤ 10^4, `res` is a string containing `q` lines, each line being either `'YES\n'` or `'NO\n'` based on the conditions evaluated for each of the `q` test cases. For each test case, `a`, `b`, `n`, and `S` are integers read from input, `prod` is calculated as `n * a`, and the conditions are: if `n * a < S` and `S - prod` ≤ `b`, or if `n * a ≥ S` and `S % n` ≤ `b`, then the line is `'YES\n'`; otherwise, the line is `'NO\n'`.
    stdout.write(res)
#Overall this is what the function does:The function `func_1` reads a number `n` from standard input, indicating the number of test cases. For each test case, it reads four integers `a`, `b`, `n`, and `S` from standard input. The function evaluates whether the sum of `n * a` and `b` is at least `S`. If `n * a` is less than `S`, it checks if the remaining value `S - (n * a)` is less than or equal to `b`. If `n * a` is greater than or equal to `S`, it checks if the remainder `S % n` is less than or equal to `b`. Based on these conditions, it appends either `'YES\n'` or `'NO\n'` to a result string. After processing all test cases, it writes the result string to standard output. The final state of the program is that `n` test cases have been processed, and the results are printed to standard output, with each line being either `'YES\n'` or `'NO\n'`.

