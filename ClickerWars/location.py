from pico2d import*

class Location:
    image = None

    def __init__(self):
        self.image = load_image('location/location_1.jpg')

    def draw(self):
        self.image.draw(240, 400)