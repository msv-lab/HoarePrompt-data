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
        
    #State: `t` remains an integer such that 1 <= t <= 5000, `n` remains an integer such that 1 <= n <= 50, `a` remains a list of 2n integers where 1 <= a_i <= 10^7, `numCases` is an input integer, and `suma` is the sum of the minimum values of pairs of integers from the input list for each case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n`, followed by a list of 2n integers. It then calculates the sum of the minimum values of each pair of integers from the list and prints this sum. After processing all test cases, the function terminates. The function does not return any value, but it prints the result for each test case. The state of the program variables `t`, `n`, and `a` remains unchanged, as they are not modified within the function.

