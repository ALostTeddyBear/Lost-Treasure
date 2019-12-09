add_library("sound")
import Regels as Screen3
import Dobbelsteen as ScreenD

def setup():
    global bgm
    fullScreen()
    global scene
    scene = ''
    Background = loadImage("image1.png")
    Background.resize(width, height)
    background(Background)
    bgm = SoundFile(this,"The Captain's Parrot.wav")
    bgm.amp(0.25)
    bgm.play()
    bgm.loop()
    

def draw():
    global scene
    if scene == "screen3":
        Screen3.draw()
        return
    
    if scene == "screenD":
        ScreenD.draw()
        return
    
    
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
    
    if isMouseWithinSpace(width-150, height-75, 100, 35):
        if mousePressed:
            exit()

    if isMouseWithinSpace(84, 225, 100, 35):
        if mousePressed:
            Screen3.setup()
            scene = "screen3"
            
    if isMouseWithinSpace(84, 150, 100, 35):
        if mousePressed:
            ScreenD.setup()
            scene = "screenD"
            
    if scene == "screen3":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                scene = ''
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False



            
