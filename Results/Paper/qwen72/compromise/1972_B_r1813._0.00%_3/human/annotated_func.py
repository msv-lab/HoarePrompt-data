#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 100) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 100) and a string s of length n with characters "U" and "D" representing the state of the coins.
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
        
    #State: `index` is `2 * t + 1`. `results` is a list of strings, where each string is either 'YES' or 'NO' based on the condition `num_up_coins % 2 == 1` for each iteration.
    for result in results:
        print(result)
        
    #State: The `index` remains `2 * t + 1`, and the loop prints each string in the `results` list, which contains 'YES' or 'NO' based on the condition `num_up_coins % 2 == 1` for each iteration.
#Overall this is what the function does:The function reads input from `sys.stdin`, processes `t` test cases, where `t` is an integer (1 ≤ t ≤ 100), and each test case consists of an integer `n` (1 ≤ n ≤ 100) and a string `s` of length `n` containing characters "U" and "D". For each test case, it checks if the number of "U" characters in `s` is odd. If it is, the function appends 'YES' to a results list; otherwise, it appends 'NO'. After processing all test cases, the function prints each result in the results list. The function does not return any value.

