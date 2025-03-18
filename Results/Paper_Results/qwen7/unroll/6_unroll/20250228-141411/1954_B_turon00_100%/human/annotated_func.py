#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n, and the given array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: Output State: The output state will consist of a series of integers, each representing the minimum number of consecutive elements with the same value in the input array `a`, except when the length of the array `n` is 1 or all elements in the array are the same, in which case the output will be `-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \), a list of \( n \) integers \( a \), and an integer \( t \). For each test case, it calculates the minimum number of consecutive identical elements in the list \( a \). If the length of the list \( n \) is 1 or all elements in the list are the same, it outputs -1. Otherwise, it outputs the calculated minimum number of consecutive identical elements.

