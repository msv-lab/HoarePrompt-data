#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s_list where each string s in s_list has a length n (1 ≤ n ≤ 10^6) consisting of lowercase Latin letters. The sum of all n values across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The loop will execute t times, and for each iteration, it will read an integer a and a string s from the input. The variables x, y, and z will be calculated as the counts of the substrings 'map', 'pie', and 'mapie' in s, respectively. The loop will print the value of x + y - z for each test case. After all iterations, the values of t and s_list will remain unchanged, and the variables a, s, x, y, and z will be undefined or reset for each new test case.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` and a string `s` from the input. It then calculates the counts of the substrings 'map', 'pie', and 'mapie' in `s` and prints the value of `x + y - z` for each test case, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. The function does not return any value and does not modify the input parameters. After the function concludes, the input values remain unchanged, and the variables used within the function are reset for each test case.

