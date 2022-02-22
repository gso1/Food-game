# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
from random import seed
from random import randint


def setup():
    global vehicle
    global food
    global img
    global img2
    global img3
    
    global f
    size(200,200)
    f = createFont("Arial",16)


    size(640, 360)
    seed(1)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(width/3, height/3, velocity)
    img = loadImage("bozo.png")
    img.resize(60,70)
    
    img2 = loadImage("moca.png")
    img2.resize(25,40)
    
    img3 = loadImage("fundo.png")
    img3.resize(640,360)
def draw():
    image(img3,0,0)
    

    textFont(f,16)            
    fill(255)                       
    text("Score: ",5,13)
    text(str(vehicle.score) ,70,13)
    
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display(img)
    
    food.update()
    food.display(img2)
    xv = vehicle.position.x
    yv = vehicle.position.y
    
    xf = food.position.x
    yf = food.position.y
    
    vehicle.velocity = PVector(xf-xv, yf-yv)
    
    if food.position == vehicle.position:
        food.position = PVector(randint(0,width), randint(0,height))
        vehicle.score = vehicle.score +1
