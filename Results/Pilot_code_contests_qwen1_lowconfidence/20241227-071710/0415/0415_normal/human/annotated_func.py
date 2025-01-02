#State of the program right berfore the function call: delta is a non-negative integer.
def func_1(delta):
    return [(int(i) + delta) for i in raw_input().split()]
    #The program returns a list of integers, each obtained by adding the value of delta to the corresponding integer input by the user
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `delta` and prompts the user to input a list of integers. It then returns a new list where each integer in the input list is incremented by the value of `delta`. This process covers all input values, including the case where the input list might be empty or contain non-integer values (though such cases would result in an error). If the input list contains non-integer values, the function will raise a ValueError.

