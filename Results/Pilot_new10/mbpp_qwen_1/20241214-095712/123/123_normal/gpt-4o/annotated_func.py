#State of the program right berfore the function call: lst is a list, and L is an integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #`lst[:L]` is the slice of `lst` up to index `L` and `lst[L:]` is the slice of `lst` starting from index `L`
#Overall this is what the function does:The function `func_1` accepts a list `lst` and an integer `L` such that `0 <= L <= len(lst)`, and returns a tuple containing two slices: `lst[:L]` (a slice of `lst` up to index `L`) and `lst[L:]` (a slice of `lst` starting from index `L`). This operation effectively splits the list into two parts based on the index `L`.

