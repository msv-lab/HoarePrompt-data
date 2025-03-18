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
        
    #State: Output State: `numCases` is greater than or equal to the total number of iterations, `i` is `numCases`, `numInteger` is an input integer, `numbers` is an empty list, `suma` is the sum of the minimum values of all pairs of elements from the original `numbers` list.
    #
    #Explanation: After all iterations of the loop have finished, `numbers` will be an empty list because each pair of elements has been processed exactly once. The variable `suma` will contain the sum of the minimum values from each pair of consecutive elements in the original `numbers` list. The value of `i` will be equal to `numCases`, as the loop runs for each case specified by `numCases`. The value of `numInteger` remains unchanged as it was input before the loop started and is not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer t and 2n integers a_1, a_2, ..., a_{2n}. It then sorts these integers in ascending order, iterates through them in pairs, calculates the sum of the minimum values from each pair, and prints the total sum. After processing all test cases, the function outputs the sum for each case.

