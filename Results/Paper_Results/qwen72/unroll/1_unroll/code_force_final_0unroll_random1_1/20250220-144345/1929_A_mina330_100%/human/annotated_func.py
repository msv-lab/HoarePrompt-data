#State of the program right berfore the function call: The function should accept two parameters: t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n (2 ≤ n ≤ 100) integers (1 ≤ a_i ≤ 10^9) representing the elements of the array a.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: The loop has completed all iterations, and for each test case, the difference between the maximum and minimum elements of the sorted list `a` has been printed. The variables `ntest`, `itest`, `n`, and `a` have been used and modified within the loop, but their final states are not directly relevant to the output. The initial state of `ntest` remains unchanged, and the list of lists provided as input has been processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It sorts the list and prints the difference between the maximum and minimum elements of the sorted list. The function does not return any value; it only prints the results for each test case. After the function concludes, the differences for all test cases have been printed, and the variables used in the function are no longer relevant.

