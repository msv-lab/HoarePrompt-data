#State of the program right berfore the function call: cast is a function that can be applied to the elements of the input, and input().split() returns a list of strings.
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element in the list of strings obtained from `input().split()`. The `cast` function will be applied to each string in the list, converting them to the type specified by `cast`.
#Overall this is what the function does:The function `func_1` accepts a parameter `cast` and returns an iterator. This iterator applies the `cast` function to each element in the list of strings obtained from `input().split()`. The `cast` function converts each string in the list to the specified type. The function does not modify any external state and only returns the iterator.

