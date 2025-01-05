def process_queries(t, test_cases):
    results = []

    for case in test_cases:
        n, s, t, q, queries = case
        case_result = []

        for li, ri in queries:
            li -= 1
            a = list(s[li:ri])
            b = list(t[li:ri])
            k = ri - li

            while True:
                changes = 0
                for i in range(k - 2):
                    if a[i] == '0' and a[i + 2] == '0' and b[i + 1] == '1' and a[i + 1] == '0':
                        a[i + 1] = '1'
                        changes += 1
                    if b[i] == '1' and b[i + 2] == '1' and a[i + 1] == '0':
                        a[i + 1] = '1'
                        changes += 1
                if changes == 0:
                    break

            max_ones = a.count('1')
            case_result.append(max_ones)

        results.append(case_result)

    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    idx = 1
    test_cases = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        t = data[idx]
        idx += 1
        q = int(data[idx])
        idx += 1
        queries = []

        for __ in range(q):
            li, ri = map(int, data[idx:idx + 2])
            idx += 2
            queries.append((li, ri))

        test_cases.append((n, s, t, q, queries))

    results = process_queries(t, test_cases)

    output = []
    for result in results:
        output.append(" ".join(map(str, result)))

    sys.stdout.write("\n".join(output) + "\n")
