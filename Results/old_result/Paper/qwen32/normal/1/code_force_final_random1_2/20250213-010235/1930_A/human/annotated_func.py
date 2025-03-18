#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the list of integers a_1, a_2, ..., a_{2n} contains exactly 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The final `score` is the sum of the scores from all `t` test cases, where each score is the sum of elements at even indices of the sorted list `l` for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and a list of `2n` integers. It sorts the list and calculates the sum of the elements located at even indices (0-based). The function prints this sum for each test case.

