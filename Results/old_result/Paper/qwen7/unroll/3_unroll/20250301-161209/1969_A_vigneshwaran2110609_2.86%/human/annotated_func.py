#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. After the loop executes all the iterations, the output consists of either "2" or "3" printed for each iteration based on the condition inside the inner loop. If for any iteration, the condition `l[l[i] - 1] == l[i] - 1` is met, "2" is printed; otherwise, "3" is printed for that iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `n` (2 ≤ n ≤ 50), and a list `p` of `n` integers (1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct). For each test case, it reads an additional integer `x`, then checks if any element `l[i]` in a list of length `x` satisfies the condition `l[l[i] - 1] == l[i] - 1`. If such an element exists, it prints "2"; otherwise, it prints "3". The function does not return any value but outputs either "2" or "3" for each test case based on the specified condition.

