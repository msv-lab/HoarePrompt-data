#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: Output State: The loop will have processed all the test cases provided as input. For each test case, `n` is an integer such that 2 ≤ n ≤ 100, and `ar` is a map object containing strings of integers sorted in ascending order based on the input integers for that specific test case.
    #
    #This means that after all iterations of the loop have finished, the program will have read all the test cases, sorted the integers provided for each test case in ascending order, and printed them out. Each test case's output will reflect the sorted integers for that particular set of inputs.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads an integer \( t \) (number of test cases, where \( 1 \leq t \leq 500 \)), an integer \( n \) (number of integers in each test case, where \( 2 \leq n \leq 100 \)), and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \) (each integer in the range \( 1 \leq a_i \leq 10^9 \)). It sorts these integers in ascending order and prints them out. The function does not return any value but ensures that all test cases are processed and their sorted integers are printed accordingly.

