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
        index += 2

        a = list(map(int, data[index:index + n + m + 1]))
        index += n + m + 1

        b = list(map(int, data[index:index + n + m + 1]))
        index += n + m + 1

        # Combine and sort by abs(a[i] - b[i])
        combined = [(a[i], b[i]) for i in range(n + m + 1)]
        combined.sort(key=lambda x: abs(x[0] - x[1]))

        # Calculate initial team skills
        p_skill = sum(combined[i][0] for i in range(n))
        t_skill = sum(combined[i][1] for i in range(m))

        result = []
        for i in range(n + m + 1):
            new_p_skill = p_skill - combined[i][0]
            new_t_skill = t_skill - combined[i][1]

            if combined[i][0] > combined[i][1]:
                result.append(new_p_skill)
            else:
                result.append(new_t_skill)

        results.append(result)

    for res in results:
        print(" ".join(map(str, res)))

# Uncomment the next line to run the function if this script is executed directly
# main()