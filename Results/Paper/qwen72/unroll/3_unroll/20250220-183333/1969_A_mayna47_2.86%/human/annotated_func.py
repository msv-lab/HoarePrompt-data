#State of the program right berfore the function call: The function should accept two parameters: an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list of integers p of length n (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend. The function should be called multiple times with different values of n and p, as specified by an integer t (1 ≤ t ≤ 5000) representing the number of test cases.
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
            
        #State: The function either prints 2 and returns immediately, or it completes the loop without printing anything. The values of `n`, `p`, and `v` remain unchanged.
        print(3)
        #This is printed: 3
    #State: If `n` is 2, the function accepts two parameters: an integer `n` (2 ≤ n ≤ 50) representing the number of friends, and a list of integers `p` of length `n` (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend. The function is called multiple times with different values of `n` and `p`, as specified by an integer `t` (1 ≤ t ≤ 5000) representing the number of test cases. `n` is an input integer and has a current value of 2. `v` is a list of length `n + 1` initialized with the first element as 0 and the remaining elements as integers provided by the input. If `n` is not 2, the function either prints 2 and returns immediately, or it completes the loop without printing anything. The values of `n`, `p`, and `v` remain unchanged.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `p` from the input. It then checks if the best friend relationships represented by `p` form a valid cycle of length 3. If `n` is 2, it prints 2 and returns. If `n` is greater than 2 and a valid cycle of length 3 is found, it prints 2 and returns. If no valid cycle of length 3 is found, it prints 3 and returns. The function does not modify the input values `n` and `p`.

