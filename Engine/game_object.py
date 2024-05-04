from Engine.Components.animator import Animator
from Engine.Components.mesh import Mesh
from Engine.Components.component import Component
from Engine.Components.transform import Transform
from Engine.error import Error


class GameObject:
    def __init__(self, tag="gameObject"):
        self.tag = tag
        self._scene = None
        self._components = list()
        self._childs = list()
        self.AddComponent(Transform())

    def AddComponent(self, added_component: Component):
        for component in self._components:
            if component.id == added_component.id:
                return Error(1, added_component.id)
        added_component.parent = self
        self._components.append(added_component)

    def GetComponent(self, component_id: str) -> Mesh | Transform | Animator:
        for component in self._components:
            if component.id == component_id:
                return component
        Error(2, component_id)

    def isComponent(self,  component_id: str):
        for component in self._components:
            if component.id == component_id:
                return True
        return False
    