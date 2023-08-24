n = int(input())
prices = list(map(int, input().split()))

cheap = [] # list to store the cheap ice spheres
for i in range(1, n-1):
    if prices[i-1] > prices[i] < prices[i+1]: # check if current ice sphere is cheap
        cheap.append(prices[i])

# sort the cheap ice spheres in descending order
cheap.sort(reverse=True)

# reorder the ice spheres
reordered = [cheap[0]]
idx = 1
for i in range(n):
    if i % 2 == 0:
        reordered.append(prices[idx])
        idx += 1
    else:
        reordered.append(cheap[idx])
        idx += 1

print(len(cheap))
print(" ".join(map(str, reordered)))