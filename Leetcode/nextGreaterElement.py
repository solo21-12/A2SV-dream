from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    lookUp = {}
    ans = []
    stack = []
    for i in range(len(nums2)-1, -1, -1):
        if len(stack) == 0:
            stack.append(nums2[i])
        else:
            top = stack[-1]
            if nums2[i] > top:
                while len(stack) > 0 and nums2[i] > stack[-1]:
                    stack.pop()

                if len(stack) > 0:
                    lookUp[nums2[i]] = lookUp.get(nums2[i], 0) + stack[-1]
                    stack.append(nums2[i])
                else:
                    stack.append(nums2[i])
                    lookUp[nums2[i]] = lookUp.get(nums2[i], 0) - 1
            else:
                stack.append(nums2[i])
                lookUp[nums2[i]] = lookUp.get(nums2[i], 0) + top

    lookUp[nums2[-1]] = lookUp.get(nums2[-1], 0) - 1
    for i in nums1:
        ans.append(lookUp[i])

    return ans
