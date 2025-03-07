#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `numCases` must be greater than 0, `i` is equal to `numCases`, `numInteger` is an input integer, `numbers` is an empty list, `a` is the last element of the original list converted to an integer, `b` is the second last element of the original list converted to an integer, `suma` is the sum of the minimum values of all consecutive pairs from the original list.
    #
    #Explanation: After the loop has executed all its iterations, `numbers` will be an empty list since all elements have been processed in pairs. The variable `i` will be equal to `numCases` because the loop iterates `numCases` times. The variable `suma` will contain the sum of the minimum values of all consecutive pairs from the original list. The variables `a` and `b` will hold the values of the last two elements of the original list, respectively.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` and another integer `n`, followed by `2n` integers representing numbers on a whiteboard. It then sorts these numbers in ascending order and calculates the sum of the minimum values of all consecutive pairs from the sorted list. Finally, it prints the calculated sum for each test case.

