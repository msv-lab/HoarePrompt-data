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
        
    #State: Output State: `t` integers representing the minimum length of segments with the same number in each input sequence. If no such segment exists (i.e., all numbers are unique), each integer will be -1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a \). It determines the minimum length of contiguous segments within the list \( a \) where all elements are identical. If no such segment exists, it outputs -1 for each test case. The function ultimately prints \( t \) integers, one for each test case, indicating the minimum segment length or -1 if no valid segment is found.

