#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: t is an integer between 1 and 500 (inclusive). For each input, n and a list of integers, the maximum value of the minimum of consecutive elements in the list is printed. The final state of t remains unchanged, but the value of t can vary based on user input during each iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer n followed by n integers. It calculates and prints the maximum value among the minimums of all consecutive pairs of integers in the list for each test case. The function does not return any value but prints the result for each test case.

