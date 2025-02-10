#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is `0`, `n` is an input integer (the last value read from input), `A` is a list of integers obtained from splitting the input string and converting each element to an integer (the last list read from input).
    #
    #After the loop executes all its iterations, `t` will be reduced to `0` since it starts as an input integer and decreases by `1` in each iteration until it reaches `0`. The values of `n` and `A` will be the ones read from the input during the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` and an integer `n`, followed by `2n` integers stored on a whiteboard. It then calculates and prints the sum of every second integer starting from the first one in the list of `2n` integers. After processing all `t` test cases, it ensures that `t` is reduced to `0`, and retains the values of `n` and the list `A` from the last test case for potential use.

