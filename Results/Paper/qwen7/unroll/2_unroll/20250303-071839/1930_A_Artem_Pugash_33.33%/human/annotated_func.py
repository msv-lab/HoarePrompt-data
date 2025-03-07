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
        
    #State: The sum of the minimum values for each pair of sorted integers across all test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` indicating the number of pairs, followed by `2n` integers. It sorts these integers and then iterates through them in pairs, summing up the minimum value of each pair. Finally, it prints the total sum for all test cases.

