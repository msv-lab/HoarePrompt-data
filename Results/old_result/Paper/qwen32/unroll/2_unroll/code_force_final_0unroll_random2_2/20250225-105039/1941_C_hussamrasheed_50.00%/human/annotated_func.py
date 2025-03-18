#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case there is an integer n such that 1 ≤ n ≤ 10^6, and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: A series of integers, each representing the sum of occurrences of 'map' and 'pie' in the corresponding input string for each of the `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string. It counts the occurrences of the substrings 'map' and 'pie' in each string, removes all occurrences of 'map', and then counts 'pie' again in the modified string. For each test case, it outputs the sum of these counts.

