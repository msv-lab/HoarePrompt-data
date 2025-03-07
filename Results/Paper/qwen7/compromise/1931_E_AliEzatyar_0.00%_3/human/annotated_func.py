#State of the program right berfore the function call: num is an integer where 1 ≤ num ≤ 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: The loop will continue to execute as long as there are still characters in `num` that are '0' from the end of the string. After all iterations, `counter` will hold the total count of '0's from the end of `num` until it encounters a non-zero digit. If `num` consists entirely of '0's, `counter` will equal the length of `num`. If `num` does not contain any '0's, `counter` will be 0. The variable `i` will be set to -1 after the loop ends, indicating that the loop has completed all possible iterations.
    #
    #In natural language: After the loop has executed all its iterations, the `counter` variable will hold the number of trailing zeros in the integer `num` (if `num` is represented as a string). The `i` variable will be -1, signifying the end of the loop.
    return counter
    #The program returns the count of trailing zeros in the string representation of `num`, and `i` is set to -1.
#Overall this is what the function does:Functionality: The function accepts an integer `num` within the range of 1 to 10^9. It counts the number of trailing zeros in the string representation of `num` and returns this count. Additionally, after the function executes, the variable `i` is set to -1.

