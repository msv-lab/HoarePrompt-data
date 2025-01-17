#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n such that 1 ≤ a_i ≤ 10^6.
def func():
    n_tests = int(input())
    for i in range(n_tests):
        n = int(input())
        
        x = [int(i) for i in input().split()]
        
        counter = x[0]
        
        for i in range(1, len(x)):
            if x[i] == 1:
                counter += 1
            elif counter > x[i]:
                counter = x[i] * ceil(counter / x[i])
            elif counter < x[i]:
                counter = x[i]
            else:
                counter = x[i] * 2
        
        print(counter)
        
    #State of the program after the  for loop has been executed: `counter` is the final value computed by the loop for each test case, `i` is the last index of the list `x`, `n_tests` is the number of test cases, and `x[i]` is the last element of the list `x`.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it accepts an integer `n` and a list of `n` integers `a_1, a_2, a_3, …, a_n` such that `1 ≤ t ≤ 1000`, `1 ≤ n ≤ 100`, and `1 ≤ a_i ≤ 10^6`. For each test case, it computes a final value `counter` based on the following rules:
1. Initialize `counter` to `x[0]`.
2. Iterate through the rest of the elements in the list `x`.
3. If `x[i]` is 1, increment `counter` by 1.
4. If `counter` is greater than `x[i]`, set `counter` to `x[i] * ceil(counter / x[i])`.
5. If `counter` is less than `x[i]`, set `counter` to `x[i]`.
6. If `counter` equals `x[i]`, set `counter` to `x[i] * 2`.

After processing all test cases, the function prints the final value of `counter` for each test case. The final state of the program after the function concludes is that it has processed all `t` test cases, and for each test case, it has printed the final value of `counter` computed according to the specified rules. The variable `counter` will hold the final value for the last test case, and `i` will be the index of the last element in the last list `x`. The variables `n_tests`, `n`, and `x` will no longer be used and can be considered local to the function.

