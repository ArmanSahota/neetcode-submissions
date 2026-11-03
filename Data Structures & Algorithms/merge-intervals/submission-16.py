class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prev_start, prev_end = result[-1]

            if prev_end >= start:
                result[-1] = [prev_start, max(prev_end, end)]
            else:
                result.append(intervals[i])
        return result
