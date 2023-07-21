class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]

        for start,end in intervals[1:]:

            lastEnd = ans[-1][1]

            if start <= lastEnd:
                ans[-1][1] = max(lastEnd,end)
            else:
                ans.append([start,end])
        
        return ans
    


    # intution
    # sort the 2d array based on their first index elements so we only have to worry about there last index 
    #  put the first elemnet in to the anser array so that we can avoid edge case and could use it to compare with current interval
    # iterate through each element and compare it's first index eleemtn with the ans last interval
    # if they merge merge them
    # else add the current element to anser array