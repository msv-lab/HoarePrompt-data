#State of the program right berfore the function call: 
def func_1():
    return int(input())
    #The program returns an integer value obtained from user input
#Overall this is what the function does:The function func_1 does not accept any parameters and returns an integer value obtained from user input. It reads an integer value from the user input and returns it as the output.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, the grid is a list of strings of length n where each string consists of characters '.' or 'X'.**
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by mapping the input values that are split by spaces to integers
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads input values separated by spaces, converts them to integers, and returns a list of these integers. The function does not handle cases where the input values are not integers.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the size of the grid, and the grid is represented by a 2D list of characters containing 'X' or '.' only.**
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list of characters from the grid, excluding the last character in each row
#Overall this is what the function does:The function `func_3` reads input from the user and returns a list of characters from the input string, excluding the last character. The function does not accept any parameters. The grid mentioned in the annotations is not utilized in the code, and there is no specific handling for test cases or grid sizes.

#State of the program right berfore the function call: n is a positive integer representing the size of the grid, and the grid is represented as a 2D list of characters where each character is either 'X' or '.'. The character 'O' does not appear in the grid for the easy version.
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns a string 's' excluding the last character
#Overall this is what the function does:The function `func_4` reads an input string, and then returns a new string that is the input string excluding the last character. The function does not accept any parameters, and it does not process a predefined grid as mentioned in the annotations. Instead, it simply operates on an input string.

#State of the program right berfore the function call: t is a positive integer. n is a positive integer such that 1 ≤ n ≤ 300. Each test case grid contains only the characters '.', 'X', and 'O'.**
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `k` is updated by the sum of occurrences of 'X' or 'O' in all elements of `M`, `n` is 0
    K = int(k / 3.0)
    clr = dict()
    cnt = [0] * 3
    for i in xrange(n):
        for j in xrange(n):
            if M[i][j] == 'X':
                clr[i, j] = (i + j) % 3
                cnt[(i + j) % 3] += 1
            else:
                clr[i, j] = -1
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `k` is updated by the sum of occurrences of 'X' or 'O' in all elements of `M`, `n` is at least 0, `K` is the integer division result of `k` divided by 3.0, `clr` contains key-value pairs where `clr[i, j]` is equal to `(i + j) % 3` for each valid `i` and `j`, `cnt` is a list of three elements where each element represents the count of occurrences of `(i + j) % 3` for each valid `i` and `j`.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: After all iterations of the loop, `k` is updated by the sum of occurrences of 'X' or 'O' in all elements of `M`, `n` is at least 0, `K` is the integer division result of `k` divided by 3.0, `clr` contains key-value pairs where `clr[i, j]` is equal to `(i + j) % 3` for each valid `i` and `j`, `cnt` is a list of three elements where each element represents the count of occurrences of `(i + j) % 3` for each valid `i` and `j`. The loop will execute until `use_clr` reaches 3 or the conditions related to `cnt` and `K` are met. After the loop finishes, `use_clr` will be the total number of times the loop executed.
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: Output State: After all iterations of the loop, `k` will be updated by the sum of occurrences of 'X' or 'O' in all elements of `M`, `n` will remain at least 0, `K` will be the integer division result of updated `k` divided by 3.0, `clr` will contain key-value pairs where `clr[i, j]` is equal to `(i + j) % 3` for each valid `i` and `j`, `cnt` will be a list of three elements where each element represents the count of occurrences of `(i + j) % 3` for each valid `i` and `j`, and `use_clr` will be the total number of times the loop executed.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `k` will be updated by the sum of occurrences of 'X' or 'O' in all elements of `M`, `n` will remain at least 0, `K` will be the integer division result of updated `k` divided by 3.0, `clr` will contain key-value pairs where `clr[i, j]` is equal to `(i + j) % 3` for each valid `i` and `j`, `cnt` will be a list of three elements where each element represents the count of occurrences of `(i + j) % 3` for each valid `i` and `j`, and `use_clr` will be the total number of times the loop executed. If `n` is less than or equal to 0, then `k` will be 0, `K` will be 0.0, `clr` will be an empty dictionary, `cnt` will be `[0, 0, 0]`, and `use_clr` will be 0.
#Overall this is what the function does:The function `func_5` initializes a matrix `M` based on the return value of functions `func_1` and `func_3`. It then calculates the sum of occurrences of 'X' or 'O' in the matrix elements. The function determines a color to use based on the sum and modifies the matrix elements accordingly. Finally, it prints the updated matrix. If the value of `n` is less than or equal to 0, the function will have specific default values for `k`, `K`, `clr`, `cnt`, and `use_clr`. The function does not accept any parameters and does not return any value.

