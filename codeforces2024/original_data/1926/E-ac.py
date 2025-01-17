def calc(n: int, k: int) -> int:
    if k <= (n + 1) // 2:
        return k * 2 - 1
    return 2 * calc(n // 2, k - (n + 1) // 2)

def solve():
    n, k = map(int, input().split())
    print(calc(n, k))

def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()