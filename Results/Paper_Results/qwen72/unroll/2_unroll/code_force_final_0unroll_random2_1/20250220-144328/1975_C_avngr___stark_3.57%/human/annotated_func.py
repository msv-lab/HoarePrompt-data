#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case includes an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and a list of n positive integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The total number of test cases t is an integer (1 ≤ t ≤ 500), and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum value of the minimum pairs of consecutive elements in the array a. The variables `t`, `n`, and `a` are modified during the execution of the loop, but their final state is not directly relevant to the output. The output is a series of integers, each corresponding to the result of one test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a list of `n` positive integers `a`. For each test case, the function computes and prints the maximum value among the minimum pairs of consecutive elements in the list `a`. The function does not return any value but outputs the results directly to the standard output. After processing all test cases, the function terminates, leaving the input variables `t`, `n`, and `a` in an undefined state.

