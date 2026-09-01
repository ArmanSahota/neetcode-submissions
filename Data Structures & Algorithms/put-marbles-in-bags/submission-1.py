class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        min_heap = []
        max_heap = []

        for i in range(len(weights) - 1):
            splits = weights[i] + weights[i + 1]

            if len(min_heap) < k - 1:
                heapq.heappush(min_heap, splits)
            else:
                heapq.heappushpop(min_heap, splits)

            if len(max_heap) < k - 1:
                heapq.heappush(max_heap, -splits)
            else:
                heapq.heappushpop(max_heap, -splits)
        max_score = sum(min_heap)
        min_score = -sum(max_heap)

        return max_score - min_score
