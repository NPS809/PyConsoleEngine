import time
from threading import Thread

from Engine.Components.component import Component
from Engine.error import Error
from Engine.utils import ConvertStringToDot, RemoveEmptyStringsFromList
from Engine.texts import *


class Frame:
    def __init__(self, dots: list, _time: float | int):
        self.dots = dots
        self.time = _time


class Animator(Component):
    id = "animator"

    def __init__(self):
        self.frames = []
        self.is_running = False
        self.loaded_animation = ""

    def CheckForParentComponents(self):
        if not self.parent.isComponent("mesh"):
            return Error(7, self.parent.tag)
        elif not self.parent.isComponent("transform"):
            return Error(8, self.parent.tag)
        else:
            return True

    def StartAnimation(self, delay=-1):
        if self.CheckForParentComponents():
            if not self.frames:
                return Error(10, self.parent.tag)
            else:
                self.is_running = True

                def anim():
                    if delay > 0:
                        time.sleep(delay)
                    for frame in self.frames:
                        self.parent.GetComponent("mesh").dots = frame.dots
                        time.sleep(frame.time)
                    self.is_running = False

                Thread(target=anim).start()

    def StartLoopAnimation(self, delay=-1):
        if self.CheckForParentComponents():
            if not self.frames:
                return Error(10, self.parent.tag)
            else:
                self.is_running = True

                def anim():
                    if delay > 0:
                        time.sleep(delay)
                    while self.is_running:
                        for frame in self.frames:
                            self.parent.GetComponent("mesh").dots = frame.dots
                            time.sleep(frame.time)
                    self.is_running = False

                Thread(target=anim).start()

    def StopAnimation(self):
        if not self.is_running:
            return Error(11, self.parent.tag)
        else:
            self.is_running = False
            self.frames = []
            self.loaded_animation = ""

    def Load(self, path_to_anim_file):
        try:
            with open(path_to_anim_file, "r", encoding="utf-8") as file:
                _text = file.read()
                frames_and_times = _text.split(">>")
                for frame_and_time in frames_and_times:
                    try:
                        tmp = frame_and_time.split("\n")
                        tmp = RemoveEmptyStringsFromList(tmp)
                        if tmp:
                            self.frames.append(Frame(
                                [ConvertStringToDot(dot) for dot in tmp[1:]],  # Строки преобразованные в точки mesh'a
                                float(tmp[0])))  # Первая строка в frame_and_time равная времени кадра
                    except ValueError:
                        return Error(14, f" >>> {tmp[0].replace(" ", "")} <<< \n{text["ft"]}")
            self.loaded_animation = path_to_anim_file
        except FileNotFoundError:
            return Error(9, path_to_anim_file)
