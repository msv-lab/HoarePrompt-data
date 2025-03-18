#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>' representing the direction of the arrow in the corresponding cell of the grid.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>' representing the direction of the arrow in the corresponding cell of the grid; after executing all iterations of the loop, for each test case, if the second last character of the second string is '<', the output will be 'No', otherwise the output will be 'Yes'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of length n (where 2 ≤ n ≤ 2⋅10^5 and n is even), containing only '<' or '>' characters. For each test case, it checks if the second last character of the second string is '<'. If true, it prints 'No'; otherwise, it prints 'Yes'. The function does not return any value but prints the result for each test case.

