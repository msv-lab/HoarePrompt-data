def max_sold_products(n, f, days):
    regular_sales = []
    potential_sales_increase = []

    for k, l in days:
        regular_sales.append(min(k, l))
        potential_sales_increase.append(min(2 * k, l) - min(k, l))

    total_sales = sum(regular_sales)
    potential_sales_increase.sort(reverse=True)

    # Take the top f increases to maximize sales
    total_sales += sum(potential_sales_increase[:f])

    return total_sales

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
f = int(data[1])
days = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n)]

# Get the result
result = max_sold_products(n, f, days)

# Print the result
print(result)
