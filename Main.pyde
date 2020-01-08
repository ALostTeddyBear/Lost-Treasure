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
    print(Settings.scene)
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
    textSize(32)
    textAlign(CENTER)
    text("The Lost Treasures", width/2, 75)

    fill(255)
    stroke(204, 102, 0)
    rect(84, 75, 100, 35)
    fill(0)
    textSize(28)
    text("Start", 130, 100)
    
    fill(255)
    stroke(204, 102, 0)
    rect(84, 150, 100, 35)
    fill(0)
    text("Dobbelsteen", 134, 175)
    
    fill(255)
    stroke(204, 102, 0)
    rect(84, 225, 100, 35)
    fill(0)
    text("Regels", 134, 250)
    
    fill(255)
    stroke(204, 102, 0)
    rect(width-150, height-75, 127, 35)
    fill(0)
    textSize(28)
    text("Afsluiten", width-87, height-47)
    
    if mouseX >= 1765 and mouseX <= 1892 and mouseY >= 1005 and mouseY <= 1040:
        if mousePressed:
            exit()
                
    if mouseX >= 84 and mouseX <= 184 and mouseY >= 75 and mouseY <= 110:
        if mousePressed:
            PlayerSetup.setup()
            Settings.scene = 'start'           
            
    if Settings.scene == "start":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                Settings.scene = ''
                    
    if mouseX >= 84 and mouseX <= 184 and mouseY >= 150 and mouseY <= 185:
        if mousePressed:
            Dobbelsteen.setup()
            Settings.scene = 'dobbelsteen'            
            
    if Settings.scene == "dobbelsteen":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                Settings.scene = ''
    
    if mouseX >= 84 and mouseX <= 184 and mouseY >= 225 and mouseY <= 260:
        if mousePressed:
            Regels.setup()
            Settings.scene = 'regels'
    
            
    if Settings.scene == "regels":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                Settings.scene = ''        

            
    if mouseX >= 1765 and mouseX <= 1892 and mouseY >= 1005 and mouseY <= 1040:
        if mousePressed:
            exit()
            
def keyPressed():
    PlayerSetup.keyPressed()
