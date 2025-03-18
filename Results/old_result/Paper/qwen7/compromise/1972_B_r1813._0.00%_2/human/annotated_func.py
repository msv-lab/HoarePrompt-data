#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting of only "U" and "D".
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
        
    #State: Output State: `index` is 4, `t` is an integer obtained from `data[1]`, `n` is a positive integer such that 1 ≤ n ≤ 100, `s` is a string of length n consisting of only "U" and "D", `results` is a list where each element is either 'YES' or 'NO' based on whether the count of 'U' in `s` is odd or even for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: index
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer \( t \), another positive integer \( n \), and a string \( s \) of length \( n \) containing only 'U' and 'D'. For each test case, it counts the number of 'U' characters in \( s \). If the count is odd, it appends 'YES' to the results list; otherwise, it appends 'NO'. Finally, it prints each result in the list.

