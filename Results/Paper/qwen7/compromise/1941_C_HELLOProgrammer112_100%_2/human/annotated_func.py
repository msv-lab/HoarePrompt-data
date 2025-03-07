#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: The output state is a collection of integers, where each integer represents the result of the expression `x + y - z` for each test case. Here, `x` is the count of occurrences of the substring "map", `y` is the count of occurrences of the substring "pie", and `z` is the count of occurrences of the substring "mapie". Each result is printed on a new line after processing all the substrings in the input string `s` for a particular test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes a positive integer `t` indicating the number of queries, an integer `n` representing the length of the string `s`, and a string `s` consisting of lowercase Latin letters. For each query within a test case, the function counts the occurrences of the substrings "map", "pie", and "mapie" in `s`. It then calculates and prints the result of the expression `x + y - z` for each query, where `x` is the count of "map", `y` is the count of "pie", and `z` is the count of "mapie". The function outputs these results for all queries in all test cases.

