#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: Output State: The value of `t` minus the total number of 'map' occurrences in all inputs plus the total number of 'pie' occurrences in all inputs.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by `t` pairs of an integer `n` and a string `s`. It counts the occurrences of the substring 'map' in each `s`, removes all instances of 'map' from `s`, counts the occurrences of the substring 'pie' in the modified `s`, and prints the sum of these two counts. After processing all test cases, it outputs the total sum of these counts across all test cases.

