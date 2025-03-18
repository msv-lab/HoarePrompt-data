#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: Output State: The loop will continue to execute as long as there are more test cases (as specified by the value of `t`). After all iterations of the loop have finished, `t` will be a positive integer such that 0 ≤ t < 500, meaning no more test cases remain. For each test case, `n` will be an input integer such that 2 ≤ n ≤ 100, and `ar` will be a list of strings representing the sorted integers from the input for each respective test case.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` will be 0, indicating that all test cases have been processed. For each test case, `n` will be the number of integers provided, and `ar` will contain those integers sorted and converted to strings.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer \( t \) (indicating the number of test cases), followed by an integer \( n \) and a list of \( n \) integers. It sorts these integers, converts them to strings, and prints the sorted list for each test case. After processing all test cases, the variable \( t \) is set to 0, indicating that no more test cases remain.

