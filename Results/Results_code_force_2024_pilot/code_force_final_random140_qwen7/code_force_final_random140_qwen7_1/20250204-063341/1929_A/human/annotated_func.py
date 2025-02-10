#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: Output State: The loop has executed all its iterations, with `t` being a new positive integer input by the user after the last iteration. For each iteration, `n` is an input integer, and `ar` is a sorted list of integers input by the user, converted from a space-separated string of integers. After all iterations, the final value of `t` will be the input provided for the last iteration, and the corresponding `ar` will be the sorted list of integers for the last input `n`.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be the value it was set to on the last iteration, `n` will be the last input integer, and `ar` will be the sorted list of integers from the last input, all based on the inputs provided during the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). For each test case, it sorts the list of integers and calculates the sum of differences between consecutive elements in the sorted list. The function then prints this sum for each test case. After processing all test cases, it outputs the final value of \( t \), which is the number of test cases processed.

