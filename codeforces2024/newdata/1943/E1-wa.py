def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        m = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        frequencies = list(map(int, data[index:index + m + 1]))
        index += m + 1
        
        # Simulate the game
        mex = 0
        while mex <= m:
            if frequencies[mex] == 0:
                # If there are no more `mex` in the array, Alice can't pick it
                break
            # Alice picks one `mex`
            frequencies[mex] -= 1
            # Bob tries to remove up to `k` of the next `mex + 1`
            if mex + 1 <= m:
                if frequencies[mex + 1] <= k:
                    frequencies[mex + 1] = 0
                else:
                    frequencies[mex + 1] -= k
            # Increment mex to check the next possible MEX
            mex += 1
        
        results.append(str(mex))
    
    # Print all results for each test case
    print("\n".join(results))

if __name__ == "__main__":
    main()