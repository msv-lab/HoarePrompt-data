import sys

def main():
    # Read the number of test cases
    t = int(input())
    for _ in range(t):
        # Read n and k for each test case
        n, k = map(int, input().split())
        
        # Initialize arrays for assigned integers and clique numbers
        a = [-1] * n
        c = [-1] * n
        
        # Initialize clique counter and starting index
        cnt = 0
        beg = 0
        
        # Process vertices in chunks
        while beg < n:
            # Determine the size of the current chunk
            k = min(k, n - beg)
            # Calculate half to help with integer assignment
            half = (k - 1) // 2
            
            # Assign integers and clique numbers for the current chunk
            for i in range(k):
                a[beg + i] = beg + (half - 1 - i)
                # Ensure the assigned integer is within bounds
                if a[beg + i] < beg:
                    a[beg + i] += k
                # Assign the current clique number
                c[beg + i] = cnt
            
            # Increment the clique counter
            cnt += 1
            # Move to the next chunk
            beg += k
        
        # Output the results for the current test case
        print(" ".join(str(x + 1) for x in a))
        print(cnt)
        print(" ".join(str(x + 1) for x in c))

if __name__ == "__main__":
    main()