#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5, and for each test case, a valid string s exists that corresponds to the given trace.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The loop has completed all iterations, `t` is 0, `n` is an input integer greater than 0, `s` is a list of integers that must have at least `n` integers, `r` is a string that has been concatenated with the values of `a[x]` for each integer `i` in `s`, where `x` is the index of `i` in `b`. Each element in `b` that corresponds to an integer in `s` has been incremented by the number of times that integer appears in `s` for each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then constructs a string `r` by mapping each integer in `s` to a character in the alphabet string `a` based on the count of occurrences in `b`. The function prints the constructed string `r` for each test case. After all test cases are processed, the function completes, and the final state is that `t` is 0, `n` and `s` are the last values read for the final test case, and `r` is the last string printed. The list `b` contains the cumulative counts of the integers in `s` across all test cases.

