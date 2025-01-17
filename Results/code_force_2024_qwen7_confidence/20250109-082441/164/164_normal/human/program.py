import heapq
from typing import List, Tuple


def compute_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Compute the Greatest Common Divisor (GCD) of a and b using the Extended Euclidean Algorithm."""
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = compute_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y


def find_minimum_steps(num_platforms: int, num_passages: int, max_level: int, levels: List[int], changes: List[int],
                       passages: List[Tuple[int, int]]) -> int:
    """Calculate the minimum number of steps needed to reach from platform 1 to platform num_platforms."""
    try:
        # Initialize graph and distances
        adjacency_list: List[List[int]] = [[] for _ in range(num_platforms)]
        for u, v in passages:
            adjacency_list[u - 1].append(v - 1)
            adjacency_list[v - 1].append(u - 1)

        distances: List[int] = [-1] * num_platforms
        distances[0] = 0
        priority_queue: List[Tuple[int, int]] = [(0, 0)]  # (distance, platform)
        visited: List[bool] = [False] * num_platforms

        while priority_queue:
            _, current_platform = heapq.heappop(priority_queue)
            if visited[current_platform]:
                continue
            visited[current_platform] = True
            for neighbor in adjacency_list[current_platform]:
                if visited[neighbor]:
                    continue
                level_difference = (levels[neighbor] - levels[current_platform] + max_level) % max_level
                changes_difference = (changes[current_platform] - changes[neighbor] + max_level) % max_level
                gcd_val, x, y = compute_gcd(changes_difference, max_level)
                if level_difference % gcd_val != 0:
                    continue
                level_difference //= gcd_val
                x *= level_difference
                step_difference = distances[current_platform] - x
                k = (step_difference + (max_level // gcd_val) - 1) // (
                            max_level // gcd_val) if step_difference >= 0 else -(
                            (-step_difference) // (max_level // gcd_val))
                steps = x + k * (max_level // gcd_val)
                if distances[neighbor] == -1 or distances[neighbor] > steps + 1:
                    distances[neighbor] = steps + 1
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

        return distances[num_platforms - 1]
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1


def main():
    num_cases: int = int(input())
    for _ in range(num_cases):
        num_platforms, num_passages, max_level = map(int, input().split())
        levels: List[int] = list(map(int, input().split()))
        changes: List[int] = list(map(int, input().split()))
        passages: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(num_passages)]
        result: int = find_minimum_steps(num_platforms, num_passages, max_level, levels, changes, passages)
        print(result)


if __name__ == "__main__":
    main()