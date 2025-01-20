#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 100 and 1 ≤ k ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ k.
def func():
    n, k = map(int, input().split())

marks = list(map(int, input().split()))

current_sum = sum(marks)

current_count = n
    while True:
        current_average = current_sum / current_count
        
        if math.ceil(current_average) >= k:
            print(current_count - n)
            break
        
        current_sum += k
        
        current_count += 1
        
    #State of the program after the loop has been executed: n is the same as the input integer n, k is the same as the input integer k, marks is a list of n integers read from the input, current_sum is current_sum + m*k, current_count is current_count + m, where m is the minimum number of iterations required such that math.ceil((current_sum + m*k) / (current_count + m)) >= k, and current_count - n is printed.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, followed by a list of `n` integers. It then calculates the minimum number of additional values, each equal to `k`, that need to be added to the list to ensure that the ceiling of the average of the list is at least `k`. The function prints the number of additional values needed. After the function concludes, `n` and `k` remain unchanged, `marks` is a list of `n` integers read from the input, `current_sum` is the sum of the original list plus `m * k` (where `m` is the number of additional values added), and `current_count` is `n + m`. The function does not return any value; it only prints the result. Edge cases include scenarios where the initial list already meets the condition, in which case no additional values are needed, and scenarios where the list contains values that are significantly less than `k`, requiring a large number of additional values to meet the condition.

