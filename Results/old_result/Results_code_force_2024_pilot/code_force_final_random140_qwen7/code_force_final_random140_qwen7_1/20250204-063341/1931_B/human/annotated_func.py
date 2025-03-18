#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and there are n integers a_1, a_2, \dots, a_n such that 0 ≤ a_i ≤ 10^9 and the sum of a_i is divisible by n.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: Output State: `t` is greater than 2 and less than or equal to 10^4 - 2, `n` is an input integer, `arr` is a sorted list of integers created from the input split by spaces. If `arr` is a sorted list, the condition remains unchanged. Otherwise, the condition also remains unchanged since no modifications are made in the else part.
    #
    #This means that after the loop has executed all its iterations, `t` will be reduced by the number of iterations (which is equal to its initial value), but it cannot go below 2. Each iteration processes an input `n` and sorts the array `arr`. The final value of `t` will be the initial value minus the number of iterations completed, and `arr` will be sorted as per the input for each iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t`, followed by an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`. It then sorts the list `a` and checks if the list is already sorted. If the list is sorted, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case based on the sorting condition.

