#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string consisting of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: After the loop executes all its iterations, `a` will contain the input integer for each test case, `s` will be the input string for each test case, `x` will be the total count of occurrences of 'map' across all input strings, and `y` will be the total count of occurrences of 'pie' across all input strings. The loop processes each test case independently, so the final values of `x` and `y` are the sums of their respective counts from all the input strings provided.
#Overall this is what the function does:The function processes multiple test cases, counting the total occurrences of the substrings 'map' and 'pie' in each input string `s`. For each test case, it reads an integer `a`, an integer `n`, and a string `s` of length `n`. It then prints the sum of the counts of 'map' and 'pie' in `s`. After processing all test cases, the function outputs the total count of 'map' and 'pie' across all input strings.

