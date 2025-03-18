#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. The loop prints either 2 or 3 for each iteration based on the condition inside the loop. Since the loop does not modify any of the variables outside its scope (t, n, and p), their states remain unchanged. The output consists of a series of 2's or 3's printed during the loop executions, depending on whether the condition `l[l[i] - 1] == i + 1` was met for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer n (2 ≤ n ≤ 50) and a list p of n distinct integers (1 ≤ p_i ≤ n, p_i ≠ i). For each test case, it reads the list p and checks if p[p[i] - 1] equals i + 1 for any i in the range 0 to x-1, where x is another integer input. If the condition is met for any i, it prints 2; otherwise, it prints 3. The function does not return any value but outputs a series of 2's or 3's based on the condition check for each test case.

