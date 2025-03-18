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
        
    #State: numCases is an input integer, t remains an integer such that 1 <= t <= 5000, n remains an integer such that 1 <= n <= 50, a remains a list of 2n integers where 1 <= a_i <= 10^7, and suma is the sum of the minimum of each pair of integers from the list of 2n integers for each of the numCases iterations.
#Overall this is what the function does:The function reads a series of test cases from the input. For each test case, it reads a list of 2n integers, sorts them in ascending order, and then iteratively pairs the integers, summing the smaller of each pair. The function prints the sum for each test case. The function does not return any value and does not modify the input parameters `t`, `n`, or `a`. After the function concludes, the input parameters remain unchanged, and the sums of the minimum pairs for each test case have been printed.

