#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
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
        
    #State: Output State: `index` is 4, `t` is an integer obtained from `data[0]`, `n` is a positive integer such that 1 ≤ n ≤ 100, `s` is a string of length n containing only "U" and "D", `results` is a list where each element is either 'YES' or 'NO' based on whether the count of 'U' in the corresponding string `s` is odd or even.
    for result in results:
        print(result)
        
    #State: Output State: The loop iterates over each element in the `results` list and prints it. Since the `results` list contains elements that are either 'YES' or 'NO', the output will be a series of 'YES' and 'NO' printed to the console, one for each element in the `results` list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer t (1 ≤ t ≤ 100), a positive integer n (1 ≤ n ≤ 100), and a string s of length n containing only "U" and "D". For each test case, it counts the number of "U" characters in the string s. If the count is odd, it appends 'YES' to the results list; otherwise, it appends 'NO'. Finally, it prints each element in the results list, which consists of 'YES' or 'NO' indicating whether the count of "U" in each string s is odd or even.

