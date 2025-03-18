#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is 0, `n` is an input integer, `A` is a sorted list of integers obtained from the input string split and converted to integers.
    #
    #After all iterations of the loop have finished, `t` will be reduced to 0 since it starts as a positive integer and decreases by 1 with each iteration until it reaches 0. The value of `n` and the list `A` will be determined by the inputs provided during the last iteration of the loop, but their specific values are not specified in the problem statement beyond being valid according to the given constraints.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `2n` integers `a_1, a_2, ..., a_{2n}`. It sorts the list of integers and calculates the sum of every second element starting from the first element (i.e., `a_1 + a_3 + ...`). The function prints this sum for each test case and continues until all test cases are processed. After processing all test cases, the variable `t` becomes 0, and the final state includes the last processed `n` and the corresponding sorted list `A`.

