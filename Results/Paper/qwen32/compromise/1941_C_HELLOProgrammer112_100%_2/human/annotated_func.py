#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, each test case consists of an integer n such that 1 <= n <= 10^6, and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The output state consists of t lines, each containing an integer. Each integer represents the count of non-overlapping occurrences of the substrings 'map' and 'pie' in the string s of the corresponding test case, minus the count of non-overlapping occurrences of the substring 'mapie'. The values of t, n, and s from the initial state remain unchanged except that s is used in each iteration to compute the output for that iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string `s`. For each string, it calculates the number of non-overlapping occurrences of the substrings 'map' and 'pie', and subtracts the number of non-overlapping occurrences of the substring 'mapie'. The result for each test case is printed as an integer.

