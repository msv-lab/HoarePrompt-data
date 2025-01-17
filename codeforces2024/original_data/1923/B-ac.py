def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(map(int, input().split()))

    # Initialize the array to store "put all on right"
    put_all_on_right = [0] * (n + 1)

    # Populate the put_all_on_right array
    for i in range(n):
        put_all_on_right[abs(x[i])] += v[i]

    # Simulate the power depletion and recharging process
    my_power = k
    for i in range(1, n + 1):
        if my_power < put_all_on_right[i]:
            print("NO")
            return
        my_power -= put_all_on_right[i]
        my_power += k

    print("YES")


# Main function for handling multiple test cases    
def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
