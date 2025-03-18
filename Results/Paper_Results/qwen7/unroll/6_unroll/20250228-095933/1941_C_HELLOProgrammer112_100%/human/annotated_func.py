#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: The output state is a list of integers where each integer represents the result of the expression `x + y - z` for each test case. Here, `x` is the number of occurrences of the substring "map", `y` is the number of occurrences of the substring "pie", and `z` is the number of occurrences of the substring "mapie" in the respective input string `s` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t`, a positive integer `n`, and a string `s` of length `n`. For each test case, it counts the occurrences of the substrings "map", "pie", and "mapie" in the string `s`. It then calculates and prints the result of the expression `x + y - z`, where `x` is the count of "map", `y` is the count of "pie", and `z` is the count of "mapie". The final output is a list of these results for all test cases.

