def max_happiness(m, x, costs):
    # sort costs in descending order
    costs.sort(reverse=True)
    
    # initialize variables
    earnings = 0
    happiness = []
    
    # iterate through each month
    for i in range(1, m+1):
        # add salary to earnings
        earnings += x
        
        # try to purchase highest-cost item
        while costs and costs[-1] <= earnings:
            # subtract cost from earnings
            earnings -= costs[-1]
            
            # increment happiness count
            happiness.append(1)
            
            # remove item from costs
            costs.pop()
            
    return len(happiness)

# read input
t = int(input())
for _ in range(t):
    m, x = map(int, input().split())
    costs = list(map(int, input().split()))
    
    print(max_happiness(m, x, costs))