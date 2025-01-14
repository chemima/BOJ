from collections import Counter

def is_complete_hand(tiles):
    counter = Counter(tiles)
    
    # 치또이 체크
    if len(counter) == 7 and all(v == 2 for v in counter.values()):
        return True

    # Check for 1 head and 4 bodies
    def can_form_melds(tiles, meld_count=4):
        if meld_count == 0:
            return True
        counter = Counter(tiles)
        for t in sorted(counter):
            if counter[t] >= 3:
                new_tiles = tiles[:]
                new_tiles.remove(t)
                new_tiles.remove(t)
                new_tiles.remove(t)
                if can_form_melds(new_tiles, meld_count - 1):
                    return True
            if t <= 7 and counter[t] > 0 and counter[t + 1] > 0 and counter[t + 2] > 0:
                # Try to remove a sequence
                new_tiles = tiles[:]
                new_tiles.remove(t)
                new_tiles.remove(t + 1)
                new_tiles.remove(t + 2)
                if can_form_melds(new_tiles, meld_count - 1):
                    return True
        return False

    # 머리쌍 찾기
    for t in counter:
        if counter[t] >= 2:
            new_tiles = tiles[:]
            new_tiles.remove(t)
            new_tiles.remove(t)
            if can_form_melds(new_tiles):
                return True
    return False

def find_waiting_tiles(tiles):
    all_tiles = [i for i in range(1, 10) for _ in range(4)]
    current_counter = Counter(tiles)
    result = []
    
    for t in range(1, 10):
        if current_counter[t] < 4:
            new_tiles = tiles + [t]
            if is_complete_hand(new_tiles):
                result.append(t)
    
    return sorted(result)

# 입력 받기
tiles = list(map(int, input().strip().split()))
result = find_waiting_tiles(tiles)

if result:
    print(" ".join(map(str, result)))
else:
    print(-1)
