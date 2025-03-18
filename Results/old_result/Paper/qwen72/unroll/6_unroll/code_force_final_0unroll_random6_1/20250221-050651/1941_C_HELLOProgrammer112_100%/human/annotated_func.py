#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 10^6) and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The function will print the result of `x + y - z` for each test case, where `x` is the number of occurrences of the substring 'map' in the string `s`, `y` is the number of occurrences of the substring 'pie' in the string `s`, and `z` is the number of occurrences of the substring 'mapie' in the string `s`. The values of `x`, `y`, and `z` are calculated for each test case independently. The initial state of the function parameters `t` and the list of tuples remains unchanged.
#Overall this is what the function does:The function reads input from the user for a specified number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters. It then calculates the number of occurrences of the substrings 'map', 'pie', and 'mapie' within `s`, and prints the result of `x + y - z`, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. The function does not return any value; it only prints the results for each test case. The initial state of the function parameters is not preserved as the function does not accept any parameters directly.

