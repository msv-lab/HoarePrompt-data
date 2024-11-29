#State of the program right berfore the function call: T is an integer between 1 and 100, n is an integer between 1 and 100,000, and x is an integer in the range [-10^9, 10^9]. The string s consists of characters '0' and '1' and has a length of n. The sum of all n across test cases does not exceed 100,000.
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
        
    #State of the program after the  for loop has been executed: `T` is between 1 and 100, `results` is a list containing the output of the computation for each iteration of the loop based on the values of `n`, `x`, and the string `s`, `index` is equal to `3 * T + 1`, `balance` is calculated as the difference between the counts of '0's and '1's in `s` during the last iteration, `prefix_balances` is a list of length `n + 1` containing cumulative balances for the last processed string `s`. If `balance` is 0 and `x` is present in `prefix_balances`, `results` includes `-1` for that iteration; otherwise, it includes `0`. If `balance` is not equal to 0, `count` is the total number of valid values in `prefix_balances` that satisfy the conditions based on `x` and `balance`.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `T` is between 1 and 100, `results` contains `T` elements, `index` is `3 * T + T`, `balance` is calculated based on the counts of '0's and '1's in `s` from the last iteration, `prefix_balances` is a list of length `n + 1`, and all elements in `results` have been printed.
#Overall this is what the function does:The function reads input values for multiple test cases, each consisting of an integer `n`, an integer `x`, and a binary string `s`. It calculates the balance of zeros and ones in `s`, and based on this balance and the value of `x`, it determines how many valid balances can be achieved. If the balance is zero and `x` exists in the calculated prefix balances, it appends -1 to the results; otherwise, it appends 0. If the balance is non-zero, it counts how many prefix balances satisfy the condition that `(x - balance) % balance == 0` and are non-negative. Finally, it prints the results for all test cases. The function does not accept parameters directly but processes input from the standard input.

