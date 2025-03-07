#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s where each string has a length n (1 ≤ n ≤ 10^6) consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: The loop has finished executing all iterations. The values of the variables `t` and `s` remain unchanged. The loop has printed the sum of the counts of the substrings 'map' and 'pie' for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` (which is not used) and a string `s`. It then counts the occurrences of the substrings 'map' and 'pie' in `s` and prints the sum of these counts. The function does not return any value; it only prints the results for each test case. The state of the program after the function concludes is that all test cases have been processed, and the counts have been printed. The input variables `t` and `s` are not modified by the function.

