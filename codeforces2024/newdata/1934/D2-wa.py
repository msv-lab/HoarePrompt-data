def play_game():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        # Determine if Alice should play first or second
        if bin(n).count('1') % 2 == 1:
            print('second')
        else:
            print('first')
            # Calculate the largest power of 2 less than n
            l = int(bin(n)[3:], 2)
            print(n ^ l, l)
        
        # Interaction loop
        while True:
            a, b = map(int, data[index:index+2])
            index += 2
            if a == b:
                break
            # Choose the next number based on the count of 1s
            n = b if bin(a).count('1') % 2 == 1 else a
            l = int(bin(n)[3:], 2)
            print(n ^ l, l)