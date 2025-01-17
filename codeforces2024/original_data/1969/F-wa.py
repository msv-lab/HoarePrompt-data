def max_coins(n, k, card_types):
    from collections import Counter
    
    # Initial hand with the first k cards
    hand = card_types[:k]
    deck = card_types[k:]
    
    # Count the occurrences of each type in the hand
    hand_count = Counter(hand)
    
    coins = 0
    
    while True:
        # Pair cards in hand
        for card_type in list(hand_count.keys()):
            pairs = hand_count[card_type] // 2
            coins += pairs
            hand_count[card_type] -= pairs * 2
            if hand_count[card_type] == 0:
                del hand_count[card_type]
        
        # Check if we can draw more cards
        if len(deck) >= 2:
            # Draw two cards from the deck
            new_cards = deck[:2]
            deck = deck[2:]
            for card in new_cards:
                hand_count[card] += 1
        else:
            # If the deck is empty, break the loop
            break
    
    return coins

# Read input
n, k = map(int, input().split())
card_types = list(map(int, input().split()))

# Calculate and print the maximum number of coins
print(max_coins(n, k, card_types))