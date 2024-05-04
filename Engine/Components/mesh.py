from Engine.Components.component import Component
from Engine.error import Error
from Engine.utils import Dot, ConvertStringToDot


class Mesh(Component):
    id = "mesh"

    def __init__(self):
        self.dots = list()

    def Add(self, dot: Dot):
        self.dots.append(dot)

    def Load(self, path_to_mesh_file: str):
        try:
            with open(path_to_mesh_file, "r") as file:
                file = file.read().split("\n")
                for string in file:
                    self.Add(ConvertStringToDot(string))
        except FileNotFoundError:
            return Error(6, path_to_mesh_file)
