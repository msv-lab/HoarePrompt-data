#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: Output State: The value of `t` is now 0 or less, which means there are no more iterations left. `a` is an input integer from the last iteration, `s` is the final input string from the last iteration, `x` is the number of occurrences of 'map' in `s`, and `y` is the number of occurrences of 'pie' in `s`. The loop has completed all its iterations, and the output of each iteration (which was the sum of `x` and `y`) has been printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s` of lowercase Latin letters. For each test case, it counts the occurrences of the substrings 'map' and 'pie' in `s`, sums these counts, and prints the result. After processing all test cases, the variable `t` becomes non-positive, indicating the end of iterations.

