#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: All test cases processed, variables n, l, and score are out of scope.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n` and a list `a` of `2n` integers. For each test case, it calculates the sum of the smallest `n` integers from the list and prints this sum. After processing all test cases, the function concludes with no variables from the test cases remaining in scope.

