#State of the program right berfore the function call: The function should accept three parameters: an integer t representing the number of test cases, a list of integers n where each integer represents the number of columns in the grid for each test case, and a list of tuples where each tuple contains two strings of length n representing the arrows in the first and second rows of the grid. Each string consists only of the characters '<' and '>', and n is even. The sum of all n values does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The loop iterates over the number of test cases specified by `t`. For each test case, it reads the integer `n` and two strings `a` and `b` of length `n`. After processing, the loop prints 'No' if the second-to-last character in `b` is '<', otherwise it prints 'Yes'. The variables `t`, `n`, `a`, and `b` are reset for each test case, and their values are not retained between iterations.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads an integer `n` and two strings `a` and `b` of length `n`. It then checks if the second-to-last character in the string `b` is '<'. If it is, the function prints 'No'; otherwise, it prints 'Yes'. The function does not return any value; it only prints the results to the standard output. The variables `n`, `a`, and `b` are reset for each test case, and their values are not retained between iterations.

