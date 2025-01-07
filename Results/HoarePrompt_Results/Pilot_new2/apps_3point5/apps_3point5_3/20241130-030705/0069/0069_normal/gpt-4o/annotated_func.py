#State of the program right berfore the function call: $T$ is a positive integer. For each test case, $n$ is a positive integer, $x$ is an integer such that $-10^9 \le x \le 10^9$, and $s$ is a binary string of length $n$.**
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
        
    #State of the program after the  for loop has been executed: Output State: After all iterations of the loop, the program variables will be as follows: $T$ remains the first integer value from the `data` list. `n` will be the total number of iterations of the loop. `x` will be assigned the last integer value from the `data` list. `s` will be assigned the last binary string value from the `data` list. `data` will remain a list containing all input values. `index` will be the last index value after the loop finishes. `balance` will be the final difference between the count of '0's and '1's in the last binary string `s`. `prefix_balances` will be a list of length `n + 1` where `prefix_balances[i]` will be calculated based on the last binary string value `s`. If `balance` is equal to 0 at the end, `results` will contain -1 if the last integer `x` is in the `prefix_balances` list, otherwise, `results` will contain 0. If `balance` is not equal to 0 at the end, `count` will be the final count of the number of times the condition `(x - b) % balance == 0 and (x - b) // balance >= 0` is satisfied for all elements in the `prefix_balances` list and this value will be appended to the `results` list.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the program variables will be as follows: `T` remains the first integer value from the `data` list, `n` will be the total number of iterations of the loop, `x` will be assigned the last integer value from the `data` list, `s` will be assigned the last binary string value from the `data` list, `data` will remain a list containing all input values, `index` will be the last index value after the loop finishes, `balance` will be the final difference between the count of '0's and '1's in the last binary string `s`, `prefix_balances` will be a list of length `n + 1` where `prefix_balances[i]` will be calculated based on the last binary string value `s`, `results` will contain either -1 or 0 based on the conditions mentioned, and `count` will be the final count of satisfying the condition `(x - b) % balance == 0 and (x - b) // balance >= 0` for all elements in the `prefix_balances` list.
#Overall this is what the function does:The function `func_1` reads input data consisting of a positive integer $T$, followed by $T$ sets of data containing a positive integer $n$, an integer $x$, and a binary string $s$ of length $n$. It then processes each set of data to calculate certain conditions based on the input values. After processing all sets, it prints the results. The function does not explicitly return a value, but it performs calculations and prints results based on the input data.

