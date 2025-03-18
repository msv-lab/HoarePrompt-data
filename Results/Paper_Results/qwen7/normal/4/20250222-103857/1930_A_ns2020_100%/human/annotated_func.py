#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers a_1, a_2, ..., a_{2n} are integers such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: Output State: `t` is 0, `n` is an input integer, `A` is a sorted list of integers obtained from the input split and converted to integers.
    #
    #Explanation: After the loop has executed all its iterations, `t` will be reduced to 0 because the loop condition `while t:` checks if `t` is non-zero. Once `t` reaches 0, the loop terminates. The values of `n` and `A` will be as they were set in the last iteration of the loop, since these variables are defined inside the loop and are not affected by the loop's termination condition.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` indicating the number of cases, then an integer `n`, and a sequence of `2n` integers. It sorts the sequence of integers and calculates the sum of every second element starting from the first element. Finally, it prints this sum for each test case and reduces `t` until it reaches zero.

