#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each integer p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, p is a list of n integers where each integer p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. After executing the loop, the output consists of either "2" printed for each iteration where the condition `l[l[i] - 1] == l[i] - 1` is met, or "3" printed for each iteration where the condition is not met.
    #
    #In natural language: The output state remains the same as the initial state, but with the addition of printed outputs from the loop. For each iteration of the loop, if the condition `l[l[i] - 1] == l[i] - 1` is true, the number 2 is printed; otherwise, the number 3 is printed. The values of `t`, `n`, and the list `p` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 50), followed by a list of `n` integers `p` (1 ≤ `p_i` ≤ `n`, `p_i` ≠ `i`, and all `p_i` are distinct). It then checks for each element `p_i` in the list whether `p[p_i - 1]` equals `p_i - 1`. If this condition is met for any element, it prints "2"; otherwise, it prints "3". The function does not return any value but produces output based on the condition checks. The final state includes the printed outputs for each test case.

