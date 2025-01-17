import math
import sys

def ask_query(l, r):
    print(f"? {l} {r}")
    sys.stdout.flush()
    x = int(input())
    return x

def mark_absent(a):
    print(f"! {a}")
    sys.stdout.flush()
    y = int(input())
    return y

def solve_test_case(n):
    max_queries = math.ceil(math.log(n, 1.116)) - 1
    queries_used = 0
    possible_absent = set(range(1, n+1))

    while queries_used < max_queries and len(possible_absent) > 2:
        mid = (min(possible_absent) + max(possible_absent)) // 2
        x = ask_query(min(possible_absent), mid)
        if x == mid - min(possible_absent) + 1:
            possible_absent = set(range(mid+1, max(possible_absent)+1))
        else:
            possible_absent = set(range(min(possible_absent), mid+1))
        queries_used += 1

    if len(possible_absent) == 1:
        a = next(iter(possible_absent))
        if mark_absent(a) == 1:
            return True
    else:
        a1, a2 = possible_absent
        if mark_absent(a1) == 1 or mark_absent(a2) == 1:
            return True

    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if solve_test_case(n):
            print("#")
            sys.stdout.flush()
        else:
            print("Failed to determine the absent student")
            sys.stdout.flush()

if __name__ == "__main__":
    main()