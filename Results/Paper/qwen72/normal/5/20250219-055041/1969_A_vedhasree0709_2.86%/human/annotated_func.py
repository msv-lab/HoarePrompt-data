#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, representing the number of test cases. Each test case consists of n, an integer such that 2 <= n <= 50, representing the number of friends, and a list p of n integers where 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct, representing the best friends of each friend.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: `t` is an integer such that 1 <= t <= 5000, `_` is `t`, `i` is `n`, `l` is a list of integers provided by the user. If any element `l[k]` is `k + 2` and the next element `l[k + 1]` is `k + 1` for any `k` in the range 0 to `n-2`, then `j` is 1 and the program has printed 2 for that test case. Otherwise, `j` remains 0, and the program has printed 3 for that test case.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer `n` and a list `l` of `n` integers. The function checks if there exists any index `k` in the list `l` such that `l[k] == k + 2` and `l[k + 1] == k + 1`. If such an index is found, the function prints `2` for that test case. If no such index is found, the function prints `3` for that test case. After processing all test cases, the function has printed either `2` or `3` for each test case, depending on the conditions met within the list `l`.

