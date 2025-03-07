#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 5000, `numCases` must be equal to `t`, `i` is `t - 1`, `numInteger` is an input integer, `numbers` is an empty list, `suma` is the sum of the minimum values of each pair of integers removed from `numbers` for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers. It then sorts these integers and calculates the sum of the minimum values of each consecutive pair of integers. Finally, it prints the sum for each test case. After processing all test cases, the function leaves `numbers` as an empty list and `suma` as the sum of the minimum values for the last test case.

