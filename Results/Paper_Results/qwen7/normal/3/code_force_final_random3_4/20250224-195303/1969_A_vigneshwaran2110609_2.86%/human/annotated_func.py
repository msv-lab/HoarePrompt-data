#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: i is 49, x is 50, n is the same as before, l remains unchanged, flag is True if any element l[j] satisfies l[l[j] - 1] == l[j] - 1 for j in range(x), otherwise flag remains True (since it was initially True and not changed).
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` integers. For each test case, it checks if `n` is between 2 and 50, and if all elements in `p` are distinct integers between 1 and `n`, not equal to their index. If any element `l[j]` in the list satisfies `l[l[j] - 1] == l[j] - 1`, it prints 2. Otherwise, it prints 3. The function does not return any value but prints the result for each test case.

