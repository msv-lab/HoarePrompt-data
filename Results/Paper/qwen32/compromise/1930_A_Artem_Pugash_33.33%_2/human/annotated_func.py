#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `numCases` is an integer read from input representing the number of test cases, `n` is an integer such that 1 ≤ n ≤ 50, `a` is the integer value of the last element processed if `n` is odd, otherwise the second-to-last element processed for the last test case, `numInteger` is an integer read from input for the last test case, `numbers` is an empty list, `suma` is the sum of the minimum values from each pair of numbers originally in the list for the last test case, `i` is `numCases - 1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the minimum values from each pair of numbers in the list and prints this sum.

