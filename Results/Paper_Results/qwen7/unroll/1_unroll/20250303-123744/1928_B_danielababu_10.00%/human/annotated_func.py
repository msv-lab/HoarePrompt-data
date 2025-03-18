#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all valid i. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func_1():
    return int(input())
    #The program returns an integer input provided by the user, which is within the range of 1 to 2 * 10^4 for the variable t.
#Overall this is what the function does:The function accepts no parameters and returns an integer input provided by the user, which must be within the range of 1 to 2 * 10^4.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 ⋅ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for each valid i.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing integers converted from a space-separated input string.
#Overall this is what the function does:The function reads a space-separated line of integers from standard input, converts each integer to a string, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9, representing the elements of the array a. It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers read from input, split by spaces. The first integer represents the number of test cases, followed by the elements of each test case's array.
#Overall this is what the function does:The function reads input from the user, processes it to extract the number of test cases and the arrays associated with each test case, and returns a list of lists where each sublist contains the elements of the array for each test case.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the length of the array a, followed by a space-separated list of n integers a_1, a_2, \ldots, a_n representing the elements of the array a. The values of t, n, and a_i satisfy the constraints provided in the problem description.
def func_4():
    return sorted(list(map(int, input().split())))
    #The program returns a sorted list of integers provided as input.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an array of integers, and returns a single sorted list containing all the integers from these arrays.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the length of the array a, followed by a space-separated list of n integers a_1, a_2, \ldots, a_n where 1 \leq n \leq 2 \cdot 10^5 and 1 \leq a_i \leq 10^9. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_5():
    return map(str, input().split())
    #The program returns a map object containing strings of the input values split from the input.
#Overall this is what the function does:The function processes input data for multiple test cases. Each test case starts with an integer `t` indicating the number of test cases, followed by an integer `n` and a list of `n` integers. The function splits the input into individual strings and returns a map object containing these strings.

#State of the program right berfore the function call: None of the variables in the provided function are relevant to the problem description. The function `func_6()` simply reads a line of input and returns a list of characters. This function does not take any parameters and does not contribute to solving the described problem.
def func_6():
    return list(input())
    #The program returns a list of characters entered by the user.
#Overall this is what the function does:The function `func_6()` reads a line of input from the user and returns it as a list of characters.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the length of the array a, followed by a line containing n integers a_1, a_2, \ldots, a_n representing the elements of the array a. The function `func_7` is not part of the solution and should not be considered.
def func_7():
    return sorted(list(map(str, input().split())))
    #The program returns a sorted list of strings, where each string represents an integer from the input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and then `n` integers from the input, storing them in an array. It then converts these integers to strings and returns a sorted list of these string representations.

#State of the program right berfore the function call: arr is a list of positive integers.
def func_8(arr):
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: Output State: `arr` is a list of positive integers; `ans` is a list where each element is the cumulative product of all elements in `arr` up to that index; `tem` is 1.
    return ans
    #The program returns a list 'ans' where each element is the cumulative product of all elements in 'arr' up to that index.
#Overall this is what the function does:The function accepts a list of positive integers and returns a new list where each element is the cumulative product of all elements in the input list up to that index.

#State of the program right berfore the function call: arr is a list of positive integers.
def func_9(arr):
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: Output State: `arr` is a list of positive integers; `ans` is a list containing the cumulative product of `arr` from the end to the start; `tem` is 1.
    return ans
    #The program returns the list 'ans' which contains the cumulative product of the list 'arr' from the end to the start
#Overall this is what the function does:The function accepts a list of positive integers `arr` and returns a new list `ans` where each element is the cumulative product of the elements in `arr` starting from the last element to the first.

