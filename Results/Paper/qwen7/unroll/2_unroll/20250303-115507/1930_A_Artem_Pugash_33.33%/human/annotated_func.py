#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: The sum of the minimum values of pairs of integers taken from each test case's sorted list of integers.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer n and 2n integers a_1, a_2, ..., a_{2n}. For each test case, it sorts the list of integers in ascending order, then iterates through the sorted list, taking pairs of integers, and sums up the minimum value of each pair. Finally, it prints the total sum for each test case.

