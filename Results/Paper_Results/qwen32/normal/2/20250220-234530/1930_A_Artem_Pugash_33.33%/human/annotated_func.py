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
        
    #State: i is equal to numCases, numbers is [], suma is the cumulative sum of the minimums of all pairs from all test cases, numInteger is the last input integer read, t remains unchanged, numCases remains unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `2n` integers. It calculates the sum of the minimum values of `n` pairs formed from the list of integers for each test case and prints the result for each test case.

