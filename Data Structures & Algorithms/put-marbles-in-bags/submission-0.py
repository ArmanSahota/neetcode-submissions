class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        splits = []

        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])

        splits.sort()
        i = k - 1

        max_score = sum(splits[-i :])
        min_score = sum(splits[: i])

        return max_score - min_score if k > 1 else 0