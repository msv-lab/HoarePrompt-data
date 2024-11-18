x, y, z = map(int, input().split())

# Calculate the minimum and maximum possible upvotes
min_upvotes = x
max_upvotes = x + z

# Calculate the minimum and maximum possible downvotes
min_downvotes = y
max_downvotes = y + z

if max_upvotes < min_downvotes:
    print("-")
elif max_downvotes < min_upvotes:
    print("+")
else:
    print("?")
