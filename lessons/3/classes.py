class SizeParameters:
    width = 2
    depth = 1
    height = 1

    def __init__(self, _width, _height, _depth):
        self.width = _width
        self.height = _height
        self.depth = _depth


class Box:
    parameters: SizeParameters
    capacity: int
    type: str
    itemArray: list

    def __init__(self, _parameters: SizeParameters, _capacity: int, _type: str, _itemArray: list):
        self.parameters = _parameters
        self.capacity = _capacity
        self.type = _type
        self.itemArray = _itemArray


    def sortItems(self):
        self.itemArray = sorted(self.itemArray)

    def showItems(self):
        for x in range(len(self.itemArray)):
            print(self.itemArray[x])

par = SizeParameters(2,1,1)

box = Box(par, 40, 'iron', [4,5,1,8,6,42,0,15])

#box.showItems()
print(box.itemArray)
box.sortItems()
print(box.itemArray)

print("Width:: " + str(box.parameters.width))
