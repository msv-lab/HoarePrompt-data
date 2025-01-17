from collections import defaultdict

def manhattan_triangle():
    # Read input
    num_cases = int(input())
    for _ in range(num_cases):
        n, d = map(int, input().split())

        # Store points in a dictionary
        points_dict = {}
        for idx in range(1, n+1):
            x, y = map(int, input().split())
            points_dict[idx] = (x, y)

        # Initialize result
        res = [0, 0, 0]

        # Group points into four categories
        dx_plus_d = defaultdict(list)
        dx_minus_d = defaultdict(list)
        dy_plus_d = defaultdict(list)
        dy_minus_d = defaultdict(list)

        for idx, (x, y) in points_dict.items():
            dx_plus_d[x + d//2].append(idx)
            dx_minus_d[x - d//2].append(idx)
            dy_plus_d[y + d//2].append(idx)
            dy_minus_d[y - d//2].append(idx)

        # Check every possible pair of points
        for x in dx_plus_d:
            if x in dx_minus_d:
                for p1 in dx_plus_d[x]:
                    for p2 in dx_minus_d[x]:
                        for p3 in points_dict:
                            if p3 != p1 and p3 != p2:
                                x3, y3 = points_dict[p3]
                                if abs(x3 - points_dict[p1][0]) == d // 2 and abs(y3 - points_dict[p1][1]) == d // 2:
                                    res = [p1, p2, p3]
                                    break
                        if res[0] != 0:
                            break
                    if res[0] != 0:
                        break
                if res[0] != 0:
                    break

        for y in dy_plus_d:
            if y in dy_minus_d:
                for p1 in dy_plus_d[y]:
                    for p2 in dy_minus_d[y]:
                        for p3 in points_dict:
                            if p3 != p1 and p3 != p2:
                                x3, y3 = points_dict[p3]
                                if abs(x3 - points_dict[p1][0]) == d // 2 and abs(y3 - points_dict[p1][1]) == d // 2:
                                    res = [p1, p2, p3]
                                    break
                        if res[0] != 0:
                            break
                    if res[0] != 0:
                        break
                if res[0] != 0:
                    break

        print(*res)


if __name__ == "__main__":
    manhattan_triangle()