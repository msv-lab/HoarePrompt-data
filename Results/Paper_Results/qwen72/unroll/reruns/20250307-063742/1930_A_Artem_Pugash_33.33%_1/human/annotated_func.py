#State of the program right berfore the function call: t is an integer where 1 <= t <= 5000, n is an integer where 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
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
        
    #State: t remains an integer where 1 <= t <= 5000, n remains an integer where 1 <= n <= 50, a remains a list of 2n integers where 1 <= a_i <= 10^7, numCases is an input integer, and the loop has printed the sum of the minimum of each pair of integers from the input for each of the numCases iterations.
#Overall this is what the function does:The function `func` reads an integer `numCases` from the input, indicating the number of test cases. For each test case, it reads an integer `numInteger` and a list of 2n integers from the input. It then sorts the list in ascending order, pairs the integers, and calculates the sum of the minimum value in each pair. The function prints this sum for each test case. The function does not return any value. After the function concludes, `numCases` is the number of test cases processed, and the sums of the minimum values of each pair for each test case have been printed.

