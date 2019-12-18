add_library("sound")
import Functies
import Regels4
import Regels6


def setup():
    global scene
    fullScreen()
    
    scene = ''
    Background = loadImage("RulesBackground.jpg")
    Background.resize(width, height)
    background(Background)

    
def draw():
    global scene
    if scene == "regels4":
        Regels4.draw()
        return
    
    if scene ==  "regels6":
        Regels6.draw()
        return
    
    img = loadImage("ValKaarten.png")
    imageMode(CENTER)
    image(img, width / 2, height / 2)
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    text("Spel Regels!", width / 2, height / 8)
    fill(240, 223, 55)
    
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
    
    def isMouseWithinSpace(x, y, breedte, hoogte):
        if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
            return True
        else:
            return False
    
    if isMouseWithinSpace(width - 300, height - 75, 127, 35):
        if mousePressed:
            Regels4.setup()
            scene = "regels4"
            
    if scene == "regels4":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
                
    if isMouseWithinSpace(width - 150, height - 75, 127, 35):
        if mousePressed:
            Regels6.setup()
            scene = "regels6"
            
    if scene == "regels6":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
    
