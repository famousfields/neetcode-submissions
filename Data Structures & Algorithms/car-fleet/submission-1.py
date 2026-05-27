class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 10, position = [1,4], speed = [3,2]
        car 1     |      car 2:
        1 - 1               4
        2- 4                6
        3  7                8
        4 10                10


         target = 10, position = [4,1,0,7], speed = [2,2,1,1]
 
          car 1     |      car 2:         | car 3:   | car 4:
        1 - 4                1              0           7                   
        2-  6                3              1           8
        3   8                5              2           9
        4   10               7              3           10
        """
        pair = [(p,s) for p,s in zip(position,speed)]
        current_pos = position
        pair.sort(reverse = True)

        myStack = []
        for p,s in pair:
            myStack.append((target - p)/s)

            if len(myStack) >= 2 and myStack[-1] <= myStack[-2]:
                myStack.pop()
                
        return len(myStack)


            

        