n = int(input())
a = list(map(int, input().split()))

gis = []
max_gis = a[0]
gis.append(max_gis)

for i in range(1, n):
    if a[i] > max_gis:
        max_gis = a[i]
        gis.append(max_gis)
    elif a[i] == max_gis:
        continue
    else:
        break

print(len(gis))
print(" ".join(str(x) for x in gis))