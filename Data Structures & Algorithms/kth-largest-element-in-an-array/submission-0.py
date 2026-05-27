class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to max heap by negating values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # Pop the largest element k-1 times
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # The next element is the k-th largest
        return -heapq.heappop(max_heap)
        