#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of all n values across all test cases does not exceed 10^5.
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
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), each iteration of the loop processes a new list 'a' of integers, finds the maximum value among the minimum pairs of adjacent elements in 'a', and prints it. After all iterations, the final printed value is the last computed maximum value from the last list processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer t (1 ≤ t ≤ 500), an integer n (2 ≤ n ≤ 10^5), and an array a consisting of n positive integers (1 ≤ a_i ≤ 10^9). It then finds the maximum value among the minimum pairs of adjacent elements in the array a and prints this value. After processing all test cases, it outputs the final maximum value found.

