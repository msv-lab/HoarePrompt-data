#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10^5), representing the length of the array a. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9), representing the elements of the array a. The total number of elements across all test cases does not exceed 10^5.
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
        
    #State: `t` is the number of test cases, `n` is the input integer for each test case, `a` is the list of integers read from the input for each test case, and `max` is the maximum value of the minimums of consecutive pairs in the list `a` for each test case. The loop has executed `t` times, and the final output consists of `t` lines, each containing the `max` value for the corresponding test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the length of an array, followed by `n` integers representing the elements of the array. For each test case, it calculates the maximum value of the minimums of consecutive pairs in the array and prints this value.

