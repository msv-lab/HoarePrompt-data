def chess_for_three(test_cases):
    results = []

    for p1, p2, p3 in test_cases:
        # Check if scores are consistent
        total_points = p1 + p2 + p3
        if total_points % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue

        # Maximum number of draws
        max_draws = min(p1, p3 - p2) + min(p2, p3 - p1)
        results.append(max_draws)

    return results

# Input reading
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    test_cases = []

    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        test_cases.append((p1, p2, p3))

    # Calculate results
    results = chess_for_three(test_cases)

    # Output results
    for result in results:
        print(result)