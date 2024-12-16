#State of the program right berfore the function call: lst is a list and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #To understand the impact of the code on the program, let's break down the given information and the code itself.
    #
    #1. **Initial State**: 
    #   - `lst` is a list.
    #   - `L` is a non-negative integer such that `0 <= L <= len(lst)`.
    #   
    #2. **Code Analysis**:
    #   - The code `return lst[:L], lst[L:]` is splitting the list `lst` into two parts at the index `L`.
    #   - `lst[:L]` returns a slice of the list from the start up to, but not including, the element at index `L`.
    #   - `lst[L:]` returns a slice of the list from the element at index `L` to the end of the list.
    #
    #Given that `L` can be any non-negative integer up to the length of `lst`, the slices returned can vary as follows:
    #- If `L = 0`, `lst[:L]` will be an empty list `[]`, and `lst[L:]` will be the entire list `lst`.
    #- If `L = len(lst)`, `lst[:L]` will be the entire list `lst`, and `lst[L:]` will be an empty list `[]`.
    #- For any `L` where `0 < L < len(lst)`, the list will be split into two non-empty parts at index `L`.
    #
    #**Output State**: **The program returns two lists: the first list contains elements from the start of `lst` up to but not including the element at index `L`, and the second list contains elements from index `L` to the end of `lst`.**
#Overall this is what the function does:The function splits the input list into two parts at the specified index and returns these two parts, with the first part containing elements from the start of the list up to but not including the element at the specified index, and the second part containing elements from the specified index to the end of the list.

