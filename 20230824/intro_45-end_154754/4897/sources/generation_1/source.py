def choose_sprinters():
    n = int(input())

    # Read the information about the runners
    runners = []
    for _ in range(n):
        name, first_leg, other_leg = input().split()
        first_leg = float(first_leg)
        other_leg = float(other_leg)
        runners.append((name, first_leg, other_leg))

    # Sort the runners by their fastest time for any leg
    runners.sort(key=lambda x: x[2])

    # Create a list to store the chosen sprinters
    selected_sprinters = []

    # Select the sprinters for each leg
    for i in range(4):
        selected_sprinters.append((runners[i][0], runners[i][i+1]))

    # Calculate the total time for the team
    total_time = sum(t for _, t in selected_sprinters)

    # Print the total time and the names of the selected sprinters
    print("{:.2f}".format(total_time))
    for runner in selected_sprinters:
        print(runner[0])


choose_sprinters()