#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is an integer where 0 ≤ `t` ≤ 4997, `n` is an input integer, `A` is a sorted list of integers obtained from the input split and mapped to integers.
    #
    #Explanation: After the loop has executed all its iterations (i.e., `t` becomes 0), `t` will be 0, meaning the loop condition `t` is no longer satisfied, and thus the loop terminates. At this point, `n` and `A` will retain their last values from the final iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n`, followed by `2n` integers representing numbers on a whiteboard. It then sorts these integers and prints the sum of every second element in the sorted list (starting from the first element). After processing all test cases, the function outputs the results for each case.

