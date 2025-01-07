#State of the program right berfore the function call: **Precondition**: **T is a positive integer. For each test case, n is a positive integer and x is an integer such that -10^9 <= x <= 10^9. s is a binary string of length n.**
def func_1():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        n = int(data[index])
        
        x = int(data[index + 1])
        
        s = data[index + 2]
        
        index += 3
        
        balance = s.count('0') - s.count('1')
        
        prefix_balances = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_balances[i] = prefix_balances[i - 1] + (1 if s[i - 1] == '0' else -1
                )
        
        if balance == 0:
            if x in prefix_balances:
                results.append(-1)
            else:
                results.append(0)
        else:
            count = 0
            for b in prefix_balances:
                if (x - b) % balance == 0 and (x - b) // balance >= 0:
                    count += 1
            results.append(count)
        
    #State of the program after the  for loop has been executed: After the loop executes, the `results` list will contain the count of how many times the conditions inside the loop's if statement were met for each iteration. The variables `data`, `T`, `index`, `n`, `x`, `s`, `balance`, `prefix_balances`, and `count` will be updated according to the loop code. The final values of these variables will depend on the data provided in `data` and the calculations performed within the loop.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `results` list will contain the count of how many times the conditions inside the loop's if statement were met for each iteration, `data`, `T`, `index`, `n`, `x`, `s`, `balance`, `prefix_balances`, and `count` variables will be updated during the loop, and each iteration of `results` will be printed.
#Overall this is what the function does:The function `func_1` reads input data that contains information about a certain number of test cases. For each test case, it processes the values of `n`, `x`, and `s` based on the provided constraints. It calculates certain conditions based on the input data and stores the count of how many times these conditions are met for each test case in a results list. Finally, it prints out each count stored in the results list. The function does not explicitly return any value but outputs the calculated counts for each test case.

