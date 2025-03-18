#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. The loop prints either "2" or "3" for each iteration based on the condition provided, but the final state of t and p remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list `p` of `n` integers. For each test case, it reads `n` and a list `l` of integers. It then checks if any element in `l` satisfies a specific condition: `l[l[i] - 1] == i + 1`. If such an element is found, it prints "2". Otherwise, it prints "3". The function does not modify the input variables `t`, `n`, or `p` and only outputs "2" or "3" for each test case.

