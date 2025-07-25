#State of the program right berfore the function call: arr is a list containing two sublists, where the first sublist represents the array a of length n (1 ≤ n ≤ 100) with elements (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9), and the second sublist represents the array b of length n (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9). Both a and b are sorted in non-decreasing order.
def func_1(arr):
    return sorted(arr, reverse=True)
    #The program returns a list where the sublists are sorted in reverse order, meaning the sublist that was originally second (b) now comes first, followed by the sublist that was originally first (a). Both sublists a and b remain sorted in their non-decreasing order.
#Overall this is what the function does:The function `func_1` accepts a list `arr` containing two sublists, both of which are sorted in non-decreasing order. It returns a new list where the entire `arr` is sorted in reverse order, meaning the elements of the sublists are not altered, but the order of the sublists is reversed. The sublist that was originally second (b) now comes first, followed by the sublist that was originally first (a). Both sublists remain sorted in their non-decreasing order.

