#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: Output State: The value of `t` will be the input value for the last iteration of the loop, `n` will be the input integer for the last iteration, and `ar` will be a sorted list of integers entered by the user for the last iteration.
    #
    #This means that after all iterations of the loop have finished, `t` will hold the value of the final test case's `t`, `n` will hold the value of the final test case's `n`, and `ar` will be the sorted list of integers corresponding to the final test case's input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 500) and a list of `n` integers (2 ≤ n ≤ 100) where each integer `a_i` (1 ≤ a_i ≤ 10^9). For each test case, it sorts the list of integers, calculates the sum of differences between consecutive elements, and prints the result. After processing all test cases, the function does not return any value but prints the result for each test case.

