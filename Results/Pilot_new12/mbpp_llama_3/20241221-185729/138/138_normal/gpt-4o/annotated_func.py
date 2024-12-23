#State of the program right berfore the function call: arr is a list of elements, and element is a value that can be compared with the elements in arr.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: arr is a list of elements, element is a comparable value, the function returns True and the index if element is found in arr; otherwise, it implicitly returns None, with index and value taking on the values of the last element in arr if the loop completes without finding a match.
    return False, -1
    #The program returns False and -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` and a comparable `element` as input, and returns a tuple containing a boolean indicating whether the `element` is found in `arr`, and an integer representing the index of the `element` if found, or -1 if not found. The function performs a linear search through the list `arr` and returns as soon as it finds a match, with the index of the first occurrence of the `element`. If the `element` is not found in the list, the function returns `False` and -1. The function handles edge cases such as an empty list, a list with a single element, and a list with duplicate elements, always returning the index of the first occurrence of the `element` if found.

