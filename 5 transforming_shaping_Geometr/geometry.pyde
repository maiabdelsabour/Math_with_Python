def setup():
    size(600,600)

def draw():
    ellipse(200,100,20,20)


def draw():
    rect(20,40,50,30)

def draw():
    translate(50,80);
    rect(50,100,100,60)



def draw():
    translate(width/2,height/2);
    rect(50,100,100,60)

def draw():
    translate(200,200);
    rotate(radians(20));
    rect(50,100,100,60)


def draw():
    translate(width/2,height/2);
    for i in range(12):
        ellipse(200,0,50,50)
        rotate(radians(360/12))

def draw():
    translate(width/2,height/2);
    for i in range(12):
        ellipse(200,0,50,50)
        rotate(radians(360/12))


# animate object
t=0
def setup():
    size(600,600)
def draw():
    global t
    #set background white
    background(225)
    translate(width/2,height/2);
    rotate(radians(t))
    for i in range(12):
        rect(200,0,50,50)
        rotate(radians(360/12))
    t+=1


    for i in range(12):
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        rotate(radians(360/12))
    t+=1

    for i in range(12):
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        popMatrix() #return to the saved orientation
        rotate(radians(360/12))
    t+=1

    
    