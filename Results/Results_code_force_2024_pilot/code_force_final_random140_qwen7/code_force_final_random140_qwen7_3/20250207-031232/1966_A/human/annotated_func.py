#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. Additionally, a list of n integers representing the numbers on the cards is provided for each test case, where each integer is in the range 1 ≤ c_i ≤ 100.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: After all iterations, the variable `a` will be an empty list, `ans` will retain its initial value `n`, `h` will be a dictionary containing the count of each integer from the original list `a`, and `ams` will be `k - 1` if any integer in `a` appears `k` or more times in `h`; otherwise, `ams` will remain `None` (or its initial value, which is not specified but can be assumed to be `None` if not explicitly changed).
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( k \), and a list of \( n \) integers representing card values. It then counts the occurrences of each card value. If any card value appears \( k \) or more times, it decreases the initial count \( n \) by \( k-1 \). Finally, it prints the adjusted count \( n \) for each test case.

