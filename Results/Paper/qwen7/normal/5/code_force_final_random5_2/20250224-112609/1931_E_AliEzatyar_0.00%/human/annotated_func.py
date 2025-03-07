#State of the program right berfore the function call: num is a list of integers, where each integer is between 1 and 10^9 inclusive, and the length of the list n satisfies 1 <= n <= 2 * 10^5. Additionally, the sum of n across all test cases does not exceed 2 * 10^5, and for each test case, an integer m is given such that 0 <= m <= 2 * 10^6.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: The value of `counter` will be equal to the number of consecutive '0's from the end of the list `num`. If `num` does not contain any '0' from the end, `counter` will be 0. If `num` ends with multiple '0's, `counter` will count all of them.
    #
    #This means that after the loop completes all its iterations, `counter` will hold the total count of '0's starting from the last element of `num` and moving backwards until a non-'0' element is encountered or the entire list is traversed.
    return counter
    #The program returns the count of consecutive '0's from the end of the list 'num'. If there are no '0's from the end, it returns 0. If there are multiple '0's from the end, it returns the total count of those '0's.
#Overall this is what the function does:The function accepts a list of integers `num` and returns the count of consecutive '0's from the end of the list. If the list does not end with any '0', it returns 0. If the list ends with one or more '0's, it returns the total count of those '0's.

