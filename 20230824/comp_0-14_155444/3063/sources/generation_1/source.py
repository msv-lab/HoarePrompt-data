N = int(input())
debts = []
for _ in range(N):
    debts.append(list(map(int, input().split())))

total_debts = sum([debt[1] for debt in debts])  # Calculate the total amount of debts

vis = [False] * N  # Keep track of visited persons
min_money = float('inf')  # Initialize the minimum money needed with infinity

for i in range(N):
    if not vis[i]:
        money_needed = 0  # Initialize the money needed for each connected component
        
        # DFS to find all connected components
        stack = [i]
        while stack:
            person = stack.pop()
            vis[person] = True
            money_needed += debts[person][1]  # Add the debt owed by this person
            
            # Add the debts owed by the persons this person owes money to
            if not vis[debts[person][0]-1]:
                stack.append(debts[person][0]-1)
            
        min_money = min(min_money, money_needed)  # Update the minimum money needed

print(min_money)