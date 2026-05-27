import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       #TODO implement min heap 
        self.heap = []
        self.numElements =k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)  # Remove the smallest of the top k

    def add(self, val: int) -> int:
         
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.numElements:
            heapq.heappop(self.heap)
        return self.heap[0]
        
