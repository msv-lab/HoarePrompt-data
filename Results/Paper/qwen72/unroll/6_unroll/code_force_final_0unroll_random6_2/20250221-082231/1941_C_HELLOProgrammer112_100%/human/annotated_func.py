#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 10^6) and a string s of length n, where s consists of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The loop will execute t times, and for each test case, it will print the value of `x + y - z`, where `x` is the number of occurrences of the substring 'map' in `s`, `y` is the number of occurrences of the substring 'pie' in `s`, and `z` is the number of occurrences of the substring 'mapie' in `s`. The values of `x`, `y`, and `z` will be recalculated for each test case, and the final output will be the sum of `x + y - z` for each test case. The variables `a` and `s` will be updated for each test case, but the overall state of the function will remain the same as the initial state, except for the printed output.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` (which is not used in the function) and a string `s`. It then calculates the number of occurrences of the substrings 'map', 'pie', and 'mapie' in `s`, and prints the result of `x + y - z`, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. The function does not return any value; it only prints the results for each test case. After the function concludes, the printed output will contain `t` lines, each corresponding to the result for a test case. The variables `a` and `s` are updated for each test case, but they do not persist outside the function.

