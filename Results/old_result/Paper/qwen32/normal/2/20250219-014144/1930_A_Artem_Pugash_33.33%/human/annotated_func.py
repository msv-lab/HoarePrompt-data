#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `numCases` is greater than or equal to 1, `i` has reached the value of `numCases`, `numInteger` holds the integer value from the last iteration's user input, `numbers` is [], `suma` is the sum of the minimum values of each pair of numbers that were originally in `numbers` for the last iteration. The loop has completed all its iterations and printed the `suma` for each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the minimum values of each pair of integers from the list and prints this sum.

