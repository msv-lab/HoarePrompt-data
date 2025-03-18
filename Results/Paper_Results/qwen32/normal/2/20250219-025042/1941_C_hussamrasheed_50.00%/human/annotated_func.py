#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: The loop has completed `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and a string `s` of length `n`. It then counts the occurrences of the substrings 'map' and 'pie' in `s`, removes all occurrences of 'map' from `s`, and counts the occurrences of 'pie' again in the modified string. Finally, it prints the sum of the initial count of 'map' and the count of 'pie' after removing 'map'.

