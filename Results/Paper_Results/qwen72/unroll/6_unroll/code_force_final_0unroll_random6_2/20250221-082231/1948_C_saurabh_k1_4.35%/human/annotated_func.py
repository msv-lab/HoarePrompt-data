#State of the program right berfore the function call: The function should take three parameters: t (1 ≤ t ≤ 10^4), a list of integers n (2 ≤ n ≤ 2·10^5 and n is even), and a list of two strings, each of length n, containing only the characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The loop iterates t times, and for each iteration, it reads an integer n, and two lists of strings a and b, each of length n. After processing, it prints 'No' if the second-to-last character in b is '<', otherwise it prints 'Yes'. The variables t, a, and b are not retained between iterations, and their values are reset with each new iteration.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n`, and two lists of strings `a` and `b`, each of length `n`. The function then checks if the second-to-last character in the list `b` is '<'. If it is, the function prints 'No'; otherwise, it prints 'Yes'. The function does not retain any state between test cases.

