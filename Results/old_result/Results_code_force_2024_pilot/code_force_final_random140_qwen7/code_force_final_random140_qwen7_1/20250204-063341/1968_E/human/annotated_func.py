#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: Output State: The loop will execute until `i` reaches `n + 2`, and the final value of `i` will be `n + 2`. This means that after all iterations, `i` will be `n + 2`, where `n` is an integer such that `2 ≤ n ≤ 10^3`.
    #
    #In simpler terms, after the loop completes all its iterations, the value of `i` will be `n + 2`, and `n` can be any integer between 2 and 1000, inclusive.
#Overall this is what the function does:The function processes a series of test cases, where each test case includes an integer `t` (1 ≤ t ≤ 50) and an integer `n` (2 ≤ n ≤ 10^3). For each test case, it prints a sequence of pairs of integers. Specifically, it prints (1, 1), (1, 2), followed by pairs (i, i) for `i` ranging from 3 to `n + 1`. After processing all test cases, it does not return any value but outputs the generated sequence of pairs.

