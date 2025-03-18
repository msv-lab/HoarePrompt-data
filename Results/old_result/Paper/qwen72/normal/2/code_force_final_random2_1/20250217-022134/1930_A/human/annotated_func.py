#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
def func():
    numCases = int(input())
    for i in range(numCases):
        numInteger = int(input())
        
        numbers = input().split()
        
        numbers.sort(reverse=False)
        
        suma = 0
        
        while numbers != []:
            a = int(numbers.pop(0))
            b = int(numbers.pop(0))
            suma += min(a, b)
        
        print(suma)
        
    #State: `t` is an integer where 1 ≤ t ≤ 5000, `numCases` is equal to the initial value of `numCases`, `i` is equal to `numCases`, `numInteger` is an input integer, `numbers` is an empty list, `suma` is the sum of the minimum values of each pair of integers taken from the original `numbers` list until the list is empty for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer `n` followed by a list of 2n integers. The function calculates the sum of the minimum values of each pair of integers from the list and prints this sum for each test case. After processing all test cases, the function terminates, leaving the input variables in their final processed states. Specifically, `numCases` remains equal to the initial number of test cases, `i` is equal to `numCases`, `numInteger` is the last input integer read, `numbers` is an empty list, and `suma` is the sum of the minimum values of each pair of integers for the last test case.

