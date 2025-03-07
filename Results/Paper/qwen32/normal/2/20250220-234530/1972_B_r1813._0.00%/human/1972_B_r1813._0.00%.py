def solve_coin_game():
    import sys
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
        
        # Count the number of 'U' (face-up) coins
        num_up_coins = s.count('U')
        
        # Determine the winner based on the parity of the count
        if num_up_coins % 2 == 1:
            results.append("YES")
        else:
            results.append("NO")
    
    # Print all results
    for result in results:
        print(result)
 
# Uncomment the following line to run the function with standard input
# solve_coin_game()