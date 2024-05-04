from Engine.imports import *

main_scene = Scene()

player = GameObject("player")
player.GetComponent("transform").position = v2(0, 12)
player.AddComponent(Mesh())
player.AddComponent(Animator())
player.GetComponent("animator").Load("Textures/anim.an")
player.GetComponent("animator").StartLoopAnimation()
main_scene.Add(player)


main_scene.StartDrawingThread(0.016)

while True:
    player.GetComponent("transform").Translate(v2(1, 0))
    if player.GetComponent("transform").position.x == 120:
        player.GetComponent("transform").position.x = 0
    time.sleep(0.5)
