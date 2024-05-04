import os
import time
from threading import Thread
from Engine.error import Error
from Engine.game_object import GameObject
from Engine.utils import v2


class Scene:
    def __init__(self):
        os.system("mode con cols=120 lines=30")
        os.system("title Engine")
        self._objects = list()
        self._previous_screen = ""
        self._is_drawing = False

    def Add(self, *objects: GameObject):
        for obj in objects:
            if obj not in self._objects:
                self._objects.append(obj)
                obj.scene = self
            else:
                return Error(3, obj.tag)

    def Remove(self, obj: GameObject):
        if obj in self._objects:
            self._objects.remove(obj)
        else:
            return Error(4, obj.tag)

    def Draw(self):
        screen = " " * 120 * 30
        for obj in self._objects:
            if obj.isComponent("mesh") and obj.isComponent("transform"):
                object_mesh_dots = obj.GetComponent("mesh").dots
                object_position = obj.GetComponent("transform").position
                for dot in object_mesh_dots:
                    screen = SetPoint(screen, object_position + dot.offset, dot.sign)
        if screen != self._previous_screen:
            os.system("cls")

            print(screen, end="", flush=True)
            self._previous_screen = screen

    def StartDrawingThread(self, update_time: float):
        self._is_drawing = True

        def Drawing():
            while self._is_drawing:
                # Hello
                self.Draw()
                time.sleep(update_time)

        Thread(target=Drawing).start()

    def StopDrawingThread(self):
        self._is_drawing = False


def SetPoint(screen: str, position: v2, sign: str):
    if v2(0, 0) <= position <= v2(119, 29):
        pos = position.y * 120 + position.x
        screen = screen[:pos] + sign + screen[pos + 1:]
    return screen
