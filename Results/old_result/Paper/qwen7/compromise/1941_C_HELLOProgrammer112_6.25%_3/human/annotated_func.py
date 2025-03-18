#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length of n across all test cases not exceeding 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: The sum of counts of the substring "map" and "pie" for each input string s across all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s` made up of lowercase Latin letters. For each test case, it counts the occurrences of the substrings "map" and "pie" in `s`, sums these counts, and prints the result. The function does not return any value but prints the sum of counts for each test case.

