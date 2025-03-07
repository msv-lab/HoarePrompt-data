#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: For each test case, the output is the total count of the substrings 'map' and 'pie' in the string s. The initial state variables t, n, and s are not altered in terms of their values but their roles in the loop determine the number of iterations and the strings processed respectively.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a string `s` of length `n`. For each test case, it calculates the total number of occurrences of the substrings 'map' and 'pie' in the string `s` and prints this count. The input parameters `t`, `n`, and `s` are not altered, but their values determine the number of test cases and the strings to be processed.

