import sys
from colorama import Fore


def Error(error_id: int, add_info=""):
    err = errors[error_id]
    print(f"{Fore.RED}{err.name} | {err.desc}\n>>> {add_info}")
    input()
    sys.exit()


class Err:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc


errors = {
    1: Err("ComponentError", "Компонент уже присвоен"),
    2: Err("ComponentError", "У объекта нет такого компонента для получения"),
    3: Err("SceneError", "Этот объект уже есть на сцене"),
    4: Err("SceneError", "Такого объекта нет на сцене"),
    5: Err("ColliderError", "У объекта должна быть текстура для обнаружения коллизии"),
    6: Err("MeshLoaderError", "Такого файла текстуры не существует"),
    7: Err("AnimatorDependenciesError", "У объекта отсутствует компонент mesh"),
    8: Err("AnimatorDependenciesError", "У объекта отсутствует компонент transform"),
    9: Err("AnimatorLoaderError", "Такого файла анимации не существует"),
    10: Err("AnimatorError", "Анимация не загружена. Ее старт невозможен"),
    11: Err("AnimatorError", "Анимация не запущена. Ее остановка невозможна"),
    12: Err("FileLoaderError", "Ошибка в синтаксисе файла текстуры / анимации"),
    13: Err("TextureError", "Знак у точки mesh'a должен быть один"),
    14: Err("AnimatorLoaderError", "Ошибка в синтаксисе файла анимации"),
    15: Err("LiveLoggerError", "Система LiveLog не запущена")
}



