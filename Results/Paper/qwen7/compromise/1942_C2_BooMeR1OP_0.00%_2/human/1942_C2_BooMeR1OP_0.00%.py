def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a = [num - 1 for num in a]  # Convert to 0-based indexing
 
    a.sort()
    present = set(a)  # Use a set for fast lookups
    ans = x - 2
 
    # Check the conditions for incrementing the answer
    for i in range(x):
        t1 = (a[i] + 1) % n
        t2 = (a[i] + 2) % n
        if t1 not in present and t2 in present:
            ans += 1
 
    # Calculate gaps
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        gap = next_elem - a[i] - 1
        if gap > 0:
            gaps.append(gap)
 
    # Process gaps
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
 
    print(ans)
 
# Main function to handle multiple test cases
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()