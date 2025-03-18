#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: After all iterations, `t` is an integer where 1 ≤ t ≤ 5000, `n` is an input integer greater than 0, `l` is a sorted list of integers from the final input, `score` is the sum of every second element starting from the first element in `l` up to the last even-indexed element within the range of `2 * n`, `i` is `2 * n`, and `2 * n` is greater than 0. The loop has completed all its iterations for all `t` test cases.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `2n` integers. The function calculates the sum of the smaller numbers in each pair of consecutive integers from the sorted list and prints this sum for each test case. After processing all test cases, the function completes without returning any value. The final state includes the printed scores for each test case, and the input variables are no longer needed.

