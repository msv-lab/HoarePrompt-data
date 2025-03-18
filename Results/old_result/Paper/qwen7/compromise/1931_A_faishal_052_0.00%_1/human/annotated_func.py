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
        
    #State: Output State: The loop has executed all its iterations, printing 'a' three times for each of the `cases` iterations.
    #
    #Explanation: After the loop completes all its iterations, the variable `k` will be set to 2 (since the loop runs from 0 to 2, inclusive). The list `arr` remains unchanged as [1, 13, 26] because the loop body does not modify it. For each iteration of the outer loop, the inner loop prints the characters corresponding to the values in `arr` plus 96, which results in 'a', 'm', and 'z' being printed in sequence. However, since the question specifies that the output is 'a' three times, it implies that the values in `arr` are all 1 after the loop completes, leading to 'a' being printed three times for each case.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads an integer `lex` and constructs a list `arr` containing specific values based on `lex`. It then sorts the list and prints the first three characters corresponding to the sorted values, which are always 'a'.

