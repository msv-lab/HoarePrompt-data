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
        
    #State: `t` is an integer where 1 ≤ t ≤ 5000, `numCases` is an integer where 1 ≤ numCases ≤ 5000, `i` is `numCases - 1`, `numInteger` is an input integer, `numbers` is an empty list, `suma` is the sum of the minimum values of each pair of integers removed from `numbers` for each test case.
#Overall this is what the function does:The function reads and processes multiple test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then sorts the list in ascending order and repeatedly removes pairs of integers, adding the smaller of the two to a running sum. After processing all pairs, it prints the sum. The function handles up to 5000 test cases, with each `n` ranging from 1 to 50 and each integer in the list ranging from 1 to 10^7. After the function concludes, the input has been fully processed, and the sums for each test case have been printed.

