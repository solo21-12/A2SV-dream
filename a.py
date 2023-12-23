def incremovableSubarrayCount(nums) -> int:
    count = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            if subarray == sorted(subarray) and (i == 0 or j == len(nums) - 1 or nums[i-1] < nums[j]):
                count += 1

    return count


print(incremovableSubarrayCount([8,7,6,6]))
