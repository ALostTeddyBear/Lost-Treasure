add_library("sound")
import Functies

def setup():
    fullScreen()
    
    Background = loadImage("Background1.jpg")
    Background.resize(width, height)
    background(Background)

    
def draw():
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    text("Spel Regels!", width/2, height/8)
    fill(240, 223, 55)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width-150, height-75, 127, 35)
    rect(width-300, height-75, 100, 35)
    fill(0)
    textSize(28)
    text("Afsluiten", width-87, height-47)
    text("Terug", width-237, height-47)
    
    def isMouseWithinSpace(x, y, breedte, hoogte):
        if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
            return True
        else:
            return False
    
    if isMouseWithinSpace(width-150, height-75, 127, 35):
        if mousePressed:
            exit()
        
