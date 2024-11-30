#State of the program right berfore the function call: n is a positive integer, x is an integer in the range from -10^9 to 10^9, and s is a binary string of length n.
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
        
    #State of the program after the  for loop has been executed: After the loop executes, `n`, `x`, `s`, `input`, `T`, `index`, `results`, `balance`, `prefix_balances` will be correctly updated based on the loop code. In the final state, the `prefix_balances` list will contain the cumulative sum of 1 if `s[i - 1]` is '0' and -1 otherwise. If `balance` equals 0, then the conditions inside the if statement will determine the values appended to `results`. If `balance` is not 0, the loop will iterate over `prefix_balances` to calculate the value of `count` to be appended to `results`.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, all variables `n`, `x`, `s`, `input`, `T`, `index`, `balance`, `results`, `prefix_balances`, `count` will retain their updated values based on the loop code. The loop will iterate over all elements in `results` and print each result stored in it.
#Overall this is what the function does:The function `func_1` reads input data, processes it according to defined constraints, and calculates results based on the given conditions. It handles cases where the balance of '0's and '1's in the binary string `s` is equal to 0 and when it's not. For the former case, it checks if a specific value `x` exists in the cumulative sum list `prefix_balances` and appends -1 if it does, or 0 if it doesn't. In the latter case, it iterates through `prefix_balances` to count the occurrences where a certain condition is met and stores the counts in the `results` list. Finally, it prints each result. The function does not explicitly return any value but performs the specified calculations and operations based on the input parameters.

