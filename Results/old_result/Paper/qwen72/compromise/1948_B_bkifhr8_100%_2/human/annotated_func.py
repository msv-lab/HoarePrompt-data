#State of the program right berfore the function call: The function `func` is expected to take input through standard input (stdin) and output through standard output (stdout). The input consists of multiple test cases, where the first line contains a single integer t (1 ≤ t ≤ 10^3) representing the number of test cases. Each test case consists of two lines: the first line contains a single integer n (2 ≤ n ≤ 50) representing the length of the array, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 99) representing the elements of the array.
def func():
    n = int(input())
    for _ in range(n):
        m = int(input())
        
        arr = [int(i) for i in input().split()]
        
        ans = True
        
        for i in range(m - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                nums = [int(i) for i in str(arr[i - 1])] + [arr[i]]
                if nums != sorted(nums):
                    ans = False
                    break
                arr[i - 1] = nums[0]
        
        print(['NO', 'YES'][ans])
        
    #State: The loop will execute for each test case, and for each test case, it will read an integer `m` and an array `arr` of length `m`. It will then determine if the array can be sorted by repeatedly moving the last element to the front if it is smaller than the element before it. If the array can be sorted this way, it will print 'YES'; otherwise, it will print 'NO'. After all test cases are processed, the variables `t`, `n`, and `arr` will no longer be in the same state as the initial state, but the overall function will have completed its execution and printed the results for all test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case includes an integer `n` and an array of `n` integers. For each test case, it determines if the array can be sorted by repeatedly moving the last element to the front if it is smaller than the element before it. If the array can be sorted this way, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes its execution and the results for all test cases are printed to standard output.

