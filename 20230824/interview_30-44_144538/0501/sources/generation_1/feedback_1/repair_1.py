MOD = 1000000007

def get_sum(l, r):
    # Calculate the sum modulo MOD
    ans = (((r - l + 1) * (l + r)) // 2) % MOD
    
    return ans


# Read input values
l, r = map(int, input().split())

# Calculate and print the sum
print(get_sum(l, r))