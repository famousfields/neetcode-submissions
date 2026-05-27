class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(numbers)):
            if target - numbers[i] in myMap:
                return [myMap[target-numbers[i]], i+1]
                       
            myMap[numbers[i]] = i + 1


        return []
        