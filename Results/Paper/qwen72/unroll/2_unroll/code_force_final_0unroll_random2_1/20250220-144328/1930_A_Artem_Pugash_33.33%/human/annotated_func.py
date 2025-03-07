#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
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
        
    #State: `t` is an integer such that 1 <= t <= 5000, `n` is an integer such that 1 <= n <= 50, `a` is a list of 2n integers where 1 <= a_i <= 10^7, `numCases` is an input integer. After the loop, `numCases` is 0, `numbers` is an empty list, and `suma` is the sum of the minimum values of each pair of integers from the list `numbers` for each case.
#Overall this is what the function does:The function reads a series of test cases from the user input. For each test case, it reads a number of integers, sorts them in non-decreasing order, and then repeatedly pairs the integers, summing the smaller integer of each pair. The function prints the sum for each test case. After processing all test cases, the function terminates without returning any value. The final state of the program is that `numCases` is 0, `numbers` is an empty list, and `suma` is the sum of the minimum values of each pair of integers from the list `numbers` for each case.

