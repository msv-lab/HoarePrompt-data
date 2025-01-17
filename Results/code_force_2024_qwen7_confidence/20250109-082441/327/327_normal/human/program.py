def count_possible_arrays(n):
    mod = 998244353
    result = []
    for k in range(1, (n-1)//2 + 1):
        # The number of possible arrays for a given k is the number of elements that can be left after the operation
        # Since the operation removes 2*k elements, the remaining elements are those that can be in the middle of the subsequence
        # For k, the number of possible middle elements is n - 2*k + 1
        possible_arrays = n - 2*k + 1
        result.append(possible_arrays % mod)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    test_cases = [int(data[i+1]) for i in range(t)]
    
    for n in test_cases:
        result = count_possible_arrays(n)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()