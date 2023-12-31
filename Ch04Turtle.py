import turtle

# This program draws a design using repeated lines.
def spiral_lines():
# Named constants
    START_X = -200       # Starting X coordinate
    START_Y = 0          # Starting Y coordinate
    NUM_LINES = 36       # Number of lines to draw
    LINE_LENGTH = 400    # Length of each line
    ANGLE = 170          # Angle to turn
    ANIMATION_SPEED = 0  # Animation speed

    # Move the turtle to its initial position.
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.pendown()

    # Set the animation speed.
    turtle.speed(ANIMATION_SPEED)

    # Draw 36 lines, with the turtle tilted
    # by 170 degrees after each line is drawn.
    for x in range(NUM_LINES):
        turtle.forward(LINE_LENGTH)
        turtle.left(ANGLE)

# This program draws a design using repeated circles.
def spiral_circles():
  # Named constants
  NUM_CIRCLES = 36    # Number of circles to draw
  RADIUS = 100        # Radius of each circle
  ANGLE = 10          # Angle to turn
  ANIMATION_SPEED = 0 # Animation speed
  
  # Set the animation speed.
  turtle.speed(ANIMATION_SPEED)
  
  # Draw 36 circles, with the turtle tilted
  # by 10 degrees after each circle is drawn.
  for x in range(NUM_CIRCLES):
     turtle.circle(RADIUS)
     turtle.left(ANGLE)

# This program draws a square
def sqr_1():
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)


# This program draws an octagon
def oct_1():
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)

def main():
    menu=0
    print('')
    while menu >= 0 and menu <= 4:
        print('[1]\tTurtle: Spiral Lines')
        print('[2]\tTurtle: Spiral Circles')
        print('[3]\tTurtle: Square')
        print('[4]\tTurtle: Octagon')
        print('...\tanything else to exit\n')
        menu=int(input('Make a selection to continue: '))
        turtle.reset()
        if menu==1:
            spiral_lines()
        elif menu==2:
            spiral_circles()
        elif menu==3:
            sqr_1()
        elif menu==4:
            oct_1()
        else:
            menu=-1
main()