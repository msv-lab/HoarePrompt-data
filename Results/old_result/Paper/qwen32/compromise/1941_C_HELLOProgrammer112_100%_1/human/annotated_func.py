#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: For each test case, the number of occurrences of the substring 'map' and 'pie' in the string `s` is counted, and the number of occurrences of the substring 'mapie' is subtracted from their sum. The result is printed for each test case. The values of `t`, `n`, and `s` from the initial state remain unchanged except that `s` is replaced by the next test case string in subsequent iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `s` of length `n`. For each test case, it calculates the number of occurrences of the substrings 'map' and 'pie' in `s`, subtracts the number of occurrences of the substring 'mapie', and prints the result. The input values `t`, `n`, and `s` are used to perform these calculations, with `t` indicating the number of test cases.

