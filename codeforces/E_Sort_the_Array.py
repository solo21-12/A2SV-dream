def is_sortable_by_one_reverse(n, arr):
    sorted_arr = sorted(arr)

    start, end = -1, -1
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            if start == -1:
                start = i
            end = i

    if start == -1:
        return "yes\n1 1"

    reversed_segment = arr[:start] + \
        list(reversed(arr[start:end + 1])) + arr[end + 1:]
    if reversed_segment == sorted_arr:
        return f"yes\n{start + 1} {end + 1}"

    return "no"


n = int(input())
arr = list(map(int, input().split()))

result = is_sortable_by_one_reverse(n, arr)
print(result)
