#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: Output State: The loop will execute `t` times, where `t` is a positive integer such that 1 ≤ t ≤ 500. For each iteration, `n` is an integer such that 2 ≤ n ≤ 100, and `ar` is a list of strings representing the sorted integers from the input.
    #
    #This means that after all iterations of the loop have finished, `t` will be the total number of test cases processed, with each test case having its own `n` (number of integers) and `ar` (sorted list of those integers).
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (1 ≤ \( t \) ≤ 500) indicating the number of subsequent test cases, followed by an integer \( n \) (2 ≤ \( n \) ≤ 100) and a list of \( n \) integers (1 ≤ \( a_i \) ≤ 10^9). For each test case, it reads the integers, sorts them, and prints the sorted integers as a space-separated string. After processing all test cases, the function concludes without returning any value.

