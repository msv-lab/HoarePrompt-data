def find_valid_ks(n, x):
    def get_even_divisors(value):
        even_divisors = []
        for i in range(1, int(value**0.5) + 1):
            if value % i == 0:
                if i % 2 == 0:
                    even_divisors.append(i)
                if (value // i) % 2 == 0 and i != value // i:
                    even_divisors.append(value // i)
        return even_divisors

    # Calculate all even divisors of n - x and n + x - 2
    divisors_n_x = get_even_divisors(n - x)
    divisors_n_x_2 = get_even_divisors(n + x - 2)

    # Combine all divisors into a set for uniqueness
    divisors = set(divisors_n_x + divisors_n_x_2)

    # Count valid k values
    valid_k_count = 0
    for d in divisors:
        k = d // 2 + 1
        if k > 1 and k >= x:
            valid_k_count += 1

    return valid_k_count


def main():
    t = int(input())  # Number of test cases
    results = []

    for _ in range(t):
        n, x = map(int, input().split())
        results.append(find_valid_ks(n, x))

    for res in results:
        print(res)


if __name__ == "__main__":
    main()
