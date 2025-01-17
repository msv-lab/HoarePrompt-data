n = int(input())
edges = []


def query_type_1(weights):
    print("?1" + " ".join(map(str, weights)))
    return int(input())


def query_type_2(a, b):
    print(f"?2{a} {b}")
    return int(input())


weights = [1] * (n - 1)
diameter = query_type_1(weights)


center_a = 1
for i in range(2, n):
    if query_type_2(i, center_a) == diameter:
        center_b = i
    elif query_type_2(i, center_b) == diameter:
        center_a = i


new_tree = [(center_a, center_b)]
for i in range(1, n + 1):
    if i != center_a and i != center_b:
        if query_type_2(i, center_a) > query_type_2(i, center_b):
            new_tree.append((center_a, i))
        else:
            new_tree.append((center_b, i))


print("!")
for edge in new_tree:
    print(f"{edge[0]} {edge[1]}")