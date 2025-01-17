#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are integers such that 1 ≤ a_i ≤ 10^6.
def func():
    n_tests = int(input())
    for i in range(n_tests):
        n = int(input())
        
        x = [int(i) for i in input().split()]
        
        counter = x[0]
        
        for i in range(1, len(x)):
            if x[i] == 1:
                counter += 1
            elif counter > x[i]:
                counter = x[i] * ceil(counter / x[i])
            elif counter < x[i]:
                counter = x[i]
            else:
                counter = x[i] * 2
        
        print(counter)
        
    #State of the program after the  for loop has been executed: `n_tests` is a positive integer within the range 1 to 1000, `counter` is the final value of `counter` after processing all test cases, `x` is a list of integers, and `i` is `len(x)` for each test case. If the loop does not execute (when the length of `x` is less than 2), `counter` remains the first element of the list `x`.
#Overall this is what the function does:The function processes a series of test cases, each containing a list of integers. For each test case, it initializes a counter with the first element of the list. It then iterates through the rest of the elements in the list, updating the counter based on specific conditions:
1. If the current element is 1, the counter is incremented by 1.
2. If the current element is greater than the counter, the counter is updated to the current element multiplied by the ceiling of the counter divided by the current element.
3. If the current element is equal to the counter, the counter is doubled.
4. If the current element is less than the counter, the counter is updated to the current element.
After processing all elements in the list for each test case, the function prints the final value of the counter. The function accepts an integer `n_tests` representing the number of test cases and for each test case, it takes an integer `n` representing the number of elements in the list, followed by a list of integers `a_i`. The function does not return anything but prints the final counter value for each test case. Edge cases include when the length of the list is less than 2, in which case the counter remains the first element of the list.

