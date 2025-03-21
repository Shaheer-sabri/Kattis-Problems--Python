W, P = map(int, input().split())
widths = []
partitions = list(map(int, input().split()))
partitions.insert(0,0)
partitions.insert(P+1, W)

for x in partitions:
    for y in partitions:
        if x < y:
            width = y - x
            if width not in widths:
                widths.append(width)

widths.sort()
print(*widths, sep=" ")


    