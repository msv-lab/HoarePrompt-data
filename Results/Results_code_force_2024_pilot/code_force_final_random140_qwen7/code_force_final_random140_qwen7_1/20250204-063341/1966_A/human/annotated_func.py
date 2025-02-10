#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. Additionally, a list of n integers c represents the numbers written on the cards, where 1 ≤ c_i ≤ 100 for each i.
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
        
    #State: The dictionary `h` contains the frequency of each integer from the original list `a`. The variable `ans` is set to `k - 1` if any integer in `a` appears at least `k` times; otherwise, `ans` is set to `n - 1`. The list `a` is empty, and the variables `_`, `n`, and `k` retain their initial values from the first iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers \( n \) and \( k \), and a list of \( n \) integers \( c \). It then counts the frequency of each integer in the list. If any integer appears at least \( k \) times, it sets the result to \( k - 1 \); otherwise, it sets the result to \( n - 1 \). Finally, it prints the result for each test case.

