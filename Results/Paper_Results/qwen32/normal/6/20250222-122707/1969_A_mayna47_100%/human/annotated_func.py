#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: t is an integer such that 1 <= t <= 5000; n is the integer value from the input (where 2 <= n <= 50); p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n and p_i != i; v is a list of n + 1 integers where the first element is 0 and the remaining n elements are the integers read from the input; i is n + 1.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` distinct integers from the input. It checks if there exists an integer `i` such that the value at index `v[i]` in the list is `i`. If such an integer is found, it prints `2` and terminates. If no such integer is found after checking all possibilities, it prints `3`. The function does not return any value.

