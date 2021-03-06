import Regels5
import Regels7

def setup():
    global scene
    fullScreen()
    scene = ''
    Background = loadImage("RulesBackground.jpg")
    Background.resize(width, height)
    background(Background)
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False

def draw():
    global scene
    if scene == "regels5":
        Regels5.draw()
        return
    
    if scene ==  "regels7":
        Regels7.draw()
        return
    
    img = loadImage("RegelsTest6.PNG")
    img.resize(width, height)
    imageMode(CENTER)
    image(img, width / 2, height / 2)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 300, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Terug", width - 240, height - 47)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 150, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Volgende", width - 87, height - 47)
    
    if isMouseWithinSpace(width - 300, height - 75, 127, 35):
        if mousePressed:
            Regels5.setup()
            scene = "regels5"
            
    if scene == "regels5":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
                
    if isMouseWithinSpace(width - 150, height - 75, 127, 35):
        if mousePressed:
            Regels7.setup()
            scene = "regels7"
            
    if scene == "regels7":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
                
    
