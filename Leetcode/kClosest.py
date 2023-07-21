import math
from typing import List


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    ans = {}
    output = []
    i = 0
    for start, end in points:
        res = math.sqrt(pow(start, 2) + pow(end, 2))
        ans[i] = ans.get(i, 0) + res
        i += 1

    sorted_dict = {key: value for key, value in sorted(
        ans.items(), key=lambda item: item[1])}

    for key, val in sorted_dict.items():
        output.append(points[key])

    return output[:k]
