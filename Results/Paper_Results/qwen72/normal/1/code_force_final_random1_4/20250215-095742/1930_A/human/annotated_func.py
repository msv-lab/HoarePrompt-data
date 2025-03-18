#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: _ is t-1, n is a new input integer greater than 0, l is a sorted list of integers from user input, score is the sum of every second element in l starting from index 0 up to the last even index less than 2 * n, i is 2 * n - 2.
#Overall this is what the function does:The function reads a series of test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the smaller number in each pair of consecutive numbers from the sorted list and prints this sum. After processing all test cases, the function completes, and the final state includes the printed scores for each test case.

