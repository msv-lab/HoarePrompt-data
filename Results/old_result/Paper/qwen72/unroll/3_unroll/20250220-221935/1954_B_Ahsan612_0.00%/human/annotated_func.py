#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of the array, and an array a of n integers (1 ≤ a_i ≤ n) that is guaranteed to be beautiful. The total number of test cases t (1 ≤ t ≤ 10^4) is provided, and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: The loop iterates through each test case, processes the array, and prints the minimum length of consecutive elements that are the same for each test case. The variables `t`, `n`, and `ar` are reset for each test case, and the loop continues until all test cases are processed. The final state of the loop is that all test cases have been processed, and the output for each test case has been printed.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n` and an array `a` of `n` integers. For each test case, it finds the minimum length of consecutive elements that are the same in the array and prints this value. If no such consecutive elements exist, it prints `-1`. After processing all test cases, the function concludes with all test cases having been processed and their respective results printed.

