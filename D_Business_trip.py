def solver(k, days):
    count = 0
    sum_increase = 0
    days.sort(reverse=True)

    for i in days:
        if sum_increase >= k:
            return count

        sum_increase += i
        count += 1

    return -1


k = int(input())

days = [int(num) for num in input().split(" ")]


print(solver(k, days))
