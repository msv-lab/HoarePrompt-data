#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: Output State: The output state consists of "Yes" or "No" printed for each test case based on the condition `if b[n - 2] == '<':`. If the character at index `n-2` in the string `b` is `<`, it prints "No"; otherwise, it prints "Yes". The number of "Yes" and "No" outputs depends on the input provided for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and two strings of length \( n \) made up of '<' and '/>'. For each test case, it checks if the second last character of the second string is '<'. If it is, it prints 'No'; otherwise, it prints 'Yes'. The function does not return any value but prints the results for each test case.

