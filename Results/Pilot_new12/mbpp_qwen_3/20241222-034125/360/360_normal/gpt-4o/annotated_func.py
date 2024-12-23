#State of the program right berfore the function call: list_of_lists is a list of lists of integers.
def func_1(list_of_lists):
    max_sum = float('-inf')
    max_list = []
    for sublist in list_of_lists:
        current_sum = sum(sublist)
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = sublist
        
    #State of the program after the  for loop has been executed: `list_of_lists` is a non-empty list of lists of integers; `max_sum` is the maximum sum of any sublist in `list_of_lists`; `max_list` is the sublist in `list_of_lists` that has the maximum sum. Initially, `max_sum` is -inf, and `max_list` is an empty list. After the loop finishes executing, `max_sum` and `max_list` are updated to reflect the maximum sum and corresponding sublist encountered during the iteration of `list_of_lists`. If no sublists are present in `list_of_lists`, `max_sum` remains -inf and `max_list` remains an empty list.
    return max_list
    #`max_list` which is the sublist in `list_of_lists` that has the maximum sum
#Overall this is what the function does:The function `func_1` accepts a parameter `list_of_lists`, which is a list of lists of integers. It iterates through each sublist to calculate the sum of its elements. It then updates two variables, `max_sum` and `max_list`, to store the maximum sum found and the corresponding sublist. If no sublists have a positive sum, `max_sum` remains `-inf` and `max_list` remains an empty list. The function returns `max_list`, which is the sublist with the highest sum. This means that if all sublists have a sum less than or equal to zero, the function will return an empty list.

