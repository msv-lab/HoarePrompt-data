#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: The output state will be a series of sums of every second element from each list `A`, sorted in ascending order, printed for each iteration of the loop.
    #
    #Explanation: For each value of `t`, the code reads an integer `n` and a list `A` of `n` integers. It then sorts the list `A` in ascending order and prints the sum of every second element starting from the first element. This process repeats until `t` becomes zero. Since `t` starts as an integer between 1 and 5000, the loop will execute that many times, each time processing a new list `A`. The final output state consists of the sums of every second element from each processed list, printed in the order they were processed.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) and a list of \( 2n \) integers. For each test case, it sorts the list in ascending order and calculates the sum of every second element starting from the first element. The function outputs these sums for each test case, one per line.

