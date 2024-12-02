#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, n is an integer such that 1 <= n <= 10^5, x is an integer such that -10^9 <= x <= 10^9, and s is a binary string of length n consisting of characters '0' and '1'. The total sum of n across all test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: `T` is the initial number of test cases, `index` is equal to 1 + 3 * T, `results` is a list containing the results from processing each test case based on the binary strings and their balances.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: if T is greater than 0, `T` is the initial number of test cases, `index` is equal to `1 + 3 * T`, `results` is a list containing results from processing each test case, and `result` is in an undefined state after all results have been printed; if T is 0, `T` is 0, `index` is 1, and `results` is an empty list.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a binary string and performs calculations based on the balance of '0's and '1's in the string. It determines if the target value `x` can be reached using a certain number of transformations based on the computed balance and returns the count of valid transformations for each case. If the total balance is zero and `x` is found in the prefix balances, it returns -1; otherwise, it returns 0. If the balance is not zero, it calculates how many transformations can reach `x` and returns that count. The function does not accept parameters and directly prints results for all test cases.

