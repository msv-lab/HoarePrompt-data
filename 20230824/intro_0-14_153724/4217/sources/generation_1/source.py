
# Read N and M from input
N, M = map(int, input().split())

# Create a list to store the count of each food
food_count = [0] * M

# Iterate through each person
for _ in range(N):
    # Read the list of foods liked by the person
    person = list(map(int, input().split()))[1:]

    # Increment the count for each food liked by the person
    for food in person:
        food_count[food - 1] += 1

# Count the number of foods liked by all the N people
liked_by_all = sum(1 for count in food_count if count == N)

# Print the result
print(liked_by_all)
