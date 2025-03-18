#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
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
        
    #State: The printed values of `suma` for each of the `numCases` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of 2n integers. For each test case, it calculates the sum of the minimum pairs formed by sorting the list and then pairing the smallest available integers together. The result for each test case is printed.

