import heapq

def card_counting_out_game():
    N, M, P = map(int, input().split())
    players = []
    # Each player's hand will be a heap
    for _ in range(N):
        data = input().split()
        name = data[0]
        cards = list(map(int, data[1:] ))
        heapq.heapify(cards)
        players.append({
            'name': name,
            'cards': cards
        })

    # Global heap of (smallest_card, name, player_index)
    global_heap = []
    for i, p in enumerate(players):
        smallest_card = p['cards'][0]
        heapq.heappush(global_heap, (smallest_card, p['name'], i))

    counted_out_order = []
    active = [True]*N  # Track who is still playing

    while len(counted_out_order) < N:
        # Pop from global heap until find valid player state
        while True:
            card_val, name, idx = heapq.heappop(global_heap)
            if active[idx] and players[idx]['cards'][0] == card_val:
                # Found current smallest card of active player
                break
            # else discard stale entry and continue popping

        # This player discards their smallest card
        heapq.heappop(players[idx]['cards'])

        # If no cards left, count out
        if len(players[idx]['cards']) == 0:
            active[idx] = False
            counted_out_order.append(name)
        else:
            # Push updated smallest card of this player into global heap
            heapq.heappush(global_heap, (players[idx]['cards'][0], name, idx))

        # Penalize all other active players
        for j in range(N):
            if j != idx and active[j]:
                # Remove smallest card
                smallest = heapq.heappop(players[j]['cards'])
                # Add penalty
                smallest += P
                # Push back penalized card
                heapq.heappush(players[j]['cards'], smallest)
                # Update global heap with new smallest card
                heapq.heappush(global_heap, (players[j]['cards'][0], players[j]['name'], j))

    print(' '.join(counted_out_order))


if __name__ == "__main__":
    card_counting_out_game()
