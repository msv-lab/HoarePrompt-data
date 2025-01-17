import sys
from bisect import bisect_left

def read_input():
    return sys.stdin.readline().rstrip()

def main():
    num_test_cases = int(read_input())

    for _ in range(num_test_cases):
        num_elements, target_sum = map(int, read_input().split())
        elements = list(map(int, read_input().split()))

        # Calculate prefix sum
        prefix_sum = [0] * num_elements
        prefix_sum[-1] = elements[-1]
        for i in range(num_elements - 2, -1, -1):
            prefix_sum[i] = prefix_sum[i + 1] + elements[i]

        # Calculate minimum number of exclusions for each candidate
        result = []
        for i in range(num_elements):
            j = bisect_left(prefix_sum, target_sum + elements[i], lo=i + 1, hi=num_elements)
            result.append(max(0, j - i - 1))

        print(*result)

if __name__ == "__main__":
    main()