from Engine.Components.component import Component
from Engine.utils import v2



class Transform(Component):
    id = "transform"

    def __init__(self, position=v2()):
        self.position = position

    def Translate(self, position_offset):
        self.position += position_offset

