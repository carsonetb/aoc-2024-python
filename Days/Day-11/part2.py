import copy

sample = "41078 18 7 0 4785508 535256 8154 447"

stones = {}

for item in sample.split(" "):
    if stones.get(item):
        stones[item] += 1
    else:
        stones[item] = 1

def setval(num, amm, inside):
    if inside.get(num):
        inside[num] += amm
    else:
        inside[num] = amm

for _ in range(75):
    j = -1
    o_stones = copy.deepcopy(stones)
    new_stones = {}
    while j < len(o_stones.keys()) - 1:
        j += 1
        stone = list(o_stones.keys())[j]
        amm = o_stones[stone]
        if amm > 1:
            pass
        if _ == 4:
            pass
        if stone == "0":
            old_stone = copy.copy(stone)
            stone = "1"
            setval(stone, amm, new_stones)
        elif len(stone) % 2 == 0:
            old_stone = copy.copy(stone)
            left = stone[:(len(stone) // 2)]
            right = stone[(len(stone) // 2):]

            right = right.lstrip("0")
            if right == "":
                right = "0"
            setval(right, amm, new_stones)
            setval(left, amm, new_stones) 
        else:
            old_stone = copy.copy(stone)
            stone = str(int(stone) * 2024)
            setval(stone, amm, new_stones)
    stones = new_stones

o = 0

for stone in stones.keys():
    o += stones[stone]

print(o)