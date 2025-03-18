#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: The output state is a list of results, where each result is calculated from the input values of `a` and the string `s` for each test case. Specifically, for each test case, the result is the count of occurrences of the substring 'map' plus the count of occurrences of the substring 'pie', minus twice the count of occurrences of the substring 'mapie'. This process is repeated for each test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `a`, a string `s`, counts the occurrences of the substrings 'map', 'pie', and 'mapie' within `s`, and prints the result which is the count of 'map' plus the count of 'pie' minus twice the count of 'mapie'. This process is repeated for each test case provided by the input. The function does not return any value but outputs the results for each test case.

