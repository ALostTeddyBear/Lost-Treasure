import Settings

def setup():
    global side, img
    side = int(random(1, 7))

def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False

def draw():
    global side, img
    

    fill(255, 193, 224)
    rect(840, 400, 200, 200)

    fill(255)
    stroke(204, 102, 0)
    rect(width/1.095, height/1.15, 125, 55, 7)
    fill(0)
    textSize(50)
    text("Terug", width/1.06, height/1.1)
    
    if isMouseWithinSpace(840, 400, 200, 200):
        if mousePressed:
            side = int(random(1, 7))

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
        

    if isMouseWithinSpace(width/1.095, height/1.15, 125, 55):
        if mousePressed:
            Settings.scene = 'main'
            
    if isMouseWithinSpace(width/1.25, height/1.15, 180, 55):
        if mousePressed:
            exit()
            




    
