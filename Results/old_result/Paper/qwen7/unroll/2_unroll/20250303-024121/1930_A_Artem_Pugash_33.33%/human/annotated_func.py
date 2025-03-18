#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: The sum of the minimum values of all pairs of integers for each test case.
#Overall this is what the function does:The function processes input data for up to 5000 test cases. For each test case, it reads an integer n and 2n integers, sorts these integers in ascending order, and then calculates the sum of the minimum values of all possible pairs of these integers. The function prints the sum for each test case.

