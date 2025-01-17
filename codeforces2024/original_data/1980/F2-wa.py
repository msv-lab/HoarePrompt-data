import math

def calculate_additional_area(fountain, n, m):
    r, c = fountain
    # Calculate the distance from the diagonal
    diagonal_distance = abs((r + c) - (n + 1))
    return max(diagonal_distance // 2, 0)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3

        alpha = (n * m + 1) // 2
        additional_areas = []

        for __ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            additional_areas.append(calculate_additional_area((r, c), n, m))

        results.append((alpha, additional_areas))

    for result in results:
        alpha, additional_areas = result
        print(alpha)
        print(' '.join(map(str, additional_areas)))

if __name__ == "__main__":
    main()