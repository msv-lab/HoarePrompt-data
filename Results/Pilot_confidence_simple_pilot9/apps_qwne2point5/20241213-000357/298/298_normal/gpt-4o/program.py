n, m, k = map(int, input().split())

# Calculate the area required for the triangle
area = n * m / k

# Check if the area is an integer
if area != int(area):
    print("NO")
else:
    area = int(area)
    # We find a way to create a triangle with this area
    if area == 0:
        print("NO")
    else:
        # We can set one point at (0, 0) and the others in a way to form the required area
        print("YES")
        print("0 0")
        if 2 * area <= n:
            print(f"{2 * area} 1")
            print(f"0 1")
        elif 2 * area <= m:
            print(f"1 {2 * area}")
            print(f"1 0")
        else:
            print(f"{n} {m // 2}")
            print(f"0 {m // 2}")
