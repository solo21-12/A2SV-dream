n = int(input())
nums = list(map(int, input().split(" ")))


def alive_people(n, claws):
    alive = []

    for i in range(n):
        curr_index = i

        kill_position = max(curr_index - claws[i], 0)

        while alive and alive[-1] >= kill_position:
            alive.pop()

        alive.append(curr_index)

    return len(alive)


print(alive_people(n, nums))
