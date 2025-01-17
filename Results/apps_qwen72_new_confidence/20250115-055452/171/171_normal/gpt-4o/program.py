from collections import deque

def card_game(n, k1, cards1, k2, cards2):
    player1 = deque(cards1)
    player2 = deque(cards2)
    seen_states = set()
    rounds = 0
    
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in seen_states:
            return -1
        seen_states.add(state)
        
        card1 = player1.popleft()
        card2 = player2.popleft()
        
        if card1 > card2:
            player1.append(card2)
            player1.append(card1)
        else:
            player2.append(card1)
            player2.append(card2)
        
        rounds += 1
    
    winner = 1 if player1 else 2
    return rounds, winner

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k1 = int(data[1])
    cards1 = list(map(int, data[2:2+k1]))
    k2 = int(data[2+k1])
    cards2 = list(map(int, data[3+k1:3+k1+k2]))
    
    result = card_game(n, k1, cards1, k2, cards2)
    if result == -1:
        print(result)
    else:
        print(result[0], result[1])
