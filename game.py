

class Game:
    # Constants
    FPS = 1
    UPDATES_PER_SECOND = int(1000 / FPS)

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height

    def update(self):
        self.tick()
        self.render()
        self.canvas.after(Game.UPDATES_PER_SECOND, self.update)


    def tick(self):
        print('Updating game objects...')


    def render(self):
        print('Rendering game objects...')
