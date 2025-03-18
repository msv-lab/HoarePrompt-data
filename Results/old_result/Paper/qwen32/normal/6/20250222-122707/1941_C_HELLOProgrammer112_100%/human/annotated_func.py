#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 10^6) representing the length of the string s, followed by the string s itself, which consists of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The output state after all iterations is the sequence of results for each of the `t` test cases, where each result is the value of `x + y - z` for the corresponding test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of lowercase Latin letters. For each test case, it calculates the number of occurrences of the substrings 'map' and 'pie' in the string, subtracts the number of occurrences of the substring 'mapie', and prints the result.

