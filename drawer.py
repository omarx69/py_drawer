import turtle



turtle.color("blue")

#shapes
def shape_circle():
    turtle.shape("circle")


def shape_square():
    turtle.shape("square")


def shape_arrow():
    turtle.shape("arrow")


def shape_turtleurturtlele():
    turtle.shape("turtle")


def shape_turtleriangle():
    turtle.shape("triangle")


def shape_classic():
    turtle.shape("classic")
#-------------------------------------------------------------------

#angles
def turn_90():
    turtle.right(90)

def turn_90_L():
    turtle.left(90)

def turn_45():
    turtle.right(45)

def turn_45_L():
    turtle.left(45)

#----------------------------

def fd():
    turtle.fd(100)

def bk():
    turtle.bk(100)

    
#-----------------------------
turtle.listen()



turtle.onkey(fd, "Return")        
turtle.onkey(bk, "Delete")

turtle.onkey(turn_90, "r")        
turtle.onkey(turn_90_L, "l")

turtle.onkey(turn_45, "R")        
turtle.onkey(turn_45_L, "L")
#----------------------------
turtle.mainloop()