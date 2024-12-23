# Read the number of participants
n = int(input())

# Initialize a list to store the ratings before and after the round
ratings = []

# Flag to determine if the round is rated
is_rated = False

# Flag to determine if the round is unrated
is_unrated = False

# Read the ratings before and after the round for each participant
for _ in range(n):
    a, b = map(int, input().split())
    ratings.append((a, b))
    if a != b:
        is_rated = True

# If the round is not rated, check for unrated condition
if not is_rated:
    for i in range(1, n):
        if ratings[i-1][0] < ratings[i][0]:
            is_unrated = True
            break

# Determine the output based on the flags
if is_rated:
    print("rated")
elif is_unrated:
    print("unrated")
else:
    print("maybe")
