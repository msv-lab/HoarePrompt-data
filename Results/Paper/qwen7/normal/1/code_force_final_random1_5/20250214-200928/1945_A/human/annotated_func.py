#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `b` is the sum of its original value and all `c` values from each input line, `a` is the first part of the split string from the last input line, `c` is the third part of the split string from the last input line, and `s` is the last line in the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers a, b, and c representing the number of introverts, extroverts, and universals, respectively. It calculates the sum of b and c for each test case and updates b accordingly. After processing all test cases, it prints the result based on the updated values of a and b, specifically the count of possible ways to arrange the people satisfying certain conditions, or an error message if the total number of people exceeds the constraint 1 ≤ t ≤ 10^4.

