#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The final value of `score` will be the sum of every second element in the list `l`, starting from the first element and going up to the last element in steps of 2.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and 2n integers. For each test case, it sorts the 2n integers, then sums every second element starting from the first, and prints the sum. After processing all test cases, the function concludes without returning any value.

