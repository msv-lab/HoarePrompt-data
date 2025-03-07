#State of the program right berfore the function call: The function should take three parameters: t, a list of integers n, and a list of tuples where each tuple contains two strings of arrows. t is an integer such that 1 ≤ t ≤ 10^4, each n is an even integer such that 2 ≤ n ≤ 2·10^5, and each string in the tuple consists of exactly n characters '<' and/or '>', representing the arrows in the first and second rows of the grid, respectively. The sum of all n values does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The loop iterates t times, and for each iteration, it reads an integer n, and two strings of arrows a and b, each of length n. After processing, it prints 'No' if the second-to-last character in b is '<', otherwise it prints 'Yes'. The values of t, n, a, and b are not retained after each iteration, so the final state of these variables is undefined.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an even integer `n` and two strings `a` and `b`, each of length `n`, consisting of characters '<' and/or '>'. The function then checks if the second-to-last character in `b` is '<'. If it is, the function prints 'No'; otherwise, it prints 'Yes'. The function does not retain any values of `t`, `n`, `a`, or `b` after each iteration, so the final state of these variables is undefined. The function does not return any values; it only prints the results for each test case.

