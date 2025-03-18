#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: The variable `t` remains unchanged, and for each test case, the loop will print either `2` or `3` based on the condition `l[l[i] - 1] == i + 1`. The list `l` and the integer `x` are not modified by the loop.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads an integer `x` and a list `l` of `x` integers. The function then checks for each element in `l` if the element at the index specified by the current element minus one equals the current index plus one. If this condition is met for any element, the function prints `2` and breaks out of the loop. If the condition is never met, the function prints `3`. The function does not modify the input variables and does not return any value. The variable `t` is not used within the function, and the state of the program remains unchanged with respect to `t`.

