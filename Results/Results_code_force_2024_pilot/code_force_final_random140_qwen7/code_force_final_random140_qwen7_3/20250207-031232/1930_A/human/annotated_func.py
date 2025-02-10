#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is 0, `n` is an input integer, `A` is a list of integers obtained from the input string split and converted to integers.
    #
    #Explanation: After the loop executes all its iterations, `t` will be reduced by 1 for each iteration until it reaches 0. Since the loop runs 3 times initially and each run decreases `t` by 1, after all iterations, `t` will be 0. The values of `n` and the list `A` will be as they were set during the last iteration of the loop, but since no further iterations occur, these values remain unchanged from their last state.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `2n` integers `a_1, a_2, ..., a_{2n}`. It then calculates and prints the sum of every other element in the list starting from the first element (i.e., `a_1 + a_3 + ...`). After processing all `t` test cases, the function ends with `t` being 0, and `n` and the list `A` retaining their values from the last test case.

