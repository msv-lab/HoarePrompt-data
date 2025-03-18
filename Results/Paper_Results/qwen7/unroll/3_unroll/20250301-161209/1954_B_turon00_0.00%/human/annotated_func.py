#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: Output State: `t` test cases are processed, and for each test case, the minimum count of consecutive elements equal to the first element in the list `a` is printed. If all elements in the list `a` are the same, `-1` is printed instead.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, an integer n, and a list of n integers a. For each test case, it prints the minimum count of consecutive elements in the list a that are equal to the first element. If all elements in the list a are the same, it prints -1 instead.

