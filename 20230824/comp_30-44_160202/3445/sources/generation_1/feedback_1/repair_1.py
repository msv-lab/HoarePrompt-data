import math

def max_delivery_time(customers):
    max_delivery_time_1 = 0  # variable name changed to avoid confusion
    max_delivery_time_2 = 0

    # calculate the maximum distance in the x and y directions for each company
    for i in range(len(customers)):
        for j in range(i+1, len(customers)):
            distance_x = abs(customers[i][0] - customers[j][0])
            distance_y = abs(customers[i][1] - customers[j][1])
            
            # calculate the maximum delivery time for the first company
            max_delivery_time_1 = max(max_delivery_time_1, distance_x, distance_y)
            
            # calculate the maximum delivery time for the second company
            max_delivery_time_2 = max(max_delivery_time_2, distance_x, distance_y)

    return max(max_delivery_time_1, max_delivery_time_2)  # return the maximum of the two delivery times

# read the number of customers
n = int(input())

# read the coordinates of the customers
customers = []
for _ in range(n):
    x, y = map(int, input().split())
    customers.append((x, y))

# handle the case when one company has only a single customer
if n == 1:
    print(0)
else:
    # calculate the maximum delivery time
    result = max_delivery_time(customers)

    # print the result
    print(result)