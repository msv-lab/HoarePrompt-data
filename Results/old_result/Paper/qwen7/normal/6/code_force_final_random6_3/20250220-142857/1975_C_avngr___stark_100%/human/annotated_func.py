#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of all n values across all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: Output State: After all iterations of the loop, `max` will hold the maximum value among the second smallest elements (temp[1]) of every possible consecutive triplet in the list `a`. The variable `t` will be 0 since all its iterations have been completed. The variable `n` will be less than or equal to 2 because the loop continues only when `n` is 2, and once `n` becomes greater than 2, `t` is set to 0 and the loop terminates. The variable `a` will remain as it was last input during the loop's final iteration. The variable `i` will be `-1` since it is decremented until it reaches -1. The variable `temp` will be an empty list since `i` has reached -1 and the loop condition `range(n - 2)` no longer holds true.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer t (number of cases), n (size of the array), and an array a of n positive integers. If n is 2, it prints the minimum element of the array. Otherwise, it finds and prints the maximum value among the second smallest elements of every possible consecutive triplet in the array a. After processing all test cases, it outputs the results for each case.

