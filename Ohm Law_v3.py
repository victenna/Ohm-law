import turtle,time
turtle.tracer(2)
wn=turtle.Screen()
wn.setup(1200,700)
wn.bgpic('bground3.gif')
wn.addshape('electrons.gif')      
t1=turtle.Turtle()
t1.setheading(0)
t1.shapesize(1)
t1.pensize(5)
t1.color('black')
t1.hideturtle()
t1.down
t1.goto(0,0)
for j in range (2):
    t1.fd(500)
    t1.right(90)
    t1.fd(200)
    t1.right(90)
    
t1.up()
t1.goto(200,20)
t1.down()
t1.color('grey')
t1.begin_fill()
for j in range (2):
    t1.fd(100)
    t1.right(90)
    t1.fd(40)
    t1.right(90)
t1.end_fill()
t1.up()    
t1.color('black')
t1.shape('square')
t1.shapesize(0.2,2)
t1.goto(0,-100)
t1.showturtle()
t1.stamp()
t1.up()
t1.goto(0,-120)
t1.down()
t1.shapesize(0.2,4)
t1.stamp()
t1.up()
t1.goto(0,-110)
t1.down()
t1.color('gold')
t1.shapesize(0.7,1)
t1.up()

#-----------------------------------------
electron=[]
X=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for n in range(14):
    electron.append(turtle.Turtle('electrons.gif'))
    #electron[n].color('light blue')
    electron[n].up()
    electron[n].shapesize(1.5)
    if n>-1 and n<5:
        electron[n].goto(n*100,0)
        electron[n].setheading(0)
    if n>4 and n<7:
        electron[n].goto(500,-(n-5)*100)
        electron[n].setheading(-90)
    if n>6 and n<12:
        electron[n].goto(500-(n-7)*100,-200)
        electron[n].setheading(180)
    if n>11:
        electron[n].goto(0,-200+100*(n-12))
        electron[n].setheading(90)
    X[n]=electron[n].xcor()
    Y[n]=electron[n].ycor()
    print(n,X[n],Y[n])
        
while True:        
    for n in range(14):
        X[n]=electron[n].xcor()
        Y[n]=electron[n].ycor()
        
        if abs(X[n]-500)<0.001 and abs(Y[n])<0.001:
            electron[n].setheading(-90)
            
        if abs(X[n]-500)<0.001 and abs(Y[n]+200)<0.001:
            electron[n].setheading(180)
            
        if abs(X[n])<0.001 and abs(Y[n]+200)<0.001:
            electron[n].setheading(90)
            
        if abs(X[n])<0.001 and abs(Y[n])<0.001:
            electron[n].setheading(0)
            
        electron[n].fd(1)
        
