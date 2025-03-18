#State of the program right berfore the function call: list1 and list2 are lists of any data type.**
def func_1(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff_elements = set1.symmetric_difference(set2)
    result_list = list(diff_elements)
    result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
    #The program returns a list containing elements that are in either `list1` or `list2` but not in both, sorted based on their index in the combined list of `list1` and `list2`.
#Overall this is what the function does:The function func_1 accepts two lists, list1 and list2, converts them into sets, finds the symmetric difference between the sets, converts the result back to a list, and sorts the list based on the index of elements in the combined list of list1 and list2. The function then returns this sorted list of elements that are present in either list1 or list2 but not in both.

