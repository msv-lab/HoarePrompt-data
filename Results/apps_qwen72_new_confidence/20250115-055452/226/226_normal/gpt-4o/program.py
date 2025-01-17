candies = list(map(int, input().split()))

# Check all possible ways to split the candies into two equal parts
possible = (candies[0] + candies[1] == candies[2] + candies[3]) or \
           (candies[0] + candies[2] == candies[1] + candies[3]) or \
           (candies[0] + candies[3] == candies[1] + candies[2]) or \
           (candies[0] + candies[1] + candies[2] == candies[3]) or \
           (candies[0] + candies[1] + candies[3] == candies[2]) or \
           (candies[0] + candies[2] + candies[3] == candies[1]) or \
           (candies[1] + candies[2] + candies[3] == candies[0])

if possible:
    print("YES")
else:
    print("NO")
