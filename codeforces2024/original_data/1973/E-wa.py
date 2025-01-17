import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(count_valid_pairs(n, arr))

def count_valid_pairs(n, arr):
    # Create a hash set to store unique elements in the array
    nums = set(arr)
    
    # Initialize counter for valid pairs
    count = 0
    
    # Check all possible pairs of (l, r)
    for i in range(1, int(2 * n)):
        l = i
        r = i + 1
        
        # Check if current pair satisfies the condition
        while r <= 2 * n and sum(arr[l-1:r+1]) in nums:
            count += 1
            r += 1
            
        # Reset l to the previous value as we have checked all possible r for this l
        l -= 1
    
    return count
if __name__ == '__main__':
    main()