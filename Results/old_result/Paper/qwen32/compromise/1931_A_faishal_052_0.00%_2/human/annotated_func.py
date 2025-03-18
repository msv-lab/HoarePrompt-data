#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
def func():
    cases = int(input())
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex <= 26:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            else:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        for k in range(3):
            print(chr(arr[k] + 96), end='')
        
    #State: t is an integer such that 1 <= t <= 100, cases is an integer specifying the number of iterations, i is equal to cases, n is an integer such that 3 <= n <= 78, arr is the sorted list from the last iteration, lex is the final value after processing in the last iteration, j is 2, k is 3.
#Overall this is what the function does:The function processes a number of test cases, each with an integer input `lex`. For each test case, it calculates a sequence of three characters based on the value of `lex` and prints these characters. The characters are derived from the English alphabet, where values 1 through 26 correspond to 'a' through 'z', and values 27 through 52 would theoretically correspond to 'a' through 'z' again, but the function does not handle values above 52 correctly as per the given code. The final state of the program is that it has printed the results for all test cases.

