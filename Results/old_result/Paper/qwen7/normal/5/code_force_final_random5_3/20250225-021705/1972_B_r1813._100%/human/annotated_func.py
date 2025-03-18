#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D" representing the initial state of the coins.
def func_1():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        
        s = data[index + 1]
        
        index += 2
        
        count_u = s.count('U')
        
        if count_u % 2 == 1:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The list `data` contains at least one positive integer as its first element, `t` is an integer representing the total number of iterations that have been executed, `n` is the integer at index `2 * t + 1` of `data`, `s` is the string at index `2 * t + 2` of `data`, `index` is `2 * t + 3`, `count_u` is the number of 'U's in the string `s`. After all iterations, `t` will be the total number of iterations executed, which is equal to the initial value of `t` from the first iteration. `n` will be the last integer processed, and `s` will be the last string processed. `index` will be `2 * t + 3`, indicating the position right after the last string processed. `count_u` will be the number of 'U's in the last processed string `s`.
    #
    #In simpler terms, after all iterations, `t` will be the total number of times the loop has run, `n` will be the last integer read from `data`, `s` will be the last string read from `data`, `index` will point to the position right after the last string, and `count_u` will be the number of 'U's in the last string `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, a positive integer `n`, and a string `s` of length `n` containing only "U" and "D". For each test case, it counts the number of 'U's in the string `s`. If the count of 'U's is odd, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, it outputs the total number of test cases processed (`t`), the last integer `n` read, the last string `s` read, and the count of 'U's in the last string `s`.

