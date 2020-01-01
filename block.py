
class Block:
    BLOCK_SIZE = 20

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def containsPoint(self, point):
        containsX = point[0] >= self.x and point[0] <= self.x + Block.BLOCK_SIZE
        containsY = point[1] >= self.y and point[1] <= self.y + Block.BLOCK_SIZE
        return containsX and containsY
