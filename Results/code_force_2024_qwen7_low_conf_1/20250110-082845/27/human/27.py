def count_permutations(cards, coins):
    n = len(cards)
    max_score = 0

    for i in range(1, n + 1):
        num_cards = cards[i - 1]
        if num_cards > 0:
            remaining_coins = coins - (n - num_cards)
            if remaining_coins >= 0:
                score = num_cards * n
                remaining_cards = [c for c in cards if c != i]
                remaining_cards.append(remaining_coins)
                score += count_permutations(remaining_cards, remaining_coins)
                max_score = max(max_score, score)

    return max_score