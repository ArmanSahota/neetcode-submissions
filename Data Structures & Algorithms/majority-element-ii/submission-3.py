class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums) // 3
        res = []
        for num, c in count.items():
            if c > n:
                res.append(num)
        return (res)