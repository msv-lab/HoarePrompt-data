#State of the program right berfore the function call: test_tup1 and test_tup2 are tuples.
def func_1(test_tup1, test_tup2):
    return tuple(set(test_tup1) & set(test_tup2))
    #The program returns a tuple containing elements that are present in both `test_tup1` and `test_tup2`
#Overall this is what the function does:The function accepts two parameters `test_tup1` and `test_tup2`, which are tuples, and returns a tuple containing the unique elements that are present in both tuples.

