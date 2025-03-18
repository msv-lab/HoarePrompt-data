#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
            
        #State: Output State: `i` is 4, `n` is between 3 and 50 inclusive, and `v[v[v[i]]]` is not equal to `i`.
        #
        #Explanation: The loop continues to iterate from `i = 1` to `i = n`. After three iterations, `i` has been incremented to 4. For each iteration, the loop checks if `v[v[v[i]]] == i`. If this condition is not met, `i` is incremented and the check continues. Since the condition was not met in the first three iterations, it will continue to be checked with `i` now being 4. The values of `n` and the condition `v[v[v[i]]] != i` remain unchanged as no modifications were made to these variables within the loop.
        print(3)
        #This is printed: 3
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an integer between 2 and 50 inclusive, `p` is a list of `n` integers where each `p_i` satisfies 1 ≤ `p_i` ≤ `n` and `p_i` ≠ `i`, and all `p_i` are distinct; `v` is a list of length `n+1` where the first element is 0 and the next `n` elements are integers inputted from the user. If `n` equals 2, then `n` is 2 and `v` is a list of length 3 with the first element as 0 and the next two elements as integers inputted from the user. If `n` is between 3 and 50, `i` is 4, and the condition `v[v[v[4]]]` is not equal to 4.
#Overall this is what the function does:The function reads an integer `n` and a list `p` of `n` integers from the user. It then checks if `n` is 2, in which case it prints 2. If `n` is not 2, it iterates through the list and checks if `v[v[v[i]]] == i` for any `i`. If this condition is found to be false, it prints 3. The function does not return any value.

