add_library("sound")
import Regels as Screen3

def setup():
    global bgm, scene
    fullScreen()
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
    
    Font = createFont("Rapscallion.ttf", 100)
    textFont(Font)
    
    fill(240, 223, 55)
    textSize(100)
    textAlign(CENTER)
    text("The Lost Treasure", width/2, height/8)
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
    text("Opties", 134, 175)
    
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
            
    if scene == "screen3":        
        if isMouseWithinSpace(width-300, height-75, 100, 35):
            if mousePressed:
                scene = ''
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False



            
