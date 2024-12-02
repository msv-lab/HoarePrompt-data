#State of the program right berfore the function call: tup is a tuple.**
def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        
        count += 1
        
    #State of the program after the  for loop has been executed: `tup` is a tuple with `n` elements, where `n` is the final value of `count`, `count` is the number of elements in the tuple `tup` before the first tuple element is encountered in the loop.
    return count
    #The program returns the count, which is the number of elements in the tuple `tup` before the first tuple element is encountered in the loop
#Overall this is what the function does:The function func_1 accepts a parameter `tup`, which is a tuple. It iterates through the elements in the tuple until it encounters the first tuple element and returns the count of elements before that element. If the tuple `tup` does not contain any tuple elements, the function returns the total number of elements in the tuple.

