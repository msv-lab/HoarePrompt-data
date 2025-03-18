#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: Output State: `arr` is a list containing sorted elements starting with 1s followed by 26s, and ends with the value of `lex`, `k` is 2, `lex` is an integer.
    #
    #Explanation: After the loop executes all its iterations, the value of `k` will be 2, as the loop iterates three times and `k` ranges from 0 to 2. The list `arr` will contain elements that are initially set to 1s and 26s based on the conditions within the loop, and it will end with the final value of `lex`. The elements in `arr` are sorted, and the loop does not modify `lex` or `k` outside of its range. Therefore, the final state of `arr` will be a sorted list starting with 1s followed by 26s, and ending with the value of `lex`.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads an integer `lex` and constructs a list `arr` based on certain conditions. It then sorts `arr` and prints the first three elements of the sorted list as characters using their corresponding ASCII values adjusted by adding 96. The function does not return any value but prints the output for each test case.

