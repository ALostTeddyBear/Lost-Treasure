import Main

def setup():
<<<<<<< HEAD
    global side, img, scene
=======
    global side, img, scene, textBoxIsActive
    
>>>>>>> 5396e4d074af1898f1f10f9d3e8d34eb4da009d1
    scene = ''
    side = int(random(1, 7))

def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False

def draw():
    global side, img, scene, textBoxIsActive
    if scene == "main":
        Main.draw()
        return

    side = int(random(1, 7))
    loop() 
    
    fill(255, 193, 224)
    rect(840, 400, 200, 200)

    fill(255)
    stroke(204, 102, 0)
    rect(width-150, height-75, 127, 35)

    fill(0)
    textSize(28)
    text("Terug", width-87, height-47)

    if side == 1 or side == 3 or side == 5:
        fill(0)
        ellipse(940, 500, 50, 50)

    if side == 2 or side == 3 or side == 5 or side == 6 or side == 4:
        fill(0)
        ellipse(875, 435, 50, 50)
        ellipse(1005, 565, 50, 50)

    if side == 4 or side == 5 or side == 6:
        fill(0)
        ellipse(1005, 435, 50, 50)
        ellipse(875, 565, 50, 50)

    if side == 6:
        fill(0)
        ellipse(1005, 500, 50, 50)
        ellipse(875, 500, 50, 50)
        
    #if isMouseWithinSpace(840, 400, 200, 200):
           # side = int(random(1, 7)) 
           # noLoop() 
            #redraw()

    if isMouseWithinSpace(width - 150, height - 75, 127, 35):
        if mousePressed:
            Main.setup()
            scene = 'main'
            
    if scene == "main":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
                
def MousePressed():
    global side
    if mouseX >= 840 and mouseX <= 1040 and mouseY >= 400 and mouseY <= 600:
        if mousePressed:
            side = int(random(1, 7))
            noLoop()
            redraw()



    
