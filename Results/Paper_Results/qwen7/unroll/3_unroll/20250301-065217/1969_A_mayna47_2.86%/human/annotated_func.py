#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
            
        #State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, p is a list of n integers such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct, v is a list of length n+1 where each element is 0 except the first element which is 0, and the loop has been executed but no condition `v[v[v[i]]] == i` was met for any i in the range 1 to n, so nothing was printed.
        print(3)
        #This is printed: 3
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an integer such that 2 ≤ n ≤ 50, `p` is a list of n integers such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct, `v` is a list of length n+1 where each element is 0 except the first element which is 0, and if `n == 2`, then `v` is a list of length 3 with the first element as 0 and the rest as integers converted from the input split. If `n != 2`, then the loop has been executed but no condition `v[v[v[i]]] == i` was met for any i in the range 1 to n, so nothing was printed.
#Overall this is what the function does:The function processes a test case defined by three values: `t` (an integer between 1 and 5000), `n` (an integer between 2 and 50), and `p` (a list of `n` distinct integers where each integer is between 1 and `n` and not equal to its index). Depending on the value of `n`, the function either prints `2` if a specific condition involving the list `v` is met, or prints `3` if no such condition is met. The function does not return any value but modifies a list `v` based on the input `p`.

