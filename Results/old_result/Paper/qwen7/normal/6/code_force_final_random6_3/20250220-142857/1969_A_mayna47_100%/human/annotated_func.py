#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: i is 50, n is an input integer such that 2 ≤ n ≤ 50, and v[v[50]] is not equal to 50.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function reads two inputs: an integer `n` and a list of `n` integers `v`. It then checks if for any index `i` from 1 to `n`, the value at `v[v[i]]` equals `i`. If such an index is found, it prints `2` and exits. Otherwise, it prints `3`. The function does not return any value.

