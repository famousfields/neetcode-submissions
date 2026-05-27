class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = []
        result = [0] * len(temperatures)
        
        for i,t in enumerate(temperatures):
            
            while temp and t > temp[-1][0]:
                stackT, stackI = temp.pop()
                result[stackI] = (i-stackI)
            
            temp.append([t,i])
        return result

