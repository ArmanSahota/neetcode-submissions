class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = result[-1]
            if prev_end >= start:
                result[-1] = [prev_start, max(prev_end, end)]
            else:
                result.append([start, end])
        return result