#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters and has length n. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: The sum of counts of occurrences of 'map' and 'pie' for each input string s across all test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer `t`, a string `s` consisting of lowercase Latin letters, and calculates the total count of occurrences of the substrings 'map' and 'pie' in `s`. It then prints this total count for each test case. The function does not return any value but outputs the results directly.

