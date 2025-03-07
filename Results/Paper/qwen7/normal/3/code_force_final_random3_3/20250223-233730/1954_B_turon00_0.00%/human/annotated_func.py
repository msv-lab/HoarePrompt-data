#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the array is beautiful.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: After all iterations, `ans` holds the minimum value of `cnt` encountered during the loop execution for each iteration, `cnt` is 0, `i` is equal to `n`, `tmp` retains its initial value, and `a` remains as the list of integers provided initially.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( t \) (the number of test cases), followed by an integer \( n \) and an array \( a \) of \( n \) integers. It then checks if the array \( a \) is beautiful (i.e., all elements in the array are the same). If the array is beautiful, it prints -1. Otherwise, it finds the minimum count of consecutive identical elements in the array and prints this minimum count.

