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
        
    #State: Output State: `numCases` must be greater than 0, `i` is equal to `numCases`, `numInteger` is an input integer, `numbers` is an empty list, `suma` is the sum of the minimum values of all pairs of integers taken from the original list, with each pair's larger number decremented by 1 before adding to `suma`.
    #
    #After the loop executes all its iterations, `numCases` will be equal to the number of times the loop was executed, which is also the total number of cases processed. The variable `i` will be equal to `numCases` since the loop increments `i` in each iteration until it reaches `numCases`. The `numbers` list will be empty because all elements have been processed in pairs. The variable `suma` will hold the cumulative sum of the minimum values from each pair of integers that were popped from the list during the loop's execution, with the larger number of each pair decremented by 1 before being added to `suma`.
#Overall this is what the function does:The function processes multiple test cases. For each case, it reads an integer `numInteger` and a list of `2*numInteger` integers. It then sorts the list in ascending order, iterates through the list in pairs, and for each pair, it adds the smaller number to a cumulative sum `suma`. If the larger number in a pair is greater than the smaller one, it decrements the larger number by 1 before adding it to `suma`. Finally, it prints the cumulative sum `suma` for each test case.

