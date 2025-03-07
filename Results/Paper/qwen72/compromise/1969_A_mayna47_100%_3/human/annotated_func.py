#State of the program right berfore the function call: n is an integer such that 2 <= n <= 50, and p is a list of integers of length n where 1 <= p[i] <= n, p[i] != i, and all elements in p are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop will not execute the print statement or return, so the values of `n`, `p`, and `v` remain unchanged.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `p` from the user. It checks if there exists any index `i` in the list `p` such that `p[p[i]] == i`. If such an index is found, the function prints `2` and returns immediately. If no such index is found, the function prints `3` and returns. The function does not return any value explicitly, but it affects the program state by printing either `2` or `3` based on the input.

