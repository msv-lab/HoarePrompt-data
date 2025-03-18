#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: After all iterations of the loop have finished, `t` is a positive integer such that \(1 \leq t-2 \leq 10^4\), `a` is the last input integer, `s` is the last input string from the user, `x` is the total number of occurrences of 'map' in all input strings, `y` is the total number of occurrences of 'pie' in all input strings, and `z` is the total number of occurrences of 'mapie' in all input strings. The loop processes each test case individually, updating `x`, `y`, and `z` with counts from each input string, and prints the result `x + y - z` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes a positive integer `t` (1 ≤ t ≤ 10^4), a positive integer `n` (1 ≤ n ≤ 10^6), and a string `s` of length `n` consisting of lowercase Latin letters. For each test case, it counts the occurrences of the substrings 'map', 'pie', and 'mapie' in the string `s`. It then prints the result of `x + y - z` for each test case, where `x` is the count of 'map', `y` is the count of 'pie', and `z` is the count of 'mapie'. After processing all test cases, the function does not return any value.

