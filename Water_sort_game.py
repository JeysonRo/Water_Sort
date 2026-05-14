# Water_sort_game

# container requirements:
# hold 4 color objects in a stack
# support pouring color objects into other WaterContainers
# group multiple identicaly color objects in the same container so they are both poured

# represent color objects as strings
class WaterContainer:
    def __init__(self, colors: list = [], size: int = 4):
        if len(colors) > size:
            raise ValueError("input colors length exceeds specified container size")
        
        self.vial = []
        self.size = size
        for color in colors:
            self.vial.append(color)
        
    def pour(self, target: WaterContainer):
        if self.canPour(target):
            while self.canPour(target):
                self.pour(target)
        else:
            return False
        return True
    
    def canPour(self, target: WaterContainer):
        # target must have space
        if len(target.vial) >= target.size:
            print("target is full")
            return False
        # giver must not be empty
        if len(self.vial) == 0:
            print("giver is empty")
            return False
        # target top must be same color as top of giver or empty
        if len(target.vial) != 0 and target.vial[-1] != self.vial[-1]:
            print("giver and target colors do not match")
            return False
        
        return True
        

class WaterSortSolver:
    def __init__(self):
        pass
    
    def solve():
        pass