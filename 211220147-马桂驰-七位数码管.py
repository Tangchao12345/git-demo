import turtle, time

def drawLine(draw):
    turtle.pendown()
    if not draw :
        turtle.penup()
    turtle.fd(40)
    turtle.right(90)

def drawNum(num):
    if num in [2, 3, 4, 5, 6, 8, 9] :
        drawLine(True)
    else:
        drawLine(False)
    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9] :
        drawLine(True)
    else:
        drawLine(False)
    if num in [0, 2, 3, 5, 6, 8, 9] :
        drawLine(True)
    else:
        drawLine(False)
    if num in [0, 2, 6, 8] :
        drawLine(True)
    else:
        drawLine(False)
    turtle.left(90)
    if num in [0, 4, 5, 6, 8, 9] :
        drawLine(True)
    else:
        drawLine(False)
    if num in [0, 2, 3, 5, 6, 7, 8, 9] :
        drawLine(True)
    else:
        drawLine(False)
    if num in [0, 1, 2, 3, 4, 7, 8, 9] :
        drawLine(True)
    else: drawLine(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)

def drawtime(time):
    for i in time:
        drawNum(int(i))

if __name__ == '__main__':
    turtle.setup()
    turtle.penup()
    turtle.pencolor("green")
    turtle.fd(-350)
    turtle.pensize(5)
    turtle.speed(10)
    drawtime(time.strftime('%Y%m%d'))
    turtle.hideturtle()
    turtle.done()