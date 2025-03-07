#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9 for all i. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: After the loop executes all iterations, `i` will be equal to `n`, `max` will hold the greatest value among all pairs of consecutive elements in the list `a` from index 0 to `n-1`, and `n` will remain as it was initially. The variable `t` will be `t - 1`, indicating that one iteration of the outer loop has completed. The list `a` will be updated with integers inputted by the user, and `max` will contain the highest minimum value found between any two consecutive elements in the list `a` during the loop's iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` positive integers. For each test case, it finds and prints the maximum value among all pairs of consecutive elements in the array `a`. The function does not return a value but prints the result for each test case.

