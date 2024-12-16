#State of the program right berfore the function call: list1, list2, and list3 are lists of integers.
def func_1(list1, list2, list3):
    combined_list = list1 + list2 + list3
    sorted_list = sorted(combined_list)
    return sorted_list
    #The program returns sorted_list which is a sorted version of combined_list containing all elements from list1, list2, and list3 combined
#Overall this is what the function does:The function accepts three lists of integers, combines them into a single list, and returns a new list that contains all the elements sorted in ascending order.

