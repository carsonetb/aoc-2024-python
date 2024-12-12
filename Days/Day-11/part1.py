sample = "41078 18 7 0 4785508 535256 8154 447"

stones = sample.split(" ")

for _ in range(25):
    j = -1
    print(len(stones))
    while j < len(stones) - 1:
        j += 1
        stone = stones[j]
        if stone == "0":
            stone = "1"
            stones[j] = stone
        elif len(stone) % 2 == 0:
            left = stone[:(len(stone) // 2)]
            right = stone[(len(stone) // 2):]
            stone = left
            stones[j] = stone

            right = right.lstrip("0")
            if right == "":
                right = "0"
            stones.insert(j + 1, right)
            j += 1
        else:
            stone = str(int(stone) * 2024)
            stones[j] = stone

print(len(stones))