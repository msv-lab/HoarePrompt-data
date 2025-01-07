def optimal_pie_distribution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    slices = list(map(int, data[1:]))
    
    # Initialize sums for Alice and Bob
    alice_sum = 0
    bob_sum = 0
    
    # Initialize who has the decider token
    # 0 means Bob has the token, 1 means Alice has the token
    decider = 0
    
    # Iterate over the slices
    for i in range(N):
        if decider == 0:
            # Bob decides
            if i < N - 1 and slices[i] < slices[i + 1]:
                # Give the slice to Alice and keep the decider token
                alice_sum += slices[i]
                decider = 0
            else:
                # Take the slice for Bob and pass the decider token to Alice
                bob_sum += slices[i]
                decider = 1
        else:
            # Alice decides
            if i < N - 1 and slices[i] < slices[i + 1]:
                # Give the slice to Bob and keep the decider token
                bob_sum += slices[i]
                decider = 1
            else:
                # Take the slice for Alice and pass the decider token to Bob
                alice_sum += slices[i]
                decider = 0
    
    print(alice_sum, bob_sum)

# Run the function
optimal_pie_distribution()
