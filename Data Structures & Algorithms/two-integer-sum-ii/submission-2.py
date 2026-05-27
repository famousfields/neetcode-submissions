class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myMap = {}
        res = []
        for i in range(len(numbers)):
            if target - numbers[i] in myMap:
                if myMap.get(target-numbers[i]) != i:
                    res.append(myMap.get(target-numbers[i])+1)
                    res.append(i+1)
                       
            myMap[numbers[i]] = i


        return res
        