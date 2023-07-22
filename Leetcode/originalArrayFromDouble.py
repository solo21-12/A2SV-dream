from typing import List


def findOriginalArray(self, changed: List[int]) -> List[int]:
    frequency = {}
    ans = []
    changed.sort()

    for i in changed:
        frequency[i] = frequency.get(i, 0) + 1

    for i in changed:
        if frequency.get(i, 0) > 0 and frequency.get(i*2, 0) > 0:
            ans.append(i)
            frequency[i] -= 1
            frequency[i*2] -= 1
    return ans if not any(frequency.values()) else []


    #Intition 
    # Count the frequency of time each element occur to avoid counting twice and each could be used for diffrent items
    # check if each item has a frequencey and they have a double in the array
    # return the answer array if the frquency dictinary is empty
