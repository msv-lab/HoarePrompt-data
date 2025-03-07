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
        
    #State: Output State: `data` is a list of strings obtained from splitting the input string, `t` is an integer obtained from `data[2]`, `n` is a positive integer such that 1 ≤ n ≤ 100, `s` is a string of length n containing only "U" and "D", `index` is `2 + 2 * t`, `results` is a list of 'YES' and 'NO' strings determined by whether the count of 'U' in each corresponding `s` string is odd or even.
    for result in results:
        print(result)
        
    #State: The loop prints each string in the `results` list, which contains 'YES' or 'NO' based on whether the count of 'U' in each corresponding `s` string is odd or even.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` (1 ≤ t ≤ 100), a positive integer `n` (1 ≤ n ≤ 100), and a string `s` of length `n` containing only "U" and "D". For each test case, it counts the number of 'U' characters in the string `s`. If the count of 'U' is odd, it appends 'YES' to the results; otherwise, it appends 'NO'. Finally, it prints each result in the list.

