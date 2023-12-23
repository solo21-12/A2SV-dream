n = int(input())
fingers = list(map(int, input().split()))

ways_to_avoid_cleaning = 0
for i in range(1, 6):
    total_fingers = sum(fingers) + i
    if total_fingers % (n + 1) != 1:
        ways_to_avoid_cleaning += 1

print(ways_to_avoid_cleaning)
