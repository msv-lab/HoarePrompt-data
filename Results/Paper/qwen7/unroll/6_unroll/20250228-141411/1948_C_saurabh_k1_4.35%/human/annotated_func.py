#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'; there are no arrows pointing outside the grid; the sum of n over all test cases doesn't exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'; the output will be 'Yes' if the second last character of the second input string is not '<', otherwise 'No'; there are no arrows pointing outside the grid; the sum of n over all test cases doesn't exceed 2 \cdot 10^5.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) (2 ≤ \( n \) ≤ 2 * 10^5 and \( n \) is even), and two strings of length \( n \) made up of characters '<' and/or '>'. For each test case, it checks if the second last character of the second string is not '<'. If true, it prints 'Yes'; otherwise, it prints 'No'. The function ensures it processes up to 10^4 test cases, and the total \( n \) across all test cases does not exceed 2 * 10^5.

