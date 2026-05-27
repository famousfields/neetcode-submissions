class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem = defaultdict(int)

        for i in nums:
            elem[i] += 1

        keys_with_highest_values = sorted(elem, key=elem.get, reverse=True)[:k]
        
        return keys_with_highest_values


        