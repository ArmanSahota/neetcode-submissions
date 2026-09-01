class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        L = 0
        R = 0
        res = []
        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            if L > q[0]:
                q.popleft()
            
            if R + 1 >= k:
                res.append(nums[q[0]])
                L += 1
            R += 1
        return res