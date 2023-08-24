import math

def max_delivery_time(customers):
    max_delivery_time = 0

    # calculate the maximum distance between any two customers for each company
    for i in range(len(customers)):
        for j in range(i+1, len(customers)):
            distance = abs(customers[i][0] - customers[j][0]) + abs(customers[i][1] - customers[j][1])
            max_delivery_time = max(max_delivery_time, distance)

    return max_delivery_time

# read the number of customers
n = int(input())

# read the coordinates of the customers
customers = []
for _ in range(n):
    x, y = map(int, input().split())
    customers.append((x, y))

# calculate the maximum delivery time
result = max_delivery_time(customers)

# print the result
print(result)