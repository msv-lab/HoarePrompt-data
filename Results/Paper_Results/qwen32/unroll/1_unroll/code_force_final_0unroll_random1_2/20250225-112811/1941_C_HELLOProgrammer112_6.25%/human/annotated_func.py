#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: For each test case, the output will be the sum of the occurrences of the substring 'map' and the substring 'pie' in the string s. The variable t will remain unchanged as it represents the number of test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then calculates and prints the total number of times the substrings 'map' and 'pie' appear in the string `s`.

