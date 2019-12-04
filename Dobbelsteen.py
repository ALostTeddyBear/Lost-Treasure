def setup():
    global side, img
    fullScreen()
    img = loadImage("5.jpg")
    print(img)
    side = int(random(1, 7))
    
        
def draw():
    global side, img
    
    image(img, 0, 0, width, height)
    
    fill(255, 193, 224)
    rect(840, 400, 200, 200)
    
    def mousePressed():
        global side

    
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
        
side = int(random(1, 7))        

    

    
