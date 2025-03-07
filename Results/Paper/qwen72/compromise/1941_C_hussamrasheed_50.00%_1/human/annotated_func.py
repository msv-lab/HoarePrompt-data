#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples test_cases, where each tuple contains an integer n (1 ≤ n ≤ 10^6) and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: The variable `t` remains unchanged. The list `test_cases` is not modified. For each test case, the number of occurrences of the substring 'map' and 'pie' in the string `s` are counted, and the sum of these counts is printed. The variables `n`, `s`, `m`, and `p` are updated for each iteration of the loop, but their final values after the loop are not retained.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` from the input. It then counts the occurrences of the substrings 'map' and 'pie' in `s`, removes all occurrences of 'map' from `s`, and prints the sum of the counts of 'map' and 'pie'. The function does not modify the input parameters or return any values. After the function concludes, the input variables remain unchanged, and the counts for each test case are printed to the console.

