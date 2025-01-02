#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, d is an integer such that d > 0, and each friend is described by two integers mi and si where 0 ≤ mi, si ≤ 10^9.
def func():
    read_input = map(int, raw_input().split())
    n = read_input[0]
    d = read_input[1]
    input_list = []
    for i in range(n):
        user_input = map(int, raw_input().split())
        
        input_list.append((user_input[0], user_input[1]))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `read_input` is a list of integers excluding the first element, `input_list` is a list of tuples where each tuple contains two integers `(user_input[0], user_input[1])` entered by the user, and `user_input` is a map object of integers entered by the user.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer; `read_input` is a list of integers excluding the first element; `input_list` is a list of tuples sorted lexicographically; `user_input` is a map object of integers entered by the user; `max_factor` is the maximum value obtained during the loop execution; `partial_sum` is the final value of the sum calculated during the loop; `j` is the last index of the tuple used in the loop.
    print(max_factor)
#Overall this is what the function does:The function processes a list of friends, each described by two integers \( m_i \) and \( s_i \), along with the number of friends \( n \) and a positive integer \( d \). It sorts the list of friends based on \( m_i \) and then iterates through the list to find the maximum value of the partial sum \( s_i \) within a distance \( d \). Specifically, for each friend \( i \), it considers the sum of \( s \)-values starting from the current friend up to the point where the difference between the current and the previous friend's \( m \)-value is less than \( d \). The function then prints the maximum value found during this process. If no valid partial sum can be formed (i.e., all friends are too far apart), the function will still correctly identify and print the largest individual \( s_i \) value.

