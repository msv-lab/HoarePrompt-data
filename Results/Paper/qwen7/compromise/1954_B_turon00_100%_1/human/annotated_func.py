#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: All iterations of the loop have completed. t is 0, and no further inputs will be processed. The variable `ans` holds the final result for each input list `a` that was processed, which is the minimum value of `cnt` encountered during the loop's execution for each input. If the input list `a` had only one element or if the minimum count of consecutive identical elements was equal to the length of the list, then `ans` will be -1 for that specific input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \), an integer \( n \), and an array \( a \) of \( n \) integers. For each test case, it calculates the minimum number of consecutive identical elements in the array \( a \). If the array \( a \) has only one element or the minimum count of consecutive identical elements equals the length of the array, the function prints -1. Otherwise, it prints the calculated minimum count. After processing all test cases, the function ends with \( t \) set to 0 and no further inputs to process, and the variable `ans` holding the result for each test case.

