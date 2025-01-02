#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and d is an integer such that d > 0. Each friend is described by two integers mi and si, where 0 ≤ mi, si ≤ 10^9, representing the amount of money and the friendship factor, respectively.
def func():
    read_input = map(int, raw_input().split())
    n = read_input[0]
    d = read_input[1]
    input_list = []
    for i in range(n):
        user_input = map(int, raw_input().split())
        
        input_list.append((user_input[0], user_input[1]))
        
    #State of the program after the  for loop has been executed: `n` is read_input[0] and must be greater than 0, `d` is read_input[1], `read_input` is a list containing `n + d` integers, the first `n` integers correspond to `mi` values and the last `d` integers correspond to `si` values, `input_list` is a list of tuples, each tuple consisting of two integers, where the tuples were appended to `input_list` during the loop iterations, `i` is `n`.
    input_list.sort()
    max_factor = input_list[0][1]
    partial_sum = input_list[0][1]
    j = 0
    for i in range(1, n):
        while input_list[i][0] - input_list[j][0] >= d:
            partial_sum -= input_list[j][1]
            j += 1
        
        partial_sum += input_list[i][1]
        
        max_factor = max(max_factor, partial_sum)
        
    #State of the program after the  for loop has been executed: `n` is read_input[0] and must be greater than 0, `d` is read_input[1], `read_input` is a list containing `n + d` integers, the first `n` integers correspond to `mi` values and the last `d` integers correspond to `si` values, `input_list` is a list of tuples, each tuple consisting of two integers, where the tuples were appended to `input_list` during the loop iterations, `input_list` is sorted based on the first elements of the tuples, `i` is `n + d`, `max_factor` is the second element of the tuple with the smallest first element in `input_list` (updated to the maximum of its current value and `partial_sum` after the loop), `partial_sum` is the maximum value of `partial_sum` obtained during the loop, `j` is `n + d`, and the last pair in `input_list` satisfies `input_list[i-1][0] - input_list[j-1][0] >= d`.
    print(max_factor)
#Overall this is what the function does:The function processes a list of friends, each described by two integers `mi` (amount of money) and `si` (friendship factor). It reads the number of friends `n` and a threshold `d`. For each friend, it reads `mi` and `si`. After sorting the friends based on their `mi` values, it calculates the maximum possible sum of `si` values within intervals of length `d`. Specifically, it iterates through the sorted list, maintaining a running sum of `si` values and updating the maximum sum encountered. If the difference between the current and previous `mi` values is greater than or equal to `d`, it adjusts the running sum by subtracting the `si` value of the previous friend. The function returns the maximum sum of `si` values found during this process. Potential edge cases include when `n` is 0 or when the `mi` values are not sufficiently spaced to meet the threshold `d`.

