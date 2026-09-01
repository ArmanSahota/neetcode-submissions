class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for i, c in count.items():
            freq[c].append(i)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        print(freq)

