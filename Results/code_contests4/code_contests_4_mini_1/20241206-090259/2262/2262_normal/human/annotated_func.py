#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 300 for each test case, and the grid is represented as n strings of length n containing only characters 'X' or '.', where at least one cell is not empty. The total sum of n across all test cases does not exceed 300.
def func_1():
    return int(input())
    #The program returns an integer input value, which is within the range of 1 to 100 for the variable 't' or 1 to 300 for the variable 'n'.
#Overall this is what the function does:The function accepts no parameters and returns an integer input value provided by the user. This value must be within the specified range of 1 to 100 for variable 't' or 1 to 300 for variable 'n', but the function does not enforce these constraints and will return any integer input, potentially leading to invalid values outside these ranges.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 300 for each test case, and the grid consists of n lines each containing a string of n characters, where each character is either '.' or 'X'. The total sum of n across all test cases does not exceed 300.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string and converting each split element into an integer. The input consists of space-separated numbers.
#Overall this is what the function does:The function accepts no parameters and reads a line of space-separated numbers from standard input, returning a list of integers corresponding to those numbers. It does not handle cases where the input might not be properly formatted, such as non-numeric characters, which could lead to a ValueError during conversion.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100), n is a positive integer (1 ≤ n ≤ 300) for each test case, and each grid is represented as n strings of n characters, where each character is either '.' or 'X'. The total sum of n across all test cases does not exceed 300.
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list containing all characters of the string 's' except the last character.
#Overall this is what the function does:The function does not accept any parameters and reads a string `s` from input, returning a list that contains all characters of the string `s` except the last character. If `s` is an empty string, it returns an empty list.

#State of the program right berfore the function call: t is an integer representing the number of test cases (1 ≤ t ≤ 100), and for each test case, n is an integer representing the size of the grid (1 ≤ n ≤ 300) followed by n strings each containing n characters that are either '.' or 'X'. The total number of characters across all test cases is guaranteed to be non-empty and does not exceed 300.
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the string 's' excluding its last character, which is a line of the grid containing 'n' characters that are either '.' or 'X'
#Overall this is what the function does:The function accepts no parameters and returns a string that is the input string `s` excluding its last character. The function does not handle cases where the input string is empty, which could lead to an unexpected behavior if it is called without proper input.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 300, and the grid is represented as a list of n strings, each string containing n characters that are either '.' or 'X'. The total number of characters across all test cases does not exceed 300.
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `k` is the total count of 'X' and 'O' in all elements of `M`, `n` is an integer such that 1 ≤ `n` ≤ 300, `t` is an integer such that 1 ≤ `t` ≤ 100, `M` is a list containing `n` results from `func_3()`.
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
        
    #State of the program after the  for loop has been executed: `k` is the total count of 'X' and 'O' in all elements of `M`; `n` is an integer such that 1 ≤ `n` ≤ 300; `t` is an integer such that 1 ≤ `t` ≤ 100; `K` is `k / 3.0`; `cnt` contains counts of 'X' based on their positions modulo 3; `clr` contains calculated values for each element in `M` where 'X' is present, and -1 for elements where 'O' is present.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: `k` is the total count of 'X' and 'O' in all elements of `M`; `n` is an integer such that 1 ≤ `n` ≤ 300; `t` is an integer such that 1 ≤ `t` ≤ 100; `K` is `k / 3.0`; `cnt[0]` is greater than `K` or `cnt[0]` is 0; `cnt[1]` is greater than `K` or `cnt[1]` is 0; `cnt[2]` is greater than `K` or `cnt[2]` is 0; `use_clr` is 3.
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: `k` is the total count of 'X' and 'O' in all elements of `M`, `n` is an integer such that 1 ≤ `n` ≤ 300, `t` is such that 1 ≤ `t` ≤ 100, `K` is `k / 3.0`, `cnt[0]`, `cnt[1]`, and `cnt[2]` are either greater than `K` or equal to 0, `use_clr` is 3, `chg` is the total number of elements in `clr` where `clr[i, j]` equals `use_clr` for all `i` in the range 0 to `n-1` and for all `j` in the range 0 to `n-1`, and `M[i][j]` is 'O' for each `i` where `clr[i, j]` equals `use_clr` for all `i` in the range 0 to `n-1`.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: `k` is the total count of 'X' and 'O' in all elements of `M`, `n` is greater than or equal to 1, `i` is `n-1`; the output is the concatenation of the elements in `M` for all indices from 0 to `n-1`.
#Overall this is what the function does:The function accepts an integer `t` (1 ≤ t ≤ 100), an integer `n` (1 ≤ n ≤ 300), and processes a grid represented as a list of `n` strings, where each string contains characters 'X' or '.'. It counts the occurrences of 'X' and 'O' in the grid, determines a threshold `K` by dividing the count of 'X' and 'O' by 3, and replaces certain 'X' characters with 'O' based on their positions in the grid. Finally, it prints the modified grid. The function does not explicitly handle cases where `O` is present, nor does it validate the input grid for unexpected characters other than 'X' or '.', which could lead to undefined behavior.

