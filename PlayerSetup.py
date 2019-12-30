import Dobbelsteen
import Main

def setup():
    global message, message2, message3, message4, message5, message6, message7, message8, message9, message10
    global textBoxIsActive, textBox2IsActive, textBox3IsActive, textBox4IsActive, textBox5IsActive, side, img, img2, img3, img4, img5, img6, scene
    fullScreen()
    img = loadImage("5.jpg")
    img2 = loadImage("Speler1.PNG")
    img3 = loadImage("Speler2.PNG")
    img4 = loadImage("Speler3.PNG")
    img5 = loadImage("Speler4.PNG")
    img6 = loadImage("Speler5.PNG")
    message = 'Naam speler'
    message2 = 'Naam speler'
    message3 = 'Naam speler'
    message4 = 'Naam speler'
    message5 = 'Naam speler'
    
    scene = ''
    

    textBoxIsActive = False
    textBox2IsActive = False
    textBox3IsActive = False
    textBox4IsActive = False
    textBox5IsActive = False
    
    side = int(random(1, 7))
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if (x < mouseX < x + breedte and y < mouseY < y + hoogte):
        return True
    else:
        return False
    
def draw():
    global side, img, img2, img3, img4, img5, scene
    image(img, 0, 0, width, height)
    image(img2, 190, 60, 90, 40)
    image(img3, 190, 260, 90, 40)
    image(img4, 190, 460, 90, 40) 
    image(img5, 190, 660, 90, 40)
    image(img6, 190, 860, 90, 40)
    
    if scene == "main":
        Main.draw()
        return
    

    
    if textBoxIsActive:
        fill(255)
    else:
        fill(0, 200, 0)
    
    rect(100, 100, 250, 80)
    
    if textBox2IsActive:
        fill(255)
    else:
        fill(250, 0, 0)
    rect(100, 300, 250, 80)
    
    if textBox3IsActive:
        fill(255)
    else:
        fill(20, 138, 230)
    rect(100, 500, 250, 80)
    
    if textBox4IsActive:
        fill(255)
    else:
        fill(255, 255, 55)
    rect(100, 700, 250, 80)
    
    if textBox5IsActive:
        fill(255)
    else:
        fill(100)
    rect(100, 900, 250, 80)
    
    fill(0)
    textSize(32)
    text(message, 220, 140)
    
    fill(0)
    textSize(32)
    text(message2, 220, 340)
    
    fill(0)
    textSize(32)
    text(message3, 220, 540)
    
    fill(0)
    textSize(32)
    text(message4, 220, 740)
    
    fill(0)
    textSize(32)
    text(message5, 220, 940)
    
        
    fill(255, 193, 224)
    rect(840, 400, 200, 200)

    
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
    
    print(mousePressed)
        
    if Dobbelsteen.isMouseWithinSpace(840, 400, 200, 200):
        if mouseButton == LEFT:
            print('yeet')
            side = int(random(1, 7))
            print('return')
    

    fill(255)
    stroke(204, 102, 0)
    rect(1770, 1010, 127, 35)
    
    fill(0)
    textSize(28)
    text("Terug", width-87, height-47)
    



def mousePress():
    global message, message2, message3, message4, message5, textBoxIsActive, textBox2IsActive, textBox3IsActive, textBox4IsActive, textBox5IsActive, side
    if mouseX >= 100 and mouseX <= 350 and mouseY >=100 and mouseY <=180:
        textBoxIsActive = not textBoxIsActive
    
    if mouseX >= 100 and mouseX <= 350 and mouseY >=300 and mouseY <=380:
        textBox2IsActive = not textBox2IsActive
        
    if mouseX >= 100 and mouseX <= 350 and mouseY >=500 and mouseY <=580:
        textBox3IsActive = not textBox3IsActive
        
    if mouseX >= 100 and mouseX <= 350 and mouseY >=700 and mouseY <=780:
        textBox4IsActive = not textBox4IsActive
        
    if mouseX >= 100 and mouseX <= 350 and mouseY >=900 and mouseY <=980:
        textBox5IsActive = not textBox5IsActive

    if mouseX >= 1770 and mouseX <= 1897 and mouseY >= 1010 and mouseY <= 1045:
        if mousePressed:
            Main.setup()
            scene = 'main'
    
        


def keyPressed():
    global message, message2, message3, message4, message5, textBoxIsActive, textBox2IsActive, textBox3IsActive, textBox4IsActive, textBox5IsActive
    if textBoxIsActive:
        if key == BACKSPACE:
            message = message[:-1]
        else:
            if keyCode == SHIFT:
               return
            if textWidth(message + key) > 250 - 40:
               return
            message += key
        
    if textBox2IsActive:
        if key == BACKSPACE:
            message2 = message2[:-1]
        else:
            if keyCode == SHIFT:
               return
            if textWidth(message2 + key) > 250 - 40:
               return
            message2 += key
            
    if textBox3IsActive:
        if key == BACKSPACE:
            message3 = message3[:-1]
        else:
            if keyCode == SHIFT:
               return
            if textWidth(message3 + key) > 250 - 40:
               return
            message3 += key
            
    if textBox4IsActive:
        if key == BACKSPACE:
            message4 = message4[:-1]
        else:
            if keyCode == SHIFT:
               return
            if textWidth(message4 + key) > 250 - 40:
               return
            message4 += key
            
    if textBox5IsActive:
        if key == BACKSPACE:
            message5 = message5[:-1]
        else:
            if keyCode == SHIFT:
               return
            if textWidth(message5 + key) > 250 - 40:
               return
            message5 += key
