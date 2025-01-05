def calculate_interestingness(n, m, a, b):
    # Calculate the transparency coefficients for each cell
    transparency = [[a[i] + b[j] for j in range(m)] for i in range(n)]
    
    # Check if there are no pairs of neighboring cells with the same transparency coefficients
    interestingness = 0
    for i in range(n):
        for j in range(m):
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            has_same_neighbor = False
            for ni, nj in neighbors:
                if 0 <= ni < n and 0 <= nj < m and transparency[ni][nj] == transparency[i][j]:
                    has_same_neighbor = True
                    break
            if not has_same_neighbor:
                interestingness += 1
    
    return interestingness

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    
    a = [int(data[3 + i]) for i in range(n)]
    b = [int(data[3 + n + i]) for i in range(m)]
    
    results = []
    for i in range(q):
        t = int(data[3 + n + m + 1 + i * 4])
        l = int(data[3 + n + m + 2 + i * 4]) - 1
        r = int(data[3 + n + m + 3 + i * 4]) - 1
        x = int(data[3 + n + m + 4 + i * 4])
        
        if t == 1:
            for j in range(l, r + 1):
                a[j] += x
        else:
            for j in range(l, r + 1):
                b[j] += x
        
        results.append(calculate_interestingness(n, m, a, b))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()