#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The total number of test cases t is an integer (1 ≤ t ≤ 500), and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop will have processed all test cases, and for each test case, it will have printed the maximum value among the minimum pairs of consecutive elements in the array a. The variables `t`, `n`, and `a` will have been updated during each iteration of the loop, but their final values will be the values from the last test case processed. The variable `max` will hold the maximum value among the minimum pairs of consecutive elements for the last test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers. It then finds and prints the maximum value among the minimum pairs of consecutive elements in the array `a`. After processing all test cases, the function concludes, and the final state of the program includes the printed results for each test case. The internal variables `t`, `n`, `a`, and `max` will hold the values from the last test case processed.

