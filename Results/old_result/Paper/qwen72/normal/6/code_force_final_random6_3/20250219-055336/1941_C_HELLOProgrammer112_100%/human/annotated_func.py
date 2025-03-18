#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of tuples test_cases, where each tuple contains an integer n (1 ≤ n ≤ 10^6) and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: After all iterations, `int(input())` has been fully consumed, `_` is equal to `int(input())` - 1, `a` is the last input integer greater than 0, `s` is the last input string, `x` is the number of times 'map' appears in the last `s`, `y` is the number of times 'pie' appears in the last `s`, `z` is the number of times 'mapie' appears in the last `s`.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` and a string `s` from the input. It then calculates the number of times the substrings 'map', 'pie', and 'mapie' appear in `s`, and prints the result of `x + y - z`, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. After processing all test cases, the function has no return value, but the input stream is fully consumed, and the final printed results correspond to the calculations for each test case.

