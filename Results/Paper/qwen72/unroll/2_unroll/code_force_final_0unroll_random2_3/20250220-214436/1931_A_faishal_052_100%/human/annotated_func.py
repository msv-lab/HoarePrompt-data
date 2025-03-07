#State of the program right berfore the function call: The function should take an integer t as input, representing the number of test cases, followed by t integers n (3 ≤ n ≤ 78) representing the encoded words.
def func():
    cases = int(input())
    info = []
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex < 28:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            elif lex <= 78:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        info.append(arr)
        
    #State: Output State: `cases` is an input integer representing the number of test cases, `n` is still an integer in the range 3 to 78 for each test case, `info` is a list containing `cases` sublists, where each sublist is sorted and contains three elements: two elements are either 1, 26, or 52 (depending on the initial value of `lex`), and the third element is the remaining value of `lex` after the loop has completed its iterations.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: The `cases` variable remains unchanged, `n` remains an integer in the range 3 to 78 for each test case, and `info` is a list containing `cases` sublists. Each sublist in `info` is sorted and contains three elements: two elements are either 1, 26, or 52 (depending on the initial value of `lex`), and the third element is the remaining value of `lex` after the loop has completed its iterations. Additionally, the loop prints a string for each sublist in `info`, where the string is composed of the characters corresponding to the ASCII values of the elements in the sublist (converted to lowercase letters by adding 96 to each element).
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases, and then for each test case, it reads an integer `n` (where 3 ≤ n ≤ 78). It processes each `n` to generate a sorted list of three integers, where the first two integers are either 1, 26, or 52 based on the initial value of `n`, and the third integer is the remaining value of `n` after the processing. The function then converts these integers to lowercase letters by adding 96 to each and prints the resulting string for each test case. The function does not return any value; it only prints the decoded strings.

