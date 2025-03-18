#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: Output State: The value of `t` remains an integer within the range 1 ≤ t ≤ 500. After all iterations of the loop have finished, `n` will be the last input integer received, and `ar` will be a sorted list of integers obtained from the last input.
    #
    #In natural language: After the loop has completed all its iterations, the variable `t` retains its initial value which is any integer between 1 and 500 inclusive. The variable `n` will hold the value of the last integer input during the loop's execution, and `ar` will contain the sorted list of integers from the last input, also received during the loop's iterations.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads an integer \( t \) (1 ≤ \( t \) ≤ 500) representing the number of cases, followed by an integer \( n \) (2 ≤ \( n \) ≤ 100) and a list of \( n \) integers \( a_1, a_2, ..., a_n \) (1 ≤ \( a_i \) ≤ \( 10^9 \)). It then sorts the list of integers and calculates the sum of differences between consecutive elements in the sorted list, printing this sum for each test case. The function does not return any value but modifies the state by processing the input data according to the specified constraints.

