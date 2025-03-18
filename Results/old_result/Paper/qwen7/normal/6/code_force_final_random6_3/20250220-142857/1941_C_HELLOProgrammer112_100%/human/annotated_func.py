#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length of n across all test cases not exceeding 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: The value of `t` remains a positive integer such that \(1 \leq t \leq 10^4\). After all iterations of the loop, `a` will be the last input integer provided, `s` will be the last string input by the user, `x` will be the total number of occurrences of 'map' in `s` across all iterations, `y` will be the total number of occurrences of 'pie' in `s` across all iterations, and `z` will be the total number of occurrences of 'mapie' in `s` across all iterations. The loop processes each test case independently, so the final values of `x`, `y`, and `z` represent the cumulative counts from all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s` containing lowercase Latin letters. It calculates the total number of occurrences of the substrings 'map', 'pie', and 'mapie' in `s` across all test cases. For each test case, it prints the result of `(number of 'map' occurrences + number of 'pie' occurrences - number of 'mapie' occurrences)`. The final state of the program includes the last input integer `a`, the last string `s`, and the cumulative counts of 'map', 'pie', and 'mapie' occurrences.

