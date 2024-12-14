def func_1():
    import sys
    input = sys.stdin.read
    (h, n) = map(int, input().split())
    total_leaves = 2 ** h
    visited_count = 0
    path = bin(n - 1)[2:].zfill(h)
    current_level = 0
    current_node = 0
    for direction in path:
        visited_count += 1
        if direction == '0':
            current_node = 2 * current_node + 1
        else:
            current_node = 2 * current_node + 2
    print(visited_count)
if __name__ == '__main__':
    func_1()