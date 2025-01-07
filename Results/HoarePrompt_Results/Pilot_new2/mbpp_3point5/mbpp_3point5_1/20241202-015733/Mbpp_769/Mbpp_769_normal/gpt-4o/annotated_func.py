#State of the program right berfore the function call: list1 and list2 are lists.**
def func_1(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff_elements = set1.symmetric_difference(set2)
    result_list = list(diff_elements)
    result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
    #The program returns a list containing the elements of diff_elements sorted based on their index in the concatenated list of list1 and list2
#Overall this is what the function does:The function accepts two lists, finds the symmetric difference between them, converts it to a list, sorts the unique elements based on their index in the concatenated form of the input lists, and returns the sorted list.

