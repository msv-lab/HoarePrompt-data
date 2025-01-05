def count_tuples(n, a):
    count = 0
    for y in range(n):
        if a[y] != 0:
            # For a fixed y, count all (x, z) pairs
            count += (y + 1) * (n - y)
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        results.append(count_tuples(n, a))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()