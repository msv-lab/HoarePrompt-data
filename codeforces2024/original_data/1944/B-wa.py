def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        k = 2 * k  # Doubling k
        
        a = list(map(int, input().split()))
        occ = [0] * (n + 1)

        for x in a:
            occ[x] += 1
        
        g0, g1, g2 = [], [], []
        for i in range(1, n + 1):
            if occ[i] == 0:
                g0.append(i)
            elif occ[i] == 1:
                g1.append(i)
            else:
                g2.append(i)
        
        v = 0
        output = []
        # Handle g2 first
        for x in g2:
            if v < k:
                output.append(f"{x} {x}")
                v += 2
        
        # Handle g1 next
        for x in g1:
            if v < k:
                output.append(f"{x}")
                v += 1
        
        # Print the first line
        print(" ".join(output))
        
        # Reset and handle g0
        v = 0
        output = []
        for x in g0:
            if v < k:
                output.append(f"{x} {x}")
                v += 2
        
        # Handle g1 again
        for x in g1:
            if v < k:
                output.append(f"{x}")
                v += 1
        
        # Print the second line
        print(" ".join(output))

if __name__ == "__main__":
    main()
