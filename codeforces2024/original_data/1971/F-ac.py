import math

def count_lattice_points(r):
    count = 0
    r_squared = r * r
    r_plus_1_squared = (r + 1) * (r + 1)
    
    for x in range(-r, r + 1):
        x_squared = x * x
        if x_squared < r_squared:
            # For x=0 to x=r-1
            y_min_sq = r_squared - x_squared
            y_max_sq = r_plus_1_squared - x_squared - 1
            if y_min_sq > y_max_sq:
                continue
            y_min = math.ceil(math.sqrt(y_min_sq)) if y_min_sq > 0 else 0
            y_max = math.floor(math.sqrt(y_max_sq))
            count += max(0, y_max - y_min + 1) * 2  # Positive and negative y
        else:
            # For x=r
            y_max_sq = r_plus_1_squared - x_squared - 1
            y_max = math.floor(math.sqrt(y_max_sq))
            count += (y_max * 2 + 1) if y_max >= 0 else 0
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        r = int(data[index])
        index += 1
        results.append(str(count_lattice_points(r)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()