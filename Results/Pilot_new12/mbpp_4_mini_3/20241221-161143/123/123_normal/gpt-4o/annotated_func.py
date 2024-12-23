#State of the program right berfore the function call: lst is a list of any elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple consisting of two elements: the first element is the sublist of 'lst' from the start to L (exclusive), and the second element is the sublist of 'lst' from L to the end. 'L' is a non-negative integer such that 0 <= L <= len(lst).
#Overall this is what the function does:The function `func_1` accepts a list `lst` and a non-negative integer `L`, where `0 <= L <= len(lst)`. It returns a tuple containing two sublists: the first sublist is made up of the elements in `lst` from the beginning to index `L` (exclusive), and the second sublist consists of the elements from index `L` to the end of `lst`. The function correctly handles cases where `L` is `0`, resulting in the first sublist being empty, or when `L` is equal to the length of `lst`, resulting in the second sublist being empty. The function does not perform any error handling for invalid values of `L`, but these are already guaranteed by the provided conditions.

