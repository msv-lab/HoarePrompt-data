#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
            
        #State: The value printed is either 2 or nothing, depending on whether the condition `v[v[v[i]]] == i` is met for any `i` in the range 1 to `n`. If the condition is met for at least one `i`, then 2 is printed; otherwise, nothing is printed.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is 2, `p` is a list of 2 integers where each `p_i` is an integer such that 1 ≤ `p_i` ≤ 2, `p_i` ≠ `i`, and all `p_i` are distinct; `v` is a list of length 3 where each element is an integer read from input and the first element is 0. If `n` is 2, then `t` remains unchanged. If `n` is not 2, the value printed is either 2 or nothing, depending on whether the condition `v[v[v[i]]] == i` is met for any `i` in the range 1 to `n`. If the condition is met for at least one `i`, then 2 is printed; otherwise, nothing is printed.
#Overall this is what the function does:The function processes predefined inputs \( t \), \( n \), and \( p \) where \( t \) is an integer between 1 and 5000, \( n \) is an integer between 2 and 50, and \( p \) is a list of \( n \) integers. It initializes a list \( v \) based on the input and checks if a specific condition is met. Depending on the outcome, it prints either 2 or 3 and returns nothing. If \( n \) is 2, it always prints 2. Otherwise, it iterates through the list \( v \) and checks if \( v[v[v[i]]] == i \) for any \( i \) in the range 1 to \( n \). If the condition is met for any \( i \), it prints 2; otherwise, it prints 3.

