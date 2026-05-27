class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # largest
            x = -heapq.heappop(max_heap)  # second largest

            if x != y:
                newStone = y - x
                heapq.heappush(max_heap, -newStone)  # push negated value


        return -heapq.heappop(max_heap) if len(max_heap) > 0 else 0

        

        