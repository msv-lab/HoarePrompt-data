import sys
input = sys.stdin.readline

# Function to read a list of integers from input
F = lambda: [*map(int, input().split())]

# Process each test case
for _ in range(int(input())):
    N = int(input())  # Number of monsters
    A = [0] + F() + [0]  # Attack values with padding
    D = [0] + F() + [0]  # Defense values with padding

    # Initialize next and previous pointers for each monster
    NXT = [(i + 1) % (N + 1) for i in range(N + 1)]
    PRV = [N] + [i for i in range(N)]
    CHK = [(i + 1) for i in range(N)]  # List of monsters to check
    ANS = [0] * N  # Array to store the number of deaths per round

    # Simulate each round
    for round in range(N):
        cnt = 0  # Counter for the number of deaths in this round
        TMP = []  # Temporary list for next round's checks
        RMV = set()  # Set of monsters to be removed

        # Check each monster in the current round
        for a in CHK:
            prv, nxt = PRV[a], NXT[a]  # Get previous and next alive monsters
            # Check if the monster dies
            if D[a] < A[prv] + A[nxt]:
                cnt += 1  # Increment death count
                # Update TMP and RMV
                if TMP and TMP[-1] == a:
                    TMP.pop()
                if (not TMP or TMP[-1] != prv) and prv > 0 and prv not in RMV:
                    TMP.append(prv)
                if 1 <= nxt <= N:
                    TMP.append(nxt)
                RMV.add(a)

        # Update pointers for dead monsters
        for a in RMV:
            prv, nxt = PRV[a], NXT[a]
            PRV[nxt] = prv
            NXT[prv] = nxt

        # Update CHK for the next round
        CHK = TMP[:]
        ANS[round] = cnt  # Store the number of deaths in this round

        # If no monsters died, break early
        if cnt == 0:
            break

    # Output the result for the current test case
    print(*ANS)