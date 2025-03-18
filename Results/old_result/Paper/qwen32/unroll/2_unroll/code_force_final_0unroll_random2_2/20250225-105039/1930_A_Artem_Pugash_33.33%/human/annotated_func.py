#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 50), indicating that there are 2n integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard. The number of test cases t is given at the beginning (1 ≤ t ≤ 5000).
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
        
    #State: numCases remains unchanged, numInteger holds the value of n from the last test case, numbers is an empty list, and suma holds the sum of the smaller numbers in each pair for the last test case (but this value is printed and not stored for all test cases).
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number `n` and `2n` integers. For each test case, it calculates the sum of the smaller number in each pair of integers and prints this sum.

