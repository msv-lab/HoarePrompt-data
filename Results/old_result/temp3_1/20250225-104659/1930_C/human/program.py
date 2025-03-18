for _ in range(int(input())):
    func_1()

def func_1() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for i in range(n):
        st.add(arr[i] + i + 1)
    print(*sorted(st, reverse=True))

