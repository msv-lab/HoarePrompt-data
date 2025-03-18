#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is 0, `n` is an input integer, `A` is a list of integers obtained from splitting the input string and converting each element to an integer.
    #
    #After the loop executes all its iterations, `t` will be reduced by 1 for each iteration until it reaches 0. Since the loop runs for the first 3 times and continues until `t` becomes 0, it means the loop will run a total of 4 times (including the first 3 times mentioned). Therefore, after all the executions of the loop, `t` will be 0. The values of `n` and the list `A` will be determined by the inputs provided during each iteration of the loop, but they will remain as they were set in the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n`, followed by `2n` integers stored in list `A`. It then calculates and prints the sum of every other element in `A`, starting with the first element. After processing all `t` test cases, the function sets `t` to 0.

