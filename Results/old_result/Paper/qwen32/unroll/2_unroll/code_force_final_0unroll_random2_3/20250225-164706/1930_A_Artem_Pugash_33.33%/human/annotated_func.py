#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and there are 2n integers a_1, a_2, ..., a_{2n} where each a_i is an integer such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000; `n` is an integer such that 1 ≤ n ≤ 50; `numCases` is an input integer representing the number of test cases.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the minimum pairs from the list by sorting the numbers and pairing them sequentially, then prints the result for each test case.

