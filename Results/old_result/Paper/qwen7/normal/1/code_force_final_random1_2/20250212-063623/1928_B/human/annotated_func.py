#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
def func_1():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function accepts no parameters and returns an integer input by the user.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the length of the array a, followed by n integers representing the elements of the array a.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing integers converted from user input split by spaces. Each integer corresponds to an element in the array 'a' for each test case.
#Overall this is what the function does:The function processes user input for multiple test cases. For each test case, it reads a series of space-separated integers and returns a map object containing these integers. These integers represent the elements of an array 'a' for each respective test case.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the length of the array a, and a is a list of integers where each integer is between 1 and \(10^9\).
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by taking user input and splitting it, converting each element to an integer.
#Overall this is what the function does:The function processes user input by taking a line of space-separated integers, converts each integer to a list element, and returns this list.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 2 \cdot 10^4. For each test case, n is an integer representing the length of the array a, where 1 ≤ n ≤ 2 \cdot 10^5. a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_4():
    return sorted(list(map(int, input().split())))
    #The program returns a sorted list of integers provided as input, where each integer is between 1 and 10^9, and the number of integers is specified by 'n' for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` representing the number of test cases, followed by an integer `n` and a list `a` of `n` integers. It then returns a sorted list of the integers in `a`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the length of the array a, followed by n space-separated integers a_1, a_2, \ldots, a_n which are the elements of the array a.
def func_5():
    return map(str, input().split())
    #The program returns a map object containing strings of the input split by spaces.
#Overall this is what the function does:The function processes user input by splitting it into a map object containing strings. It accepts no direct parameters but reads input from the standard input stream, which should be in the format of multiple space-separated values. The function does not modify any external variables and returns a map object where each element is a string representation of the input values.

#State of the program right berfore the function call: The function does not take any parameters and it is not used in the context of solving the given problem. It returns a list of characters obtained from user input, which is irrelevant to the problem described.
def func_6():
    return list(input())
    #The program returns a list of characters entered by the user.
#Overall this is what the function does:The function does not accept any parameters and returns a list of characters entered by the user.

#State of the program right berfore the function call: The function does not take any parameters. The input is provided through standard input and consists of multiple test cases. Each test case starts with an integer t indicating the number of test cases. Following this, each test case is described with the first line containing an integer n indicating the length of the array a, followed by a line containing n integers representing the elements of the array a. The input format and constraints are as described in the problem statement.
def func_7():
    return sorted(list(map(str, input().split())))
    #The program returns a sorted list of strings, where each string is an element from the input array converted to a string.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case includes an integer indicating the length of an array followed by the array elements. It converts these elements to strings and returns a sorted list of these string elements.

#State of the program right berfore the function call: arr is a list of positive integers.
def func_8(arr):
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: Output State: `arr` is a list of positive integers, `i` is equal to `len(arr)`, `tem` is the product of all elements in `arr`, and `ans` is a list containing the cumulative products of all elements in `arr`.
    #
    #This means that after the loop has executed all its iterations, `i` will be equal to the length of the list `arr`. The variable `tem` will hold the product of all elements in `arr`. The list `ans` will contain the cumulative products of the elements in `arr` as `tem` was updated in each iteration.
    return ans
    #The program returns a list `ans` containing the cumulative products of all elements in `arr`
#Overall this is what the function does:The function accepts a list of positive integers and returns a new list containing the cumulative products of all elements in the input list. After executing the function, the returned list `ans` will contain the cumulative products, where each element at index `i` represents the product of all elements in the input list from index `0` to `i`.

#State of the program right berfore the function call: arr is a list of positive integers.
def func_9(arr):
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: Output State: `arr` is a list of positive integers, `i` is `-1`, `tem` is the product of all elements in `arr` when traversed from the last element to the first, `ans` is a list containing the cumulative product of elements of `arr` starting from the last element to the first, with each subsequent element being the product of all preceding elements.
    #
    #In simpler terms, `ans` will contain the cumulative product of elements of `arr` from the end to the beginning, where each element in `ans` is the product of all elements in `arr` that come after it in the original list.
    return ans
    #`ans` is a list containing the cumulative product of elements of `arr` from the end to the beginning, where each element in `ans` is the product of all elements in `arr` that come after it in the original list.
#Overall this is what the function does:The function accepts a list of positive integers `arr` and returns a new list `ans`. Each element in `ans` represents the product of all elements in `arr` that come after the corresponding element in `arr`, starting from the end of the list.

