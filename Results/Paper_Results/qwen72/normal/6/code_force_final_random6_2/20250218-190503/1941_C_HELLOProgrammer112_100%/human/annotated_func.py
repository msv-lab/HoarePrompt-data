#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s_list where each string s in s_list has a length n (1 ≤ n ≤ 10^6) consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The loop has executed `t` times, where `t` is the initial input integer representing the number of test cases. For each iteration, `a` was an input integer greater than 0, `s` was an input string, `x` was the number of times 'map' appeared in `s`, `y` was the number of times 'pie' appeared in `s`, and `z` was the number of times 'mapie' appeared in `s`. The final output for each test case is the value of `x + y - z`.
#Overall this is what the function does:The function `func` takes no parameters and does not return any value. It reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` (which is not used in the function) and a string `s`. The function then calculates the number of times the substrings 'map', 'pie', and 'mapie' appear in `s`, and prints the result of `x + y - z` for each test case, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. After processing all `t` test cases, the function concludes.

