import Main
import javax.swing.JFrame as JFrame
import javax.swing.JOptionPane as JOptionPane

def setup():
    global bgm, scene
    fullScreen()
    global scene
    scene = ''
    Background = loadImage("image1.png")
    Background.resize(width, height)
    background(Background)
 
def input(message=''):
    return JOptionPane.showInputDialog("Speler naam:", message)

def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False
    
def draw():
    global scene
    if scene == "main":
        Main.draw()
        return
    
    fill(255)
    stroke(204, 102, 0)
    rect(30, 75, 260, 35)
    
    fill(0)
    textSize(28)
    text("Klik hier om een naam in te voeren", 160, 100)
    
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
    text("Start spel", width - 87, height - 47)
    
    if isMouseWithinSpace(30, 75, 260, 35):
        if mousePressed:
            answer = input()
            println(str(answer))
            
    if isMouseWithinSpace(width - 300, height - 75, 127, 35):
        if mousePressed:
            Main.setup()
            scene = 'main'
    
    
            
    
    
