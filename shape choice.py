import turtle
t = turtle.Pen()
t.speed(100)

def triangle():
        for x in range(size_variable):
            t.forward(x)
            t.left(120)

def square():
        for x in range(size_variable):
            t.forward(x)
            t.left(90)

def leftspiral():
        for x in range(size_variable):
            t.forward(x)
            t.left(91)

def rightspiral():
        for x in range(size_variable):
            t.forward(x)
            t.left(89)

while True:

    instruction = input("""What size would you like the shape?
1) 50
2)100
3)200
4)400.""")
    if instruction == "1":
        size_variable = 50
    if instruction == "2":
        size_variable = 100
    if instruction == "3":
        size_variable = 200
    if instruction == "4":
        size_variable =  400

    instruction = input("""What color would you like your shape?
1) blue
2) red
3) yellow
4) green.""")
    if instruction == "1":
        t.pencolor("blue")
    if instruction == "2":
        t.pencolor("red")
    if instruction == "3":
        t.pencolor("yellow")
    if instruction == "4":
        t.pencolor("green")
    instruction = input("""What shape would you want to draw?
1) triangle
2) square
3) left spiral
4) right spiral.""" )             
    if instruction == "1":
        triangle()
    if instruction == "2":
        square()
    if instruction == "3":
        leftspiral()
    if instruction == "4":
        rightspiral()
click_to_close
