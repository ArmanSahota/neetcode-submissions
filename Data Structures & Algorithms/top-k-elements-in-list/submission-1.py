class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        for i in range(len(counter)):
            return[num for num, count in counter.most_common(k)]
            
        
        