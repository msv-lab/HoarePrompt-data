def solve():
    import sys
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
        
        # Calculate the total balance of the given string s
        balance = s.count('0') - s.count('1')
        
        # Generate prefix balances
        prefix_balances = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_balances[i] = prefix_balances[i - 1] + (1 if s[i - 1] == '0' else -1)
        
        if balance == 0:
            # If balance is 0, check if any prefix has the exact balance x
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
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
