n = int(input())
debts = []
for _ in range(n):
    debts.append(list(map(int, input().split())))

total_debts = sum([debt[1] for debt in debts])  # Calculate the total amount of debts

vis = [False] * n  # Keep track of visited persons
min_money = 0  # Initialize the minimum money needed as 0

for i in range(n):
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

                money_needed -= debts[debts[person][0]-1][1]  # Subtract the money received from others

        min_money = min(min_money, money_needed)  # Update the minimum money needed

min_money = max(min_money, total_debts)  # Take the maximum of minimum money needed and total debts

print(min_money)