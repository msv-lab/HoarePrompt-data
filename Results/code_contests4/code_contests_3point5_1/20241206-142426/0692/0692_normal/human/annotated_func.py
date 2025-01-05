#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 150000 and 1 <= arr[i] <= 10^6 for all i.**
def func_1(arr):
    days = 0
    for i in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[i] > arr[j]:
                days += 1
                break
        
    #State of the program after the  for loop has been executed: arr is a list of integers where len(arr) is greater than or equal to 2. days is the total number of occurrences where arr[i] > arr[j] for any i < j
#Overall this is what the function does:The function `func_1` accepts a parameter `arr`, which is a list of integers. The function iterates through the list to count the occurrences where an element at a lower index is greater than an element at a higher index. The variable `days` keeps track of these occurrences. The function calculates `days` by comparing each element with all elements that come after it in the list. The function does not have a specific return value mentioned in the description provided.

