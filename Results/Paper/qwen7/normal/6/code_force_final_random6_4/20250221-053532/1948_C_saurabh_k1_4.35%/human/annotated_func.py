#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'; the sum of n over all test cases doesn't exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: Output State: The loop will have executed for all test cases provided. For each test case, `n` will be an integer between 2 and 2⋅10^5 (inclusive) and is even. `a` will be a list of strings where each string is a character from the input string for that test case, and `b` will be a list of strings created by converting each character of the input string for that test case to a string. After processing all test cases, if for any test case `b[n-2]` is not equal to '<', the loop will have printed 'Yes' for that test case; otherwise, it will have printed 'No'. The final state will reflect the outcome of running the loop for all test cases, with `n`, `a`, and `b` updated according to the inputs of each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( n \) (2 ≤ \( n \) ≤ 2⋅10^5 and \( n \) is even), and two strings of length \( n \) consisting of characters '<' and '/>'. For each test case, it reads the two strings, checks if the second last character of the second string is '<', and prints 'No' if true, otherwise prints 'Yes'. After processing all test cases, it outputs the results for each case.

