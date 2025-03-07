#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string consisting of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: Output State: The output state will consist of a list of integers, where each integer is the sum of the counts of 'map' and 'pie' in the respective strings provided for each iteration of the loop. For each input integer `t`, the loop will process `t` lines, where each line starts with an integer `n` followed by a string `s`. The output will be the count of 'map' plus the count of 'pie' in each string `s`, printed for each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by `t` pairs of an integer `n` and a string `s`. It then counts the occurrences of the substring 'map' and 'pie' in each string `s`, sums these counts, and prints the result for each test case. The function does not return any value but outputs the sum of counts of 'map' and 'pie' for each input string.

