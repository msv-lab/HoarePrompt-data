#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^7) for each test case.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: The loop has completed all iterations, and `t` is now 0. The list `A` and the variable `n` are not preserved between iterations, so their final values are undefined. The initial state of the input parameters remains unchanged, but the loop has processed each test case by sorting the list of integers and printing the sum of the elements at even indices.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 5000) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 50) and a list of 2n integers (1 ≤ a_i ≤ 10^7). The function sorts the list of integers and prints the sum of the elements at even indices. After processing all test cases, the function does not return any value, and the state of the input parameters remains unchanged. The final state of the program is that `t` is 0, and the list `A` and the variable `n` are not preserved between iterations, so their final values are undefined.

