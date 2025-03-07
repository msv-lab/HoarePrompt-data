#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    if (n == 2) :
        print(2)
        #This is printed: 2
    else :
        for i in range(1, n + 1):
            if v[v[v[i]]] == i:
                print(2)
                return
            
        #State: v is a list of length n+1 where each element is 0, and no 2 printed.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an integer such that 2 ≤ n ≤ 50, `p` is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct, `v` is a list of length n+1 where each element is 0, and if `n` equals 2, then the first element of `v` is set to the input integer and no 2 is printed; otherwise, no changes are made to `v` and no 2 is printed.
#Overall this is what the function does:The function processes a predefined set of inputs (t, n, p) where t is an integer between 1 and 5000, n is an integer between 2 and 50, and p is a list of n distinct integers each between 1 and n, excluding the index i. It initializes a list v of length n+1 with all elements set to 0. If n equals 2, it sets the first element of v to the first input integer and prints 2. Otherwise, it iterates through the list v to check a specific condition. If the condition is met, it prints 2 and returns. If the condition is not met, it prints 3. The function does not return any value explicitly but prints either 2 or 3 based on the conditions checked.

