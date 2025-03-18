#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: The output state will consist of a series of integers, each representing the sum of the counts of the substrings 'map' and 'pie' for each input string \(s\) across all test cases. Each integer corresponds to one test case's result, printed in the order they were processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer `t`, a string `s` consisting of lowercase Latin letters, and counts the occurrences of the substrings 'map' and 'pie' in `s`. It then prints the sum of these counts for each test case. The function does not return any value but outputs the results for all test cases.

