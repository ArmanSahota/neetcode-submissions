class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for i, num in count.items():
            freq[num].append(i)
        result = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                result.append(j)
                k -= 1
                if k == 0:
                    return result

