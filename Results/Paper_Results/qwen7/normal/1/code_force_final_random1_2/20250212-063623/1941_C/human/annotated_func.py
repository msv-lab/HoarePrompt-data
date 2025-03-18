#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string consisting of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: The value of `a` is determined by the input for each test case, `s` is the string input for each test case, `x` is the total count of occurrences of 'map' across all strings, and `y` is the total count of occurrences of 'pie' across all strings.
    #
    #Explanation: After all iterations of the loop, `a` will take on the value of the last input integer provided, `s` will be the last string input. However, since the loop processes each string individually and counts 'map' and 'pie' occurrences separately for each string, `x` and `y` will accumulate the counts of 'map' and 'pie' across all strings processed. Thus, `x` and `y` represent the grand totals of 'map' and 'pie' occurrences respectively, summed up from all the input strings.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \), a positive integer \( n \), and a string \( s \) of lowercase Latin letters with length \( n \). For each test case, it counts the occurrences of the substrings 'map' and 'pie' in the string \( s \), and prints the sum of these counts. The function accumulates these counts across all test cases and outputs the total counts of 'map' and 'pie' occurrences after processing all test cases.

