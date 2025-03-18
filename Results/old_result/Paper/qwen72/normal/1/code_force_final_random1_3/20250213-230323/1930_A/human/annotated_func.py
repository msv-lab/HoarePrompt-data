#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: After all iterations of the loop, `t` is an integer where 1 ≤ t ≤ 5000, `n` is an input integer, `l` is a sorted list of integers from the last input, `score` is the sum of every second element starting from the first element in `l` (i.e., the sum of `l[0]`, `l[2]`, `l[4]`, ..., `l[2*n-2]`), and the loop has completed all its iterations for all `t` test cases.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of 2n integers, sorts the list, and calculates the sum of every second element starting from the first element in the sorted list. It then prints the calculated sum for each test case. After processing all test cases, the function completes, and no further state is maintained.

