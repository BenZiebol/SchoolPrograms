import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose:
#   Computes the total number of cents with the given change
# Input Parameter(s):
#   Quaters-the number of quarters
#   Dimes-the number of Dimes
#   Nickels-the number of Nickels
#   Pennies-the number of pennies
# Return Value:
#   Int-returns the total change of the coins in cents
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose:
#   Draws the univerty of Minnesota logo
# Input Parameter(s):
#   NONE
# Return Value:
#   NONE-Visual display of the UofMN logo
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose:
#   Draw a 8 sided star
# Input Parameter(s):
#   None
# Return Value:
#   NONE-Visual display of a 8 sided star
#==========================================

def star8():
    turtle.speed(0)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    turtle.forward(200)
    turtle.left(90+45)
    
    


# Part C: trajectory
#==========================================
# Purpose:
#   Calculates how far the object will travel
# Input Parameter(s):
#   Height-starting height, in meters
#   Speed-starting speed, in m/s
#   angle-angle at which the object is thrown, in degrees
# Return Value:
#   Float-distance the object travels before hitting the ground, in meters
#==========================================

def trajectory(height, speed, angle):
    angle_radians=angle/180*math.pi
    speed_horizontal=speed*math.cos(angle_radians)
    speed_vertical=speed*math.sin(angle_radians)
    time=(speed_vertical + math.sqrt(speed_vertical**2 + 19.6 * height)) / 9.8
    return speed_horizontal*time
    
#print(round(trajectory(0,20,25),3))        Test

