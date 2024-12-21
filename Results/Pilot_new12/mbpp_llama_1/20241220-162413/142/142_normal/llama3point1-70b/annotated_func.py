#State of the program right berfore the function call: lst is a list and element is any type of object that can be compared to the elements in lst.
def func_1(lst, element):
    return all(item == element for item in lst)
    #The program returns True if all elements in list 'lst' are equal to 'element', False otherwise
#Overall this is what the function does:The function checks if all elements in a given list are equal to a specified element, returning True if they are all equal and False otherwise, handling lists of any size, including empty lists, and accommodating elements of any comparable type, with no modification to the original list.

