import Regels 
import Dobbelsteen
import PlayerSetup
import Settings

def setup():
    global Background
    fullScreen()
    Background = loadImage("image1.png")
    Background.resize(width, height)
    background(Background)
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False

def draw():
    if Settings.scene == "regels":
        Regels.draw()
        return
    
    if Settings.scene == "dobbelsteen":
        Dobbelsteen.draw()
        return
    
    if Settings.scene == "start":
        PlayerSetup.draw()
        return
    
    background(Background)
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    
    fill(0, 255, 255)
    textSize(100)
    textAlign(CENTER)
    text("The Lost Treasures", width / 2, height = 125)

    fill(255)
    stroke(204, 102, 0)
    rect(width/30, height/6, 180, 55, 7)
    fill(0)
    textSize(50)
    text("Start", width/17.5, height/6+45)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width/30, height/4, 180, 55, 7)
    fill(0)
    text("Dobbelsteen", width/13, height/4+45)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width/30, height/3, 180, 55, 7)
    fill(0)
    text("Regels", width/16, height/3+45)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width/1.25, height/1.15, 180, 55, 7)
    fill(0)
    textSize(50)
    text("Afsluiten", width/1.19, height/1.1)
    
    if isMouseWithinSpace(width/30, height/6, 180, 55):
        if mousePressed:
            PlayerSetup.setup()
            Settings.scene = 'start'           
            
    if Settings.scene == "start":        
        if isMouseWithinSpace(width/1.25, height/1.15, 180, 55):
            if mousePressed:
                Settings.scene = ''
                    
    if isMouseWithinSpace(width/30, height/4, 180, 55):
        if mousePressed:
            Dobbelsteen.setup()
            Settings.scene = 'dobbelsteen'            
            
    if Settings.scene == "dobbelsteen":        
        if isMouseWithinSpace(width/1.25, height/1.15, 180, 55):
            if mousePressed:
                Settings.scene = ''
    
    if isMouseWithinSpace(width/30, height/3, 180, 55):
        if mousePressed:
            Regels.setup()
            Settings.scene = 'regels'
    
            
    if Settings.scene == "regels":        
        if isMouseWithinSpace(width/1.25, height/1.15, 180, 55):
            if mousePressed:
                Settings.scene = ''        

            
    if isMouseWithinSpace(width/1.25, height/1.15, 180, 55):
        if mousePressed:
            exit()
            
def keyPressed():
    PlayerSetup.keyPressed()
