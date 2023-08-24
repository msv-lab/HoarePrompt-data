n = int(input())
a = list(map(int, input().split()))

gis = []
max_gis = float('-inf')
gis.append(max_gis)

for i in range(1, n):
    if a[i] > max_gis:
        max_gis = a[i]
    gis.append(a[i])

gis = list(set(gis)) # Remove duplicates
gis.sort() # Sort the GIS in increasing order

print(len(gis))
print(" ".join(map(str, gis)))