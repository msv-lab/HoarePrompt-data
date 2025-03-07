#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each integer p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The loop will execute as many times as there are test cases (as specified by the first input). For each test case, `i` will eventually reach `n` because the loop continues to increment `i` until it does so. The variable `j` will remain 1 if the condition `l[i] == i + 2 and l[i + 1] == i + 1` is met at any point during the loop's execution, otherwise it will remain 0. The list `l` will remain unchanged from its initial input state after each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list \( l \) of \( n \) integers. For each test case, it checks if there exists an index \( i \) such that \( l[i] = i + 2 \) and \( l[i + 1] = i + 1 \). If such an index is found, it prints 2 and stops further checks for that test case. If no such index is found after checking all possible indices, it prints 3. The function does not return any value but prints the result for each test case.

