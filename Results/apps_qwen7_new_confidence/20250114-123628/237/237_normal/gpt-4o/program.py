s = input().strip()

# Count the number of pearls ('o') and links ('-') in the string
pearl_count = s.count('o')
link_count = s.count('-')

# If there are no pearls or only one pearl, we can always make the necklace valid
if pearl_count == 0 or pearl_count == 1:
    print("YES")
else:
    # Check if the links can be evenly distributed among the pearls
    if link_count % pearl_count == 0:
        print("YES")
    else:
        print("NO")
