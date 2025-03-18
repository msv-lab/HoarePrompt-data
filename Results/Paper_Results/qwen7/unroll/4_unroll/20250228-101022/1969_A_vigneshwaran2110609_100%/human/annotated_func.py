#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. The loop prints either 2 or 3 for each iteration based on the condition given, and the output state remains unchanged as the loop does not modify any of the variables outside its scope.
    #
    #In simpler terms, the loop processes inputs and prints either 2 or 3 for each iteration but does not change the values of `t`, `n`, or `p`. Therefore, the output state remains the same as the initial state.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`, a list `l` of `n` integers, and implicitly by `t` (which is not used within the function). For each test case, it reads `n` and `l`, then checks if any element `l[i]` in the list satisfies the condition `l[l[i] - 1] == i + 1`. If such an element is found, it prints `2` and breaks out of the loop. If no such element is found, it prints `3`. The function does not modify the input values and only prints `2` or `3` for each test case.

