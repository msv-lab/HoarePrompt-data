#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each a_i is an integer such that 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The output consists of `t` lines, where each line contains the sum of the elements at even indices of the sorted list for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list of `2n` integers, sorts the list, and then calculates the sum of the elements at even indices (0-based). It prints this sum for each test case.

