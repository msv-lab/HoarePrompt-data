#State of the program right berfore the function call: The function should accept an integer n as input where 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: The `info` list will contain `cases` sublists, each of which is a sorted list of three integers. Each sublist represents the positions of three lowercase Latin letters derived from the input `lex` value, with the positions adjusted according to the conditions in the loop. The `lex` value is used to determine the positions, and the loop ensures that the sum of the positions in each sublist equals the original `lex` value. The `cases` variable remains unchanged.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: Output State: The `info` list remains unchanged, containing `cases` sublists, each of which is a sorted list of three integers. The `cases` variable also remains unchanged. The loop prints a string for each sublist in `info`, where each string consists of three lowercase Latin letters corresponding to the positions in the sublist. The sum of the positions in each sublist equals the original `lex` value.
#Overall this is what the function does:The function reads an integer `cases` from the user, representing the number of test cases. For each test case, it reads another integer `lex` (3 ≤ lex ≤ 78) and calculates a sorted list of three integers that represent the positions of three lowercase Latin letters. The sum of these positions equals the original `lex` value. It then converts these positions into the corresponding lowercase letters and prints them. The function does not return any value. After the function concludes, the `info` list contains `cases` sublists, each a sorted list of three integers, and the `cases` variable remains unchanged.

