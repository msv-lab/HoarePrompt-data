(x, y, z) = map(int, input().split())
min_upvotes = x
max_upvotes = x + z
min_downvotes = y
max_downvotes = y + z
if max_upvotes < min_downvotes:
    print('-')
elif max_downvotes < min_upvotes:
    print('+')
else:
    print('?')