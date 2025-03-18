#State of the program right berfore the function call: The function will receive an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the function will receive three integers a, b, and c (0 ≤ a, b, c ≤ 10^9) representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The output state consists of the series of printed results for each test case, which are the values of the expression `(a - -b // 3, -1)[c < b % 3]` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing the counts of introverts, extroverts, and universals. For each test case, it calculates and prints a value based on these counts. The printed value is either the total number of individuals adjusted by a third of the sum of extroverts and universals, or -1 if the number of universals is less than the remainder when the sum of extroverts and universals is divided by 3.

