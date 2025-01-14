def solve():
    import sys
    input = sys.stdin.readline
    
    N = int(input().strip())
    tiles = input().split()

    counts = {}
    
    for i, tile in enumerate(tiles):
        counts[tile] = counts.get(tile, 0) + 1
        if counts[tile] == 5:
            print(i + 1)
            return
    print(0)

solve()
