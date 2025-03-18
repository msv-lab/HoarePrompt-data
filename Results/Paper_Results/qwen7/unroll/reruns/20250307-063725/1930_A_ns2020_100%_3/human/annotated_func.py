#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: The output state will consist of the sum of every second smallest number from each input list, printed for each iteration of the loop.
    #
    #Explanation: The loop runs `t` times, where `t` is initially an integer input. In each iteration, it reads an integer `n` and then a list `A` of `n` integers. It sorts the list `A` and prints the sum of every second element starting from the first element (i.e., `A[0] + A[2] + ...`). After printing, `t` is decremented by 1. Therefore, the final output state will be a series of sums, one for each iteration of the loop, representing the sum of every second smallest number from each input list.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and `2n` integers. For each test case, it sorts the list of integers and calculates the sum of every second smallest number, starting from the smallest. This sum is then printed for each test case. After processing all test cases, the function concludes, leaving the output consisting of these sums.

