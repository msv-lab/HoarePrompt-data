T = int(input())
N = int(input())
monkeys_first_type = []
for _ in range(N):
    time_find_spot, time_produce_coconut = map(int, input().split())
    monkeys_first_type.append((time_find_spot, time_produce_coconut))

M = int(input())
monkeys_second_type = []
for _ in range(M):
    time_find_tool, time_open_coconut = map(int, input().split())
    monkeys_second_type.append((time_find_tool, time_open_coconut))