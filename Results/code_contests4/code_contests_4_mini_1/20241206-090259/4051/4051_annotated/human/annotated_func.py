#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{14}.
def func_1():
    arr = list(map(int, raw_input().strip().split(' ')))
    return arr
    #The program returns the list of integers 'arr' obtained from the input
#Overall this is what the function does:The function accepts input from the user, processes it into a list of integers, and returns this list. It assumes that the input will be well-formed integers separated by spaces. However, since there are no checks for input validity, if the input is not correctly formatted, it could result in a ValueError or an empty list being returned.

