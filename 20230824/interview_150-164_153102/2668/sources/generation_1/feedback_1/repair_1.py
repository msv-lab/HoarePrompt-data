jacket_cost, sock_cost, money = map(int, input().split())

# calculate the remaining money after buying the jacket
remaining_money = money - jacket_cost

# calculate the maximum number of socks that can be bought with the remaining money
max_socks = remaining_money // sock_cost

if max_socks >= 1 or (max_socks == 0 and money % sock_cost == 0 and money >= 2 * sock_cost):
    print("Lucky Chef")
else:
    print("Unlucky Chef")