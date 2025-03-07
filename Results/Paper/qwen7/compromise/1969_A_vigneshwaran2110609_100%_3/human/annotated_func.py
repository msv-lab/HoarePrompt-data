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
        
    #State: i is 50, x is 50, n is within the range [2, 50], flag is True, and l is a list of integers entered by the user.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer n (2 ≤ n ≤ 50), followed by a list of n integers p (1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct). For each test case, it reads an additional integer x (0 ≤ x ≤ n) and checks if the condition l[l[i] - 1] == i + 1 holds for any i in the range 0 to x-1, where l is the list of integers. If the condition is met for any i, it prints 2; otherwise, it prints 3. The function does not return anything but prints the result for each test case.

