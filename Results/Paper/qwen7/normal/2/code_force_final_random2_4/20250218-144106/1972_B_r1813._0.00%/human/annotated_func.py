#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D" representing the initial state of the coins.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        s = data[index]
        
        index += 1
        
        num_up_coins = s.count('U')
        
        if num_up_coins % 2 == 1:
            results.append('YES')
        else:
            results.append('NO')
        
    #State: Output State: `index` is 10, `t` is 3, `n` is the length of `data[8]`, `s` is `data[9]`, `data` is a list of strings obtained from splitting the input string, `results` is a list containing either 'YES' or 'NO' based on the count of 'U' in each `s`. If the count of 'U' in any `s` is odd, `results` will contain 'YES' for that iteration; otherwise, it will contain 'NO'. The loop has executed 3 times as specified, and `index` is now at 10, indicating that all iterations of the loop have been completed.
    #
    #In simpler terms, after the loop runs all its iterations, `index` will be 10, `t` will still be 3 (since it's not modified in the loop), `n` will be the length of the 9th element in `data`, `s` will be the 10th element in `data`, and `results` will contain 'YES' or 'NO' based on whether the count of 'U' in each string `s` is odd or even during the loop's iterations.
    for result in results:
        print(result)
        
    #State: The loop has completed all its iterations, `index` is 10, `t` is 3, `n` is the length of the 9th element in `data`, `s` is the 10th element in `data`, and `results` contains 'YES' or 'NO' based on whether the count of 'U' in each string `s` is odd or even during the loop's iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t`, a positive integer `n`, and a string `s` of length `n` containing only "U" and "D". For each test case, it counts the number of 'U' characters in the string `s`. If the count of 'U' is odd, it appends 'YES' to the results list; otherwise, it appends 'NO'. After processing all test cases, it prints the results one by one.

