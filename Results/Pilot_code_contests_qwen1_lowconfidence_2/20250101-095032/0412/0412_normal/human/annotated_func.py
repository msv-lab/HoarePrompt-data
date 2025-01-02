#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and d is a non-negative integer. Each friend is described by two non-negative integers mi and si, where 0 ≤ mi, si ≤ 10^9, representing the amount of money and the friendship factor, respectively.
def func():
    read_input = map(int, raw_input().split())
    n = read_input[0]
    d = read_input[1]
    input_list = []
    for i in range(n):
        user_input = map(int, raw_input().split())
        
        input_list.append((user_input[0], user_input[1]))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `read_input` is a list of integers, `d` is the second element of `read_input`, `user_input` is a list of integers obtained from `raw_input().split()`, `input_list` is a list of tuples where each tuple contains the first two elements of `user_input` for each iteration, the length of `input_list` is equal to `n`.
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
        
    #State of the program after the  for loop has been executed: `i` is `n`, `j` is the index where the condition `input_list[i][0] - input_list[j][0] < d` first holds, `partial_sum` is the maximum of its original value and the sum of selected elements from `input_list`, `max_factor` is the maximum value of `partial_sum` after all iterations, and `input_list[i][0]` must be at least `d` units greater than `input_list[j][0]` if `i < n`.
    print(max_factor)
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer such that \(1 \leq n \leq 10^5\)) and `d` (a non-negative integer), along with a list of friends described by their `mi` and `si` values. It processes this input to find the maximum possible sum of `si` values such that the corresponding `mi` values are at most `d` units apart. The function sorts the input list of friends by their `mi` values, then iterates through the sorted list to maintain a running sum of `si` values while ensuring the difference between consecutive `mi` values does not exceed `d`. The function outputs the maximum sum found. The function handles edge cases such as when `n` is 1 or when no valid pairs exist within the given constraint. If no valid pairs can be formed, the function will output 0.

