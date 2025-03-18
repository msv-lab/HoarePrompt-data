#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length of n across all test cases not exceeding 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: Output State: `t` must be greater than 0, `i` is equal to `t`, `n` is an input integer, `s` is the string input by the user without any occurrence of 'map', `m` is the number of occurrences of 'map' in the original `s`, `p` is the number of occurrences of 'pie' in `s`.
    #
    #This means that after all iterations of the loop have finished, the variable `i` will be equal to `t` (the total number of iterations), and for each iteration, the string `s` had all instances of 'map' removed, with `m` and `p` being the counts of 'map' and 'pie' in the original string `s`, respectively. The values of `t`, `n`, and the final state of `s` will reflect the last iteration's inputs and transformations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 10^4) and a string `s` (1 ≤ length of `s` ≤ 10^6). For each test case, it removes all occurrences of the substring 'map' from `s`, counts the remaining occurrences of 'pie', and prints the sum of the counts of 'map' and 'pie' from the original string `s`. After processing all test cases, the function does not return any value but outputs the results for each test case.

