class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [ -s for s in nums]
        heapq.heapify(nums)
        
        res = []
        while k > 0:
            x = heapq.heappop(nums)
            res.append(x)
            k -= 1
        return -res[-1]