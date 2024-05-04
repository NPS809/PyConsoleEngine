# PyConsoleEngine
Simple console engine. Very basic functions such as creating objects, adding objects on scene, drawing scene and starting animations.

## Simple Engine programm:

```py
from Engine.imports import *

main_scene = Scene() 

player = GameObject("player")
player.GetComponent("transform").position = v2(12, 12) # Getting components

player.AddComponent(Mesh())
player.AddComponent(Animator()) # Adding components

player.GetComponent("animator").Load("Textures/anim.an")
player.GetComponent("animator").StartLoopAnimation() # Another getting components

main_scene.Add(player) 

main_scene.StartDrawingThread(0.016)
```
