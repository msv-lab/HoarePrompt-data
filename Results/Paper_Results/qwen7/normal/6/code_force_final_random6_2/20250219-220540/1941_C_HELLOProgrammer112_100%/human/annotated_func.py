#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters and has a length of n. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: Output State: The loop has executed all its iterations. For each iteration, `a` is an input integer, `s` is a string input by the user, `x` is the number of occurrences of 'map' in `s`, `y` is the number of occurrences of 'pie' in `s`, and `z` is the number of occurrences of 'mapie' in `s`. After all iterations, `num_iterations` equals the total number of test cases processed, and both `a` and `s` are reset to the values of the last test case's input integer and string, respectively. The final printed value is the sum of `x` and `y` minus `z` for the last input string `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \(a\) and a string \(s\). For each test case, it counts the occurrences of the substrings 'map', 'pie', and 'mapie' in \(s\), and prints the result of adding the counts of 'map' and 'pie' and then subtracting the count of 'mapie'. After processing all test cases, the function outputs the final result for the last input string \(s\).

