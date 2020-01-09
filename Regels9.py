import Regels8
import Settings

def setup():
    fullScreen()
    Background = loadImage("RulesBackground.jpg")
    Background.resize(width, height)
    background(Background)
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False
    
def draw():   
    img1 = loadImage("VoorbeeldMap1.png")
    img2 = loadImage("VoorbeeldMap2.png")
    img3 = loadImage("VoorbeeldMap3.png")
    img4 = loadImage("VoorbeeldMap4.png")
    image(img1, 225, height / 2)
    image(img2, 725, height / 2)
    image(img3, 1225, height / 2)
    image(img4, 1685, height / 2)
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    text("Map voorbeelden", width / 2, height / 8)
    fill(240, 223, 55)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 300, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Hoofdmenu", width - 240, height - 47)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width - 150, height - 75, 127, 35)
    
    fill(0)
    textSize(28)
    text("Terug", width - 87, height - 47)
    
    if isMouseWithinSpace(width - 300, height - 75, 127, 35):
        if mousePressed:
            Settings.scene = "main"
            
    
    if isMouseWithinSpace(width - 150, height - 75, 127, 35):
        if mousePressed:
            Regels8.setup()
            scene = "regels8"
            
    if Settings.scene == "regels8":        
        if isMouseWithinSpace(width - 350, height - 75, 100, 35):
            if mousePressed:
                scene = ""
