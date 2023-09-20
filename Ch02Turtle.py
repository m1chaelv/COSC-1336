def main():
    import turtle
#    turtle.goto(0,100)
#    turtle.goto(100,100)
#    turtle.goto(100,0)
#    turtle.goto(0,0)
#    turtle.clearscreen()
#    waiting=('ready?')
#    import turtle
    turtle.clearscreen
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,-40)
    turtle.begin_fill()
    turtle.color('red')
    turtle.penup()
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(50,50)
    turtle.pendown()
    turtle.color('black')
    turtle.goto(-50,50)
    turtle.goto(-50,-50)
    turtle.goto(50,-50)
    turtle.goto(50,50)

    number = 2

    if number == 1:
        print('One')
    elif number == 2:
        print('Two')
    elif number == 3:
        print('Three')
    else:
        print('Unknown')
    



main()

    
